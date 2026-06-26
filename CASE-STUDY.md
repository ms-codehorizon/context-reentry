# Case Study: re-entering a real repo after 14 days

This is a real run, not a mock-up. The target is my own `subscription-auditor` repo
(a previous build), untouched for two weeks. The evidence pack below is the actual
output of `gather.py`; the brain-dump is the memory I actually had walking back in -
which turned out to be wrong. The specialist caught it.

## Step 1 - collect the evidence (no memory needed)

```
$ python3 gather.py ../subscription-auditor
```

Real output (trimmed):

```
# EVIDENCE PACK - subscription-auditor
- Current branch: main
- Last commit: 2026-06-10 (14 days ago)

## Working tree state
?? demo.gif
  -> Uncommitted/untracked changes present - base is NOT clean. Section 2 likely applies.

## Recent commits (last 12)
b1ea9a2  2026-06-10  minor update
5aab3a7  2026-06-10  python not needed anymore. remove
ecd2169  2026-06-10  remove unnecessary stuff
9a101c7  2026-06-10  readme langunage update
a1873a3  2026-06-10  security fixes
...
3b9b04b  2026-06-09  Initial commit: subscription auditor operator and Flask UI.

## Most recently touched files (last 15)
interface/index.html
main.py
pyproject.toml
...
```

## Step 2 - my brain-dump (what I actually remembered)

> "Subscription auditor. Been a couple weeks. I think I still need to finish wiring the
> Flask backend - there's a `main.py` and an `app.py` for the server. Also I recall a
> demo gif I wanted to add. Wanted to ship it to GitHub Pages."

## Step 3 - what the specialist returned

> **⚠ CONFLICT (repo wins).** You believe the Flask backend (`main.py` / `app.py`)
> still needs finishing. The evidence says the opposite: commit `5aab3a7` -
> *"python not needed anymore. remove"* - **deleted** `main.py` and `pyproject.toml`,
> and `app.py` is not in the tree. The initial commit had a "Flask UI"; you since
> moved to a **static, no-server** design (`interface/index.html` is the live file).
> `main.py` shows in "recently touched" only because deleting it was the last thing
> that touched it. **Do not rebuild the backend - that hour would be wasted.**
>
> **PROJECT:** subscription-auditor  **LAST ACTIVE:** 2026-06-10  **RETURNING AFTER:** 14 days
>
> **WHERE YOU WERE (EVIDENCE):** finishing a cleanup + security pass and getting ready
> to ship to GitHub Pages; the last commits removed the Python server and tidied the repo.
>
> **THE OPEN DECISION:** nothing on the backend - that's settled. The only open question
> is whether the static site is actually shipped.
>
> **RESOLVED / NOT RESOLVED:**
> [x] Python backend removed (intentional, commit 5aab3a7)
> [x] security + cleanup pass committed
> [ ] `demo.gif` untracked, never committed
> [?] GitHub Pages deployment not confirmed live
>
> **FIRST ACTION ON RETURN - Sec 1:** drop the phantom backend task - you deleted it on
> purpose. Then commit or `.gitignore` `demo.gif` and confirm Pages serves `interface/`.
>
> **WATCH OUT FOR:** if your notes say "finish the backend," that memory is stale; the
> repo is the source of truth. `main.py` shows in "recently touched" only because it was
> deleted - not a signal to rebuild it.

## Why this is the point

A memory-only re-entry would have sent me to rebuild a Flask backend I had
*deliberately deleted* - the single most expensive way to waste a session. The repo
remembered correctly when I didn't. That's the difference between a note-taker and a
re-entry specialist: it reconstructs from evidence and reconciles my memory against it,
repo wins.
