"""One-Line Office Jokes entry: writes a single office-life joke to entry.txt."""
import os

ENTRY = "I blocked an hour for focus time, so the team booked a meeting to discuss why I was unavailable."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)  # no trailing newline: the gate counts every character
