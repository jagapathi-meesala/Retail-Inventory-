from adapters.tool_loader import ToolRegistry

def test_contract_metadata():
 t=ToolRegistry().get("analyze-inventory"); assert t.metadata.name and t.metadata.description and "required" in t.metadata.input_schema
