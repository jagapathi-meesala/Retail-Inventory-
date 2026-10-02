from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_docs_exist_and_explainability_headings():
 for f in ["README.md","AGENTS.md","DUTIES.md","RULES.md","SOUL.md","EXPLAINABILITY.md"]: assert (ROOT/f).is_file()
 text=(ROOT/"EXPLAINABILITY.md").read_text()
 for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]: assert text.count(h)==1
 for bad in ["## Inputs\n","## Decision\n","## Limits\n"]: assert bad not in text
