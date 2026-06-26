# Rules: Re-Entry Logic

Build the re-entry map by running these sections IN ORDER. For the **FIRST ACTION ON
RETURN**, the first rule that fires decides - note the rule number next to it
(e.g. "FIRST ACTION - 3a"). The remaining open loops are listed under RESOLVED / NOT
RESOLVED.

## User preferences (overrides - edit these, they win ties)

| Setting | Value | Note |
|---|---|---|
| Re-entry energy default | normal | If the dump says "low energy / short session", momentum (3e) may be promoted to FIRST ACTION; otherwise importance wins |
| Definition of "blocking someone" | reply owed, review owed, or handoff owed | These count as 3a even with no explicit deadline |

## Section 0 Inputs, evidence precedence & tagging (apply before everything)

- 0a. Two possible inputs: the **EVIDENCE PACK** (from `gather.py` - the repo's real
      trail: commits, uncommitted work, branches, touched files, TODOs) and an
      optional **BRAIN-DUMP** (the user's memory). **Evidence is ground truth.** The
      dump's job is the *why* the repo can't show - intent, not facts.
- 0b. Tag every fact in the map as **EVIDENCE** (from the pack), **RECALLED**
      (from the dump), **INFERRED** (your deduction), or **UNKNOWN**. Never let a
      RECALLED or INFERRED claim wear an EVIDENCE label. A guess reading as a fact is
      the failure mode this whole tool exists to prevent.
- 0c. Memory-only fallback: if no evidence pack is given, proceed from the dump but
      say so plainly - confidence is lower, and Section 1 reconciliation and Section 2
      safety-first cannot run without the repo.
- 0d. Blank/missing field → **UNKNOWN**, never invented.

## Section 1 Reconcile memory against evidence (the differentiator)

Run this whenever both an evidence pack and a brain-dump are present.

- 1a. Test each claim in the dump against the evidence. When the repo contradicts the
      memory, emit a **CONFLICT** at the top of the map: state both sides, mark it
      CONFLICT, and **the repo wins** - correct the plan to reality. Re-entering on a
      false memory is exactly what costs the lost hour.
- 1b. Conflict patterns to check explicitly:
      • "I finished X" but X is uncommitted / not in any commit / tests red.
      • "I'm on branch Y" but Y doesn't exist or is stale.
      • "I removed / added Z" but the evidence shows the opposite.
      • "Almost done" but the diffstat shows a large unfinished change.
- 1c. Where memory and evidence agree, tag the fact EVIDENCE (the repo confirmed it).
      Where the dump supplies intent the repo can't (the *why*), keep it RECALLED.

## Section 2 Safety first (evidence-driven - check before ranking)

- 2a. If the evidence shows an UNSTABLE or UNKNOWN base - uncommitted/untracked
      changes, failing or unrun tests, a half-finished refactor/migration visible in
      the diffstat - the FIRST ACTION is ALWAYS **"establish known-good state"**
      (read the diff, run the tests, commit-or-stash) BEFORE any feature work. You
      cannot rank new work on a base you can't trust.
- 2b. Once the evidence shows a clean, committed, green base, skip to Section 3.

## Section 3 Rank the open loops (pick the FIRST ACTION)

Open loops come from BOTH sources: uncommitted files, stale branches, and TODO/FIXME
markers in the evidence, plus anything in the dump. Score each against these in order;
the first dimension that separates items decides their rank. The top item becomes the
FIRST ACTION (unless Section 2 fired); the rest populate RESOLVED / NOT RESOLVED.

- 3a. **You are the bottleneck.** A reply/review/handoff someone else (or another
      project) is waiting on. Highest: external clock plus you're holding others up.
- 3b. **Hard clock.** A deadline or scheduled commitment for THIS project within 48h.
- 3c. **Critical path.** Unblocks the most of your own remaining work - count the
      downstream loops it frees. More unblocked = higher.
- 3d. **Pending decision.** An unresolved decision that makes other work speculative
      until it's made. This is what fills THE OPEN DECISION; resolve before building on a guess.
- 3e. **Momentum (tiebreak / low-energy promote).** The thing you were mid-keystroke
      on - lowest re-entry cost, usually the most recent uncommitted file. Wins ties;
      only becomes FIRST ACTION if nothing in 3a-3d fired, or the user flagged low energy.

## Section 4 The FIRST ACTION ON RETURN (anti-arbitrary requirement)

- 4a. Exactly ONE action is the FIRST ACTION. It carries one sentence stating the rule
      it won on and what it beat (e.g. "FIRST ACTION - 3a: Dana is blocked on this
      review; the API refactor (3c) frees more work but has no one waiting").
- 4b. If the energy override (short / low-energy session) changed the pick, say so in
      WATCH OUT FOR, so the user knows importance was deliberately set aside this once.

## Section 5 STOP gates (the only times you ask)

Otherwise: decide, don't ask. STOP and ask exactly one question only when:

- 5a. Two items tie on 3a/3b with real, competing external clocks and neither the
      evidence nor the dump gives a way to rank whose deadline matters more.
- 5b. There is no evidence pack AND the dump is too thin to reconstruct any state -
      ask for the single most useful thing: "Point me at the repo, or tell me the last
      thing you actually did."

## Tie-breaker

If two outcomes remain defensible after all sections: a CONFLICT to resolve beats new
work (reality first); an item with an **external party waiting** beats a solo item; a
**known clock** beats an open-ended task; and only then does **momentum** decide.
Importance owns the FIRST ACTION; momentum is the backup - never flip them silently.
