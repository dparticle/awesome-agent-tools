"""agentindex — the engine behind awesome-agent-tools.

Modules
-------
util              shared IO / text helpers
github            GitHub REST client with on-disk caching and rate-limit budget
discover          candidate discovery via the GitHub search API
readme_analysis   README -> capabilities, setup effort, friendliness, doc quality
scoring           health score, quality gates, tiers, momentum
supersede         the elimination engine (supersede / dormant / deprecated)
render            README + docs generation
"""

__version__ = "1.0.0"

SCHEMA_VERSION = 1
