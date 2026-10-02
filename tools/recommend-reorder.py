"""Deterministic reorder quantity recommendation."""
from contracts.tool_contract import ToolContract, ToolMetadata

def validate(data):
    for k in ("current_stock","reorder_point","target_stock"):
        if k not in data: raise ValueError(f"missing required field: {k}")
        v=data[k]
        if isinstance(v,bool) or not isinstance(v,(int,float)) or v<0: raise ValueError(f"{k} must be a non-negative number")
    if data["target_stock"] < data["reorder_point"]: raise ValueError("target_stock must be >= reorder_point")

def execute(data):
    qty=max(0.0,float(data["target_stock"])-float(data["current_stock"]))
    return {"recommended_order_quantity":qty,"action":"reorder" if qty>0 else "no_action","reason":"Restore stock to target level when current stock is below target."}

tool=ToolContract(ToolMetadata("recommend-reorder","Recommend replenishment quantity from current, reorder-point, and target stock.",{"type":"object","required":["current_stock","reorder_point","target_stock"]}),validate,execute)
