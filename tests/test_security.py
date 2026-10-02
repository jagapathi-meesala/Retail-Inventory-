from adapters.tool_loader import ToolRegistry

def test_invalid_inputs_rejected():
 r=ToolRegistry()
 assert not r.execute("recommend-reorder",{"current_stock":-1,"reorder_point":0,"target_stock":2}).ok
 assert not r.execute("analyze-inventory",{"items":[{"sku":"A","stock":1}]}).ok
 assert not r.execute("summarize-stock",{"items":[{"sku":"","stock":1}]}).ok

def test_malformed_input_rejected():
 r=ToolRegistry(); assert not r.execute("summarize-stock",{"items":"not-a-list"}).ok
