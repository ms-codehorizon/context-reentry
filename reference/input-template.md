# Input: Evidence First, Memory Optional

Re-entry shouldn't lean on your memory - your memory is the thing that decayed. The
specialist takes two inputs; only the first is required.

## 1. The evidence pack (primary, required)

Three ways to produce it. The `interface/` page can **scan a GitHub repo** (GitHub
API) or **pick a local folder** (any modern browser) and auto-fill the pack for you. For the
deepest scan - the only one that sees uncommitted diffs and TODOs - run `gather.py`:

```
python3 /path/to/context-reentry/gather.py .  > evidence.md
# or point at any repo:
python3 gather.py ~/code/acme-portal
```

It collects, read-only (git + file reads, nothing written):

- time since your last commit, current branch
- working-tree state - uncommitted/untracked files (your unfinished thought)
- staged/unstaged diffstat - what's changed but not saved
- recent commits - what you were actually doing
- recent branches - threads you may have left mid-way
- most recently touched files
- TODO / FIXME / HACK left in the code

This is **ground truth** (tagged EVIDENCE). It needs no memory from you.

## 2. The brain-dump (optional, for the *why*)

The repo shows *what* you did, rarely *why*. Add a couple of lines only for intent and
for things outside the repo - who's waiting on you, a looming deadline, what a change
was in service of:

```
Why: the export endpoint is for the Acme demo next Wednesday.
Waiting: Dana owes nothing; I owe her a PR review.
Deadline: Acme demo Wed.
```

## How the two combine

- The specialist tags each fact EVIDENCE / RECALLED / INFERRED / UNKNOWN (rules.md 0b).
- When your memory contradicts the repo, it flags a **CONFLICT** and the repo wins
  (rules.md Section 1).
- No evidence pack at all? It runs memory-only and says so - lower confidence, and it
  can't do safety-first or reconciliation (rules.md 0c).
- Minimum viable input: the evidence pack alone. The brain-dump is pure upside.
