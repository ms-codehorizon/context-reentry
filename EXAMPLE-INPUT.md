# Example input - paste this to test the specialist in one shot

No repo handy? Copy everything in the box below into Claude (or any LLM) **after**
you've given it this folder's files. It's a real `gather.py` evidence pack from my
subscription-auditor repo plus the (wrong) memory I actually had - so you'll see the
specialist catch the conflict. The expected result is written up in
[`CASE-STUDY.md`](CASE-STUDY.md).

```
Act as the specialist defined in these files. Follow identity.md and apply rules.md
in order, citing rule numbers. Treat the EVIDENCE PACK as ground truth and the
brain-dump as memory to reconcile against it - the repo wins on any conflict.
Produce the re-entry map per reference/reentry-doc-template.md.

===== EVIDENCE PACK =====
# EVIDENCE PACK - subscription-auditor
- Current branch: main
- Last commit: 2026-06-10 (14 days ago)

## Working tree state
?? demo.gif

## Recent commits (last 12)
b1ea9a2  2026-06-10  minor update
5aab3a7  2026-06-10  python not needed anymore. remove
ecd2169  2026-06-10  remove unnecessary stuff
a1873a3  2026-06-10  security fixes
3b9b04b  2026-06-09  Initial commit: subscription auditor operator and Flask UI.

## Most recently touched files (last 15)
interface/index.html
main.py
pyproject.toml

===== BRAIN-DUMP (optional) =====
I think I still need to finish wiring the Flask backend - there's a main.py and
app.py for the server. Also a demo gif I wanted to add. Wanted to ship to GitHub Pages.
```

**What a correct run does:** flags a CONFLICT - your memory says "finish the Flask
backend," but commit `5aab3a7` deleted `main.py`/`pyproject.toml`; you moved to a
static, no-server design. It tells you **not** to rebuild the backend (the hour-saving
catch), then ranks the real loops: resolve the untracked `demo.gif`, confirm GitHub
Pages serves `interface/`.

To test with your own project instead, run `python3 gather.py /path/to/your/repo` and
paste that in place of the EVIDENCE PACK above.
