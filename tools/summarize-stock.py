"""Aggregate stock summary tool."""
from contracts.tool_contract import ToolContract, ToolMetadata

def validate(data):
    if not isinstance(data.get("items"), list) or not data["items"]: raise ValueError("items must be a non-empty list")
    for i in data["items"]:
        if not isinstance(i,dict): raise ValueError("each item must be an object")
        if "sku" not in i or "stock" not in i: raise ValueError("each item requires sku and stock")
        if not isinstance(i["sku"],str) or not i["sku"].strip(): raise ValueError("sku must be non-empty")
        if isinstance(i["stock"],bool) or not isinstance(i["stock"],(int,float)) or i["stock"]<0: raise ValueError("stock must be non-negative")

def execute(data):
    stocks=[float(i["stock"]) for i in data["items"]]
    return {"sku_count":len(stocks),"total_units":sum(stocks),"average_units":sum(stocks)/len(stocks),"zero_stock_skus":[i["sku"] for i in data["items"] if float(i["stock"])==0]}

tool=ToolContract(ToolMetadata("summarize-stock","Produce aggregate stock metrics for a supplied SKU list.",{"type":"object","required":["items"]}),validate,execute)
