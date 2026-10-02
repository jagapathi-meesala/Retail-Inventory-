"""Adapter registry independent of external AI frameworks."""
from .portable_adapter import OpenAIAdapter, CrewAIAdapter, ClaudeCodeAdapter, LyzrAdapter

class AdapterRegistry:
    def __init__(self, core):
        self._adapters = {c.name: c(core) for c in (OpenAIAdapter, CrewAIAdapter, ClaudeCodeAdapter, LyzrAdapter)}
    def names(self): return sorted(self._adapters)
    def get(self, name):
        if name not in self._adapters: raise KeyError(f"Unknown adapter: {name}")
        return self._adapters[name]
