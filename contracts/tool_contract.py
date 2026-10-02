"""Framework-independent tool contract."""
from dataclasses import dataclass
from typing import Any, Callable, Mapping

@dataclass(frozen=True)
class ToolError:
    code: str
    message: str

@dataclass(frozen=True)
class ToolResult:
    ok: bool
    data: Any = None
    error: ToolError | None = None

@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: Mapping[str, Any]

class ToolContract:
    metadata: ToolMetadata
    validator: Callable[[Mapping[str, Any]], None]
    executor: Callable[[Mapping[str, Any]], Any]

    def __init__(self, metadata: ToolMetadata, validator, executor):
        self.metadata = metadata
        self.validator = validator
        self.executor = executor

    def validate(self, inputs: Mapping[str, Any]) -> None:
        if not isinstance(inputs, Mapping):
            raise ValueError("inputs must be an object")
        self.validator(inputs)

    def execute(self, inputs: Mapping[str, Any]) -> ToolResult:
        try:
            self.validate(inputs)
            return ToolResult(ok=True, data=self.executor(inputs))
        except (ValueError, TypeError, KeyError) as exc:
            return ToolResult(ok=False, error=ToolError("INVALID_INPUT", str(exc)))
        except Exception as exc:
            return ToolResult(ok=False, error=ToolError("TOOL_FAILURE", str(exc)))
