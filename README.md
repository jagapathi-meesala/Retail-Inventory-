# Retail Inventory Agent

Framework-independent Python agent for retail inventory analysis. It provides deterministic stock-health classification, replenishment quantity calculation, and aggregate stock summaries.

## Architecture
`agent.yaml` defines the OpenGAP manifest. `contracts/` defines the framework-independent tool interface, `tools/` contains domain implementations, `adapters/tool_loader.py` discovers tools dynamically, `core/` executes them, and `adapters/portable_adapter.py` provides thin invocation adapters for OpenAI SDK, CrewAI, Claude Code, and Lyzr without importing those frameworks.

## Installation
Use Python 3.11+ and install `requirements.txt`.

## Configuration
Runtime configuration is supplied through environment variables shown in `.env.example`. No API keys or production credentials are included.

## Tools
- `analyze-inventory`: classify SKU stock health and calculate shortfall.
- `recommend-reorder`: calculate replenishment quantity to target stock.
- `summarize-stock`: calculate aggregate stock metrics.

## Skills
- `inventory-analysis`: inventory health assessment.
- `replenishment-planning`: deterministic replenishment planning.

## Usage
Use `ToolRegistry` to discover tools dynamically and `AgentCore.run()` to execute a tool with validated structured input.

## Testing
Run `pytest -q` and `python verification/readiness_audit.py`.

## Portability
The core contract has no CrewAI, LangChain, OpenAI, Claude, or Lyzr dependency. Thin adapters expose the same invocation contract; this repository does not claim vendor compatibility testing or certification.

## Limitations
No external inventory database, demand forecasting, supplier lead-time optimization, purchase-order execution, or real-time retail integration is implemented.
