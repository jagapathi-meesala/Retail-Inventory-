from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_manifest_static_opengap_010_shape():
    data = yaml.safe_load((ROOT / "agent.yaml").read_text())

    allowed = {
        "spec_version", "name", "version", "description", "author", "license",
        "model", "extends", "dependencies", "skills", "tools", "agents",
        "delegation", "runtime", "a2a", "compliance", "registries", "tags",
        "mcp_servers", "metadata"
    }

    assert set(data) <= allowed
    assert data["spec_version"] == "0.1.0"
    assert re.fullmatch(r"^[a-z][a-z0-9-]*$", data["name"])
    assert re.fullmatch(
        r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$",
        str(data["version"])
    )
    assert isinstance(data["description"], str) and data["description"]

    for key in ("skills", "tools"):
        assert isinstance(data[key], list)
        assert len(data[key]) == len(set(data[key]))
        assert all(
            re.fullmatch(r"^[a-z][a-z0-9-]*$", x)
            for x in data[key]
        )

    skill_dirs = {
        p.name
        for p in ROOT.joinpath("skills").iterdir()
        if p.is_dir() and (p / "SKILL.md").is_file()
    }

    assert set(data["skills"]) == skill_dirs

    tool_files = {
        p.stem
        for p in ROOT.joinpath("tools").glob("*.py")
        if not p.name.startswith("__")
    }

    assert set(data["tools"]) == tool_files
