"""Static readiness audit for required Agent Passport artifacts."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
required=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
dirs=["adapters","config","contracts","core","skills","tools","tests","verification"]
errors=[]
for f in required:
 p=ROOT/f
 if not p.is_file() or not p.read_text().strip(): errors.append(f"missing/empty: {f}")
for d in dirs:
 if not (ROOT/d).is_dir(): errors.append(f"missing directory: {d}")
text=(ROOT/"EXPLAINABILITY.md").read_text() if (ROOT/"EXPLAINABILITY.md").is_file() else ""
for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]:
 if text.count(h)!=1: errors.append(f"required heading count != 1: {h}")
 section_pattern=re.escape(h)+r"(.*?)(?=^## |\Z)"
 m=re.search(section_pattern,text,re.S|re.M)
 if not m or len(re.findall(r"(?<=[.!?])\s+",m.group(1).strip()))<2: errors.append(f"section lacks two sentences: {h}")
for bad in ["## Inputs\n","## Decision\n","## Limits\n"]:
 if bad in text: errors.append(f"conflicting heading: {bad.strip()}")
if errors:
 print("READINESS AUDIT: FAIL")
 print("\n".join("- "+e for e in errors)); sys.exit(1)
print("READINESS AUDIT: PASS")
