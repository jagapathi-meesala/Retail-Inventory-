from adapters.tool_loader import ToolRegistry
import pytest

def test_unknown_tool():
 r=ToolRegistry()
 with pytest.raises(KeyError): r.get("missing-tool")
