"""Category discovery.

Categories are **derived from the data**, not declared up front.

The first design hard-coded twelve categories chosen by hand from a handful of
examples. That had two problems: the taxonomy reflected whoever wrote it rather
than what the ecosystem looks like, and a tool spanning several problem areas
had to be forced into exactly one.

Why the obvious approaches do not work
--------------------------------------
Clustering *capabilities* by co-occurrence fails here. The capability frequency
distribution is a smooth continuum (74%, 65%, 54%, 52%, 47% ... 3%), so there is
no natural cut, and the two most common capabilities drag ~95% of tools into one
mega-cluster that says nothing.

What works is weighting each capability by how much it *distinguishes* a tool:

    prominence(tool, capability) = idf(capability) x log(1 + mentions)

``idf`` suppresses capabilities nearly every tool claims, and the mention count
rewards tools that actually emphasise the feature rather than name-dropping it.
Each tool becomes a normalised vector of prominences; clustering those vectors by
cosine similarity produces categories that are genuinely distinct, and every
capability ends up as some tool's strongest signal.

A tool belongs to *every* category it is prominent in — magpie does both
multi-account switching and model routing — with the strongest as its primary.

Stability matters as much as correctness: a curated list whose sections
reshuffle nightly is unusable, so a cluster inherits the previous run's slug and
human-edited title when its membership is broadly unchanged.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Iterable

from .readme_analysis import capability_label, capability_short
from .util import DATA_DIR, LOG, read_json, slugify, write_json

CATEGORIES_PATH = DATA_DIR / "categories.json"

#: Cosine similarity at which two clusters merge. Tuned by sweeping the value
#: and reading the resulting sections: 0.20 collapses to 3 mega-categories,
#: 0.36 shatters into 15 fragments, 0.32 yields 12 well-sized sections.
DEFAULT_MERGE_THRESHOLD = 0.32

#: A second capability is added to a category title only when its lift is at
#: least this fraction of the leader's, so titles read as one coherent topic.
TITLE_PAIRING_RATIO = 0.75

#: Stop merging at this many clusters, so a small crawl still yields a readable
#: taxonomy instead of one giant section.
MAX_CLUSTERS = 16

#: A category needs at least this many tools to be worth a section.
MIN_CLUSTER_TOOLS = 3

#: A tool is cross-listed under another category when it shares at least this
#: many of that category's defining capabilities. Cross-listing is deliberately
#: scarce: with a looser rule sub2api appeared under seven of ten sections, which
#: makes the membership signal worthless. Two matches against a category's top
#: three capabilities means the tool genuinely does that category's job.
SECONDARY_CAPABILITY_MATCHES = 2

#: Hard ceiling on how many categories one tool may appear in. Beyond this the
#: tool is a platform rather than a member of any particular problem area.
MAX_CATEGORIES_PER_TOOL = 3

#: Capabilities on more than this share of tools are ecosystem-wide, not
#: category-defining; they get zero weight in the vectors.
UBIQUITY_CEILING = 0.60


@dataclass
class Cluster:
    """A discovered category."""

    slug: str
    capabilities: list[str]
    tools: list[str] = field(default_factory=list)
    primary_tools: list[str] = field(default_factory=list)
    title_en: str = ""
    title_zh: str = ""
    tagline_en: str = ""
    tagline_zh: str = ""
    problem_en: str = ""
    problem_zh: str = ""
    stability: float = 0.0
    cohesion: float = 0.0

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.slug,
            "title": {"en": self.title_en, "zh": self.title_zh},
            "tagline": {"en": self.tagline_en, "zh": self.tagline_zh},
            "problem": {"en": self.problem_en, "zh": self.problem_zh},
            "capabilities": self.capabilities,
            "tools": sorted(self.primary_tools),
            "also_in": sorted(set(self.tools) - set(self.primary_tools)),
            "stability": round(self.stability, 3),
            "cohesion": round(self.cohesion, 3),
        }


# --------------------------------------------------------------------------
# Prominence vectors
# --------------------------------------------------------------------------


def capability_tool_sets(entries: Iterable[dict[str, Any]]) -> dict[str, set[str]]:
    """Map each capability to the tools that document it."""
    sets: dict[str, set[str]] = {}
    for entry in entries:
        key = entry["full_name"].lower()
        for cap in entry.get("analysis", {}).get("capabilities", []):
            sets.setdefault(cap, set()).add(key)
    return sets


def compute_idf(tool_sets: dict[str, set[str]], total: int) -> dict[str, float]:
    """Inverse document frequency: rare capabilities are informative."""
    return {
        cap: math.log(total / len(tools)) if tools else 0.0
        for cap, tools in tool_sets.items()
    }


def split_ubiquitous(
    tool_sets: dict[str, set[str]],
    total: int,
    *,
    ceiling: float = UBIQUITY_CEILING,
) -> tuple[dict[str, set[str]], list[str]]:
    """Separate distinctive capabilities from ecosystem-wide ones.

    A capability present on almost every tool cannot define a category: it
    describes the whole field. ``cross-agent-support`` was claimed by 75% of
    tools and ``mcp-support`` by 65%, and including them collapsed the taxonomy
    into one 137-tool section.

    Returns ``(distinctive, ubiquitous)``.
    """
    if total <= 0:
        return dict(tool_sets), []
    distinctive: dict[str, set[str]] = {}
    ubiquitous: list[str] = []
    for cap, tools in tool_sets.items():
        if len(tools) / total > ceiling:
            ubiquitous.append(cap)
        else:
            distinctive[cap] = tools
    return distinctive, sorted(ubiquitous)


def prominence_vector(
    entry: dict[str, Any],
    idf: dict[str, float],
    *,
    ubiquitous: set[str] | None = None,
) -> dict[str, float]:
    """Weighted, L2-normalised capability vector for one tool.

    Returns an empty vector when every capability the tool has is either
    ubiquitous or unknown — such a tool cannot be placed by content.
    """
    analysis = entry.get("analysis") or {}
    hits = analysis.get("capability_hits") or {}
    ubiquitous = ubiquitous or set()

    vector: dict[str, float] = {}
    for cap in analysis.get("capabilities") or []:
        if cap in ubiquitous:
            continue
        weight = idf.get(cap, 0.0) * math.log(1 + max(int(hits.get(cap, 1)), 0))
        if weight > 0:
            vector[cap] = weight

    norm = math.sqrt(sum(w * w for w in vector.values()))
    if norm <= 0:
        return {}
    return {cap: w / norm for cap, w in vector.items()}


def cosine(a: dict[str, float], b: dict[str, float]) -> float:
    """Cosine similarity of two L2-normalised sparse vectors."""
    if not a or not b:
        return 0.0
    if len(a) > len(b):
        a, b = b, a
    return sum(w * b.get(cap, 0.0) for cap, w in a.items())


def centroid(vectors: list[dict[str, float]]) -> dict[str, float]:
    """Normalised mean of a set of vectors."""
    if not vectors:
        return {}
    acc: dict[str, float] = {}
    for vec in vectors:
        for cap, weight in vec.items():
            acc[cap] = acc.get(cap, 0.0) + weight
    norm = math.sqrt(sum(w * w for w in acc.values()))
    if norm <= 0:
        return {}
    return {cap: w / norm for cap, w in acc.items()}


# --------------------------------------------------------------------------
# Clustering
# --------------------------------------------------------------------------


def similarity_matrix(vectors: dict[str, dict[str, float]]) -> dict[tuple[str, str], float]:
    """Precompute pairwise cosine similarity, keyed by sorted name pair."""
    names = sorted(vectors)
    matrix: dict[tuple[str, str], float] = {}
    for i, a in enumerate(names):
        for b in names[i + 1 :]:
            matrix[(a, b)] = cosine(vectors[a], vectors[b])
    return matrix


def cluster_tools(
    vectors: dict[str, dict[str, float]],
    *,
    threshold: float = DEFAULT_MERGE_THRESHOLD,
    max_clusters: int = MAX_CLUSTERS,
) -> list[list[str]]:
    """Agglomerative clustering with **average linkage**.

    Average linkage (mean pairwise similarity between the two groups' members)
    is used rather than centroid linkage on purpose. Centroid similarity between
    two large groups regresses toward the mean of the whole corpus, so it stays
    above any fixed threshold and the algorithm chains everything into a single
    cluster — which is exactly what happened with the first implementation.

    Deterministic: ties break on name order, so identical input always yields
    identical clusters and the nightly diff stays meaningful.
    """
    names = sorted(vectors)
    if not names:
        return []

    sim = similarity_matrix(vectors)
    clusters: list[list[str]] = [[n] for n in names]

    def linkage(a: list[str], b: list[str]) -> float:
        total = 0.0
        for x in a:
            for y in b:
                total += sim[(x, y)] if x < y else sim[(y, x)]
        return total / (len(a) * len(b))

    while len(clusters) > 1:
        best: tuple[float, int, int] | None = None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                score = linkage(clusters[i], clusters[j])
                if best is None or score > best[0]:
                    best = (score, i, j)
        if best is None:
            break
        score, i, j = best
        if score < threshold:
            break
        merged = sorted(clusters[i] + clusters[j])
        clusters = [c for k, c in enumerate(clusters) if k not in (i, j)]
        clusters.append(merged)
        clusters.sort()

    # If the threshold left more sections than is readable, merge the closest
    # pairs until the taxonomy is a sensible size.
    while len(clusters) > max_clusters:
        best = None
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                score = linkage(clusters[i], clusters[j])
                if best is None or score > best[0]:
                    best = (score, i, j)
        if best is None:
            break
        _, i, j = best
        merged = sorted(clusters[i] + clusters[j])
        clusters = [c for k, c in enumerate(clusters) if k not in (i, j)]
        clusters.append(merged)
        clusters.sort()

    return sorted(clusters, key=lambda c: (-len(c), c[0]))


def cluster_signature(
    members: list[str],
    vectors: dict[str, dict[str, float]],
    *,
    corpus_mean: dict[str, float] | None = None,
    limit: int = 6,
) -> list[str]:
    """The capabilities that best characterise a cluster.

    Ranked by **lift** — how much more prominent a capability is inside this
    cluster than across the corpus — rather than raw prominence. Raw prominence
    ranks ``agent-runtime`` and ``skills-plugins`` top of almost every cluster
    because they are common everywhere, which produced titles like
    "Skills & Orchestration" for groups that were really about something else.
    Lift surfaces what makes *this* group distinct.
    """
    if not members:
        return []
    acc: dict[str, float] = {}
    for name in members:
        for cap, weight in vectors.get(name, {}).items():
            acc[cap] = acc.get(cap, 0.0) + weight
    means = {cap: total / len(members) for cap, total in acc.items()}

    baseline = corpus_mean or {}
    floor = (sum(baseline.values()) / len(baseline)) if baseline else 0.0

    def lift(cap: str) -> float:
        base = max(baseline.get(cap, 0.0), floor * 0.25, 1e-6)
        return means[cap] / base

    return sorted(means, key=lambda cap: (-lift(cap), cap))[:limit]


def signature_lift(
    signature: list[str],
    members: list[str],
    vectors: dict[str, dict[str, float]],
    corpus_mean: dict[str, float],
) -> list[float]:
    """Lift values for a signature, used to decide how to title a category."""
    acc: dict[str, float] = {}
    for name in members:
        for cap, weight in vectors.get(name, {}).items():
            acc[cap] = acc.get(cap, 0.0) + weight
    means = {cap: total / max(len(members), 1) for cap, total in acc.items()}
    floor = (sum(corpus_mean.values()) / len(corpus_mean)) if corpus_mean else 0.0
    out: list[float] = []
    for cap in signature:
        base = max(corpus_mean.get(cap, 0.0), floor * 0.25, 1e-6)
        out.append(means.get(cap, 0.0) / base)
    return out


def corpus_means(vectors: dict[str, dict[str, float]]) -> dict[str, float]:
    """Mean prominence of each capability across the whole corpus."""
    acc: dict[str, float] = {}
    counts: dict[str, int] = {}
    for vec in vectors.values():
        for cap, weight in vec.items():
            acc[cap] = acc.get(cap, 0.0) + weight
            counts[cap] = counts.get(cap, 0) + 1
    total = max(len(vectors), 1)
    return {cap: acc[cap] / total for cap in acc}


# --------------------------------------------------------------------------
# Naming
# --------------------------------------------------------------------------


def capability_problem(cap_id: str, lang: str = "en") -> str:
    from .readme_analysis import capabilities as all_caps

    for cap in all_caps():
        if cap["id"] == cap_id:
            return (cap.get("problem") or {}).get(lang, "")
    return ""


def name_cluster(
    signature: list[str],
    lifts: list[float] | None = None,
) -> dict[str, str]:
    """Build a human title from the cluster's signature capabilities.

    Only capabilities of comparable distinctiveness are paired in the title.
    Pairing the top two unconditionally produced names like "Security & Voice"
    and "Providers & Desktop UI", where the second word was a weak, incidental
    member that made the section sound arbitrary. A second word is included only
    when its lift is close to the leader's; otherwise the single strongest
    capability names the category.

    Names come from the capability catalogue, so adding a capability
    automatically gives a future category a name without touching this module.
    """
    if not signature:
        return {
            "title_en": "Other",
            "title_zh": "其他",
            "tagline_en": "",
            "tagline_zh": "",
            "problem_en": "",
            "problem_zh": "",
        }

    lifts = lifts or [1.0] * len(signature)
    paired = [signature[0]]
    if len(signature) > 1 and lifts[1] >= lifts[0] * TITLE_PAIRING_RATIO:
        paired.append(signature[1])

    title_en = " & ".join(capability_short(c, "en") for c in paired)
    title_zh = "与".join(capability_short(c, "zh") for c in paired)

    return {
        "title_en": title_en,
        "title_zh": title_zh,
        "tagline_en": capability_label(signature[0], "en"),
        "tagline_zh": capability_label(signature[0], "zh"),
        "problem_en": capability_problem(signature[0], "en"),
        "problem_zh": capability_problem(signature[0], "zh"),
    }


# --------------------------------------------------------------------------
# Stability
# --------------------------------------------------------------------------


def load_previous() -> dict[str, dict[str, Any]]:
    data = read_json(CATEGORIES_PATH, default={}) or {}
    return {c["id"]: c for c in data.get("categories", [])}


def match_previous(
    signature: list[str],
    previous: dict[str, dict[str, Any]],
    taken: set[str],
) -> tuple[str, float]:
    """Find the previous category this cluster continues, if any."""
    best_slug, best_score = "", 0.0
    caps = set(signature)
    for slug, prev in previous.items():
        if slug in taken:
            continue
        prev_caps = set(prev.get("capabilities") or [])
        if not prev_caps or not caps:
            continue
        score = len(caps & prev_caps) / len(caps | prev_caps)
        if score > best_score:
            best_slug, best_score = slug, score
    return best_slug, best_score


# --------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------


def discover_categories(
    entries: list[dict[str, Any]],
    *,
    threshold: float = DEFAULT_MERGE_THRESHOLD,
) -> list[Cluster]:
    """Derive categories from the capability data. Pure; writes nothing.

    Mutates each entry to add ``categories`` and ``primary_category``.
    """
    tool_sets = capability_tool_sets(entries)
    if not tool_sets or not entries:
        return []

    total = len(entries)
    idf = compute_idf(tool_sets, total)
    ubiquitous = {c for c, t in tool_sets.items() if len(t) / total > UBIQUITY_CEILING}
    if ubiquitous:
        LOG.info("ubiquitous capabilities excluded from clustering: %s", ", ".join(sorted(ubiquitous)))

    vectors: dict[str, dict[str, float]] = {}
    for entry in entries:
        vec = prominence_vector(entry, idf, ubiquitous=ubiquitous)
        if vec:
            vectors[entry["full_name"].lower()] = vec

    if not vectors:
        return []

    raw = cluster_tools(vectors, threshold=threshold)
    previous = load_previous()
    baseline = corpus_means(vectors)
    taken: set[str] = set()
    clusters: list[Cluster] = []
    membership: dict[str, list[str]] = {}

    for members in raw:
        if len(members) < MIN_CLUSTER_TOOLS:
            # Too small to be a section of its own; its tools are re-placed by
            # similarity in assign_tools rather than dropped.
            continue
        signature = cluster_signature(members, vectors, corpus_mean=baseline)
        names = name_cluster(
            signature,
            signature_lift(signature, members, vectors, baseline),
        )
        prev_slug, stability = match_previous(signature, previous, taken)

        if prev_slug and stability >= 0.5:
            slug = prev_slug
            taken.add(prev_slug)
            # Preserve a human-edited title across runs.
            title = (previous[prev_slug].get("title") or {})
            names["title_en"] = title.get("en") or names["title_en"]
            names["title_zh"] = title.get("zh") or names["title_zh"]
        else:
            slug = slugify(names["title_en"])
            base, n = slug, 2
            while slug in taken or slug in {c.slug for c in clusters}:
                slug = f"{base}-{n}"
                n += 1

        centre = centroid([vectors[m] for m in members])
        cohesion = sum(cosine(vectors[m], centre) for m in members) / len(members)
        clusters.append(
            Cluster(
                slug=slug,
                capabilities=signature,
                title_en=names["title_en"],
                title_zh=names["title_zh"],
                tagline_en=names["tagline_en"],
                tagline_zh=names["tagline_zh"],
                problem_en=names["problem_en"],
                problem_zh=names["problem_zh"],
                stability=stability,
                cohesion=cohesion,
            )
        )
        membership[slug] = members

    if not clusters:
        return []

    assign_tools(clusters, membership, entries, vectors)
    clusters.sort(key=lambda c: (-len(c.primary_tools), c.title_en))
    return clusters


def assign_tools(
    clusters: list[Cluster],
    membership: dict[str, list[str]],
    entries: list[dict[str, Any]],
    vectors: dict[str, dict[str, float]],
) -> None:
    """Attach tools to every category they belong to.

    A tool is listed under a category when it has a capability that the category
    is *about* — not merely when it sits near the cluster centroid. Cosine
    proximity alone put magpie only under account management, even though it
    routes models between providers, which is exactly the multi-category
    behaviour this is meant to capture.

    Primary = the closest cluster by cosine. Secondary = the tool has at least
    ``SECONDARY_CAPABILITY_MATCHES`` of that cluster's signature capabilities.
    """
    centroids = {
        c.slug: centroid([vectors[m] for m in membership.get(c.slug, []) if m in vectors])
        for c in clusters
    }
    centroids = {slug: vec for slug, vec in centroids.items() if vec}

    # The strongest few capabilities of each cluster, which define its topic.
    topics = {c.slug: set(c.capabilities[:3]) for c in clusters}

    for entry in entries:
        key = entry["full_name"].lower()
        vec = vectors.get(key)

        if not vec or not centroids:
            # Every capability is ecosystem-wide; park it in the largest
            # category so it does not silently vanish from the index.
            largest = clusters[0]
            largest.tools.append(key)
            largest.primary_tools.append(key)
            entry["categories"] = [largest.slug]
            entry["primary_category"] = largest.slug
            continue

        scored = sorted(
            ((cosine(vec, centroids[slug]), slug) for slug in centroids),
            key=lambda pair: (-pair[0], pair[1]),
        )
        _, best_slug = scored[0]

        # The tool's own capabilities, strongest first.
        own = [cap for cap, _ in sorted(vec.items(), key=lambda kv: (-kv[1], kv[0]))]

        # Rank the other categories by how much of their topic this tool covers,
        # so the cap keeps the *best* matches rather than an arbitrary subset.
        extras: list[tuple[int, float, str]] = []
        for slug, caps in topics.items():
            if slug == best_slug:
                continue
            overlap = len(set(own) & caps)
            if overlap >= SECONDARY_CAPABILITY_MATCHES:
                extras.append((overlap, cosine(vec, centroids[slug]), slug))

        extras.sort(key=lambda item: (-item[0], -item[1], item[2]))
        chosen = [best_slug] + [slug for _, _, slug in extras[: MAX_CATEGORIES_PER_TOOL - 1]]

        for slug in chosen:
            next(c for c in clusters if c.slug == slug).tools.append(key)
        next(c for c in clusters if c.slug == best_slug).primary_tools.append(key)
        entry["categories"] = sorted(chosen)
        entry["primary_category"] = best_slug


def save_categories(clusters: list[Cluster], generated_at: str | None = None) -> None:
    write_json(
        CATEGORIES_PATH,
        {
            "generated_at": generated_at,
            "count": len(clusters),
            "categories": [c.as_dict() for c in clusters],
        },
    )
    LOG.info(
        "discovered %d categories: %s",
        len(clusters),
        ", ".join(f"{c.slug}({len(c.primary_tools)})" for c in clusters),
    )
