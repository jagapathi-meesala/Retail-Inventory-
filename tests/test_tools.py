from adapters.tool_loader import ToolRegistry

def test_discovery_and_analysis():
 r=ToolRegistry(); assert r.names()==["analyze-inventory","recommend-reorder","summarize-stock"]
 out=r.execute("analyze-inventory",{"items":[{"sku":"A","stock":0,"reorder_point":5},{"sku":"B","stock":6,"reorder_point":5},{"sku":"C","stock":8,"reorder_point":5}]})
 assert out.ok and out.data["counts"]=={"critical":1,"low":0,"healthy":2}

def test_reorder_and_summary():
 r=ToolRegistry(); out=r.execute("recommend-reorder",{"current_stock":8,"reorder_point":5,"target_stock":20}); assert out.data["recommended_order_quantity"]==12
 s=r.execute("summarize-stock",{"items":[{"sku":"A","stock":0},{"sku":"B","stock":10}]}); assert s.data["total_units"]==10 and s.data["zero_stock_skus"]==["A"]
