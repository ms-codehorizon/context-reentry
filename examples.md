# Examples: Re-Entry in Action

Each example shows the inputs (evidence pack ± brain-dump) and the **re-entry map** the
specialist returns. The FIRST ACTION always cites the rule it won on. For a full worked
run on a real repo, see [`CASE-STUDY.md`](CASE-STUDY.md).

## Example 1 - the teammate is the bottleneck (rule 3a)

**Evidence (GitHub scan), `acme-portal`:** last commit 3 days ago "wip: invoice export"
on `feature/invoice-export`; clean tree; open PR #18 by `@dana`, review requested from you.
**Brain-dump:** "I was deep in the export endpoint and want to finish it."

**Re-entry map (abridged):**
- **WHERE YOU WERE (EVIDENCE):** mid-build on the invoice export endpoint; the CSV
  download button is still a TODO waiting on it.
- **THE OPEN DECISION:** finish the export now, or clear the review you owe Dana first.
- **RESOLVED / NOT RESOLVED:** [ ] export endpoint in progress · [ ] CSV button blocked
  on it · [ ] Dana's PR #18 review owed.
- **FIRST ACTION - 3a:** review Dana's PR #18. She's blocked on you; it beats finishing
  the export (3c), which frees more of your own work but has nobody waiting.
- **WATCH OUT FOR:** `export.py` is your most recent uncommitted file and the easy resume,
  but importance beats momentum here - do the review first.

## Example 2 - safety first, straight from the evidence (Section 2)

**Evidence (gather.py), `api-gateway`:** last touched ~2 weeks ago; working tree shows
6 uncommitted files mid-refactor across `api/`; diffstat large and lopsided.
**Brain-dump:** none.

**Re-entry map (abridged):**
- **WHERE YOU WERE (EVIDENCE):** a large, unfinished API-layer refactor sits uncommitted.
- **THE OPEN DECISION:** UNKNOWN - no dump; the repo can't say whether to finish or revert.
- **RESOLVED / NOT RESOLVED:** [ ] API refactor uncommitted and incomplete.
- **FIRST ACTION - 2a:** establish known-good state - read the diff, run the suite,
  decide commit-or-stash. No feature can be ranked on top of a base this unstable.
- **WATCH OUT FOR:** the plan is grounded in the diff, not a memory of where you think
  you were - confirm the test state before trusting anything.

## Example 3 - the conflict catch (Section 1, the differentiator)

**Evidence (gather.py), `subscription-auditor`:** recent commit "python not needed
anymore. remove"; no `app.py` in the tree; clean working tree.
**Brain-dump:** "I still need to finish wiring the Flask backend in app.py."

**Re-entry map (abridged):**
- **⚠ CONFLICT (repo wins):** you believe the Flask backend in `app.py` is unfinished.
  The repo shows you *deleted* the Python backend ("python not needed anymore. remove")
  and `app.py` is gone - you already moved to a no-server design. Do not re-open it.
- **WHERE YOU WERE (EVIDENCE):** clean tree; last work was removing the server layer.
- **THE OPEN DECISION:** none on the backend - that's settled. What's left is shipping.
- **RESOLVED / NOT RESOLVED:** [x] Python backend removed (intentional) · [?] deploy not confirmed.
- **FIRST ACTION - Sec 1:** drop the phantom backend task; the server is gone on purpose.
  Then proceed to the real open loops, not the one your memory invented.
- **WATCH OUT FOR:** deleted files can resurface in "recently touched" - that is not a
  signal to rebuild them.

## Example 4 - no evidence, thin memory, honest stop (Section 5b)

**Evidence:** none (no repo path given).
**Brain-dump:** "Project Zephyr. Haven't looked in a while. Something about onboarding?"

**Re-entry map (abridged):**
- **WHERE YOU WERE:** UNKNOWN - no evidence pack, and the dump names no concrete action.
- **STOP - 5b (one question):** "Point me at the Zephyr repo (`python3 gather.py path`),
  or tell me the last thing you actually did - a file, a commit, a message."
- The specialist did NOT invent an onboarding plan. With no evidence and no real memory,
  a confident guess is exactly the failure this tool exists to prevent.
