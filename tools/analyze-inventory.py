"""Inventory health analysis tool."""
from contracts.tool_contract import ToolContract, ToolMetadata

def validate(data):
    if not isinstance(data.get("items"), list) or not data["items"]: raise ValueError("items must be a non-empty list")
    for item in data["items"]:
        if not isinstance(item, dict): raise ValueError("each item must be an object")
        for key in ("sku","stock","reorder_point"):
            if key not in item: raise ValueError(f"missing required field: {key}")
        if not isinstance(item["sku"], str) or not item["sku"].strip(): raise ValueError("sku must be non-empty")
        for key in ("stock","reorder_point"):
            if isinstance(item[key], bool) or not isinstance(item[key], (int,float)) or item[key] < 0: raise ValueError(f"{key} must be a non-negative number")

def execute(data):
    rows=[]
    for i in data["items"]:
        stock=float(i["stock"]); rp=float(i["reorder_point"])
        status="critical" if stock == 0 else "low" if stock <= rp else "healthy"
        rows.append({"sku":i["sku"],"stock":stock,"reorder_point":rp,"status":status,"shortfall":max(0.0,rp-stock)})
    counts={s:sum(r["status"]==s for r in rows) for s in ("critical","low","healthy")}
    return {"items":rows,"counts":counts}

tool=ToolContract(ToolMetadata("analyze-inventory","Classify inventory health from current stock and reorder points.",{"type":"object","required":["items"]}),validate,execute)
