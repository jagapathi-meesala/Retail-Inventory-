"""Portable adapter interfaces; no framework dependency."""
from abc import ABC, abstractmethod
from typing import Mapping, TYPE_CHECKING
if TYPE_CHECKING:
    from core.agent_core import AgentCore

class AgentAdapter(ABC):
    name = "framework-independent"
    @abstractmethod
    def invoke(self, tool: str, inputs: Mapping) -> dict: ...

class OpenAIAdapter(AgentAdapter):
    name = "openai-sdk"
    def __init__(self, core): self.core = core
    def invoke(self, tool, inputs): return self.core.run(tool, inputs)

class CrewAIAdapter(AgentAdapter):
    name = "crewai"
    def __init__(self, core): self.core = core
    def invoke(self, tool, inputs): return self.core.run(tool, inputs)

class ClaudeCodeAdapter(AgentAdapter):
    name = "claude-code"
    def __init__(self, core): self.core = core
    def invoke(self, tool, inputs): return self.core.run(tool, inputs)

class LyzrAdapter(AgentAdapter):
    name = "lyzr"
    def __init__(self, core): self.core = core
    def invoke(self, tool, inputs): return self.core.run(tool, inputs)
