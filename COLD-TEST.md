# Cold Test: a fresh model, three unseen scenarios

The real test of a folder-based specialist is whether a fresh model, handed only these
files and inputs it has never seen, makes the calls I would make. These three scenarios
are NOT in `examples.md` or `CASE-STUDY.md` - they were run cold, applying only
`identity.md` + `rules.md`.

Each lists the inputs, the call the folder produced (with the rule that fired), and
the call I would make. All three matched.

---

## Scenario 1 - the teammate is the bottleneck (rule 3a)

**Evidence (GitHub scan), repo `billing-service`:** last commit 3 days ago
"wip: proration calc" on `feature/proration`; clean working tree; open PR #42
"fix invoice rounding" by `@maria`, review requested from **you**.
**Brain-dump:** "I was deep in the proration math and want to finish it."

**Folder's call:** Section 1 - no conflict (memory matches the wip commit).
Section 2 - base is committed, skip. Section 3 - **3a fires:** you owe Maria a review;
she is blocked on you. **FIRST ACTION - 3a:** review Maria's PR #42. It beats finishing
the proration math (3c), which frees your own work but has nobody waiting on it.

**My call:** review Maria's PR first. **Match.** The folder didn't chase the thing I
was emotionally "deep in"; it chased the person I was blocking.

---

## Scenario 2 - memory says done, the repo says otherwise (Section 1 + 2a)

**Evidence (gather.py), repo `etl-pipeline`:** working tree has 7 uncommitted files
under `migrations/`; last commit "start schema v2 migration"; test suite shows
failures.
**Brain-dump:** "Pretty sure I finished the schema migration and it was passing."

**Folder's call:** Section 1 - **CONFLICT (repo wins):** you believe the migration is
finished and green, but the evidence shows 7 uncommitted migration files and a red
suite. Section 2 - **FIRST ACTION - 2a:** establish known-good state (read the diff, run
the suite, decide commit-or-stash) before any new work. Do not build on "it's done."

**My call:** stop, verify the migration state, get to green first. **Match.** This is
the exact false-memory trap that wastes a session, and the folder caught it.

---

## Scenario 3 - nothing urgent, low energy (rule 3e + energy override)

**Evidence (local folder scan), repo `portfolio-site`:** clean and committed; last
commit "tweak hero copy" yesterday; most recently edited `about.tsx`; no open PRs, no
deadlines.
**Brain-dump:** "Short session, low energy tonight. Was poking at the About page."

**Folder's call:** Section 1 - no conflict. Section 2 - clean. Section 3 - 3a/3b/3c/3d
do not fire (nobody waiting, no clock, nothing large to unblock). Energy override
promotes momentum: **FIRST ACTION - 3e:** resume the About page (`about.tsx`), the
lowest-friction restart for a short session.

**My call:** just pick the About page back up. **Match.** No invented urgency, no
guilt-tripping me into a big task I don't have the energy for tonight.

---

## What this demonstrates

Three inputs the model had never seen, three different rules firing (3a bottleneck,
Section 1 conflict + 2a safety, 3e momentum), and three calls that match mine - with
the rule cited each time. Swap in your own `rules.md` thresholds and the same machinery
applies your judgment instead of mine.

> Reproduce it yourself: drop this folder into a fresh chat, paste any scenario's
> evidence + brain-dump, and check the call against the one written here.
