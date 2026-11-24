# Brutally honest, funny error message about what actually broke (final v2).
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_TEXT = "Error: the database is fine, the code is fine, the intern deployed the wrong branch on a Friday and then went home for the weekend."

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(ENTRY_TEXT)
