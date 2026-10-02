"""Dynamic discovery of Python tool modules."""
import importlib.util
from pathlib import Path
from contracts.tool_contract import ToolContract

class ToolRegistry:
    def __init__(self, tools_dir=None):
        self.tools_dir=Path(tools_dir or Path(__file__).resolve().parents[1]/"tools")
        self._tools={}
        self.discover()
    def discover(self):
        for path in self.tools_dir.glob("*.py"):
            if path.name.startswith("__"): continue
            spec=importlib.util.spec_from_file_location(path.stem.replace("-","_"),path)
            if spec is None or spec.loader is None: continue
            module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
            tool=getattr(module,"tool",None)
            if isinstance(tool,ToolContract): self._tools[tool.metadata.name]=tool
        return self
    def names(self): return sorted(self._tools)
    def get(self,name):
        if name not in self._tools: raise KeyError(f"Unknown tool: {name}")
        return self._tools[name]
    def execute(self,name,inputs): return self.get(name).execute(inputs)
