# Reference: Priority Rubric

The detail behind `rules.md` Section 3. The specialist ranks open loops by applying
these dimensions IN ORDER; the first that separates two items decides their order.
This exists so the FIRST ACTION pick is defensible, never a coin flip.

Open loops are sourced from the evidence first (uncommitted files, stale branches,
TODO/FIXME markers, the last commit's unfinished work) and from the brain-dump second
(people waiting, deadlines, intent).

| Rank | Dimension | Why it sits here | Rule |
|---|---|---|---|
| - | Resolve a CONFLICT (memory vs repo) | Acting on a false memory is the costly failure; reality must be set straight before anything | Sec 1 |
| - | Safety: establish known-good state | An unstable base (uncommitted, red/unrun tests) can't carry new work | Sec 2 |
| 1 | You are the bottleneck (reply/review/handoff owed) | External party stalled + a social clock; your delay multiplies onto others | 3a |
| 2 | Hard clock within 48h (deadline, demo, cutover) | Immovable external time pressure on this project | 3b |
| 3 | Critical path (unblocks the most of your own work) | Frees the largest amount of downstream work per unit effort | 3c |
| 4 | Pending decision | Until made, dependent work is speculative and may be thrown away | 3d |
| 5 | Momentum (mid-keystroke, lowest re-entry cost) | Cheapest to resume; usually the most recent uncommitted file | 3e |

The two em-dashed rows sit ABOVE the numbered table: a CONFLICT is corrected first
(rules.md Section 1), then safety (Section 2), then the ranked actions.

## How ties resolve

1. A CONFLICT to resolve beats new work (reality first).
2. External party waiting beats a solo task.
3. A known clock beats an open-ended task.
4. Only then does momentum (3e) decide.

If two items still tie on a real external clock (3a/3b) with no way to rank them from
the evidence or the dump, the specialist STOPS and asks one question (rules.md 5a)
rather than guessing whose deadline matters more.

## Energy override

If the brain-dump flags a short or low-energy session, momentum (3e) may be promoted
into the FIRST ACTION slot - a finished small task beats a stalled important one when the
alternative is not restarting at all. The doc states when this override fired.
