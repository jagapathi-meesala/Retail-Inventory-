from adapters.tool_loader import ToolRegistry
from core.agent_core import AgentCore
from adapters.registry import AdapterRegistry

def test_adapter_names_and_invocation():
 reg=AdapterRegistry(AgentCore(ToolRegistry())); assert reg.names()==["claude-code","crewai","lyzr","openai-sdk"]
 assert reg.get("openai-sdk").invoke("summarize-stock",{"items":[{"sku":"A","stock":2}]})["ok"]
