from adapters.tool_loader import ToolRegistry
from core.agent_core import AgentCore

def test_agent_structured_response():
 a=AgentCore(ToolRegistry()); out=a.run("recommend-reorder",{"current_stock":10,"reorder_point":5,"target_stock":10}); assert out=={"ok":True,"tool":"recommend-reorder","data":{"recommended_order_quantity":0.0,"action":"no_action","reason":"Restore stock to target level when current stock is below target."}}
