# AGENTS.md

Use the framework-independent core and tool contracts as the source of execution behavior. Validate inputs before invoking tools, preserve structured errors, and do not introduce runtime secrets or hardcoded external configuration.

The agent is advisory: inventory calculations do not place orders or mutate external systems.
