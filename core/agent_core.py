"""Core execution engine."""
from typing import Mapping

class AgentCore:
    def __init__(self, registry):
        self.registry = registry

    def run(self, tool_name: str, inputs: Mapping) -> dict:
        result = self.registry.execute(tool_name, inputs)
        if result.ok:
            return {"ok": True, "tool": tool_name, "data": result.data}
        return {"ok": False, "tool": tool_name, "error": {"code": result.error.code, "message": result.error.message}}

def build_agent(tool_registry):
    from adapters.registry import AdapterRegistry
    core = AgentCore(tool_registry)
    return core, AdapterRegistry(core)
