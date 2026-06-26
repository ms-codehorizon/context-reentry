# Output Template: The Re-Entry Map

The specialist fills this in. Goal: the user reads it in ~90 seconds and is working on
the *right* thing. Keep it scannable - recognition beats re-reading.

```
RE-ENTRY MAP: <Project>

[ Conflict - repo wins ]   (only if memory contradicts the repo; put it FIRST)
  You believed: <the memory>
  The repo shows: <the evidence>
  -> <corrected take>

PROJECT:          <name>
LAST ACTIVE:      <date of last commit>
RETURNING AFTER:  <gap, e.g. 14 days>

WHERE YOU WERE:
<1-3 sentences, grounded in the evidence - last commits, working tree.>

THE OPEN DECISION:
<the one decision or question left open.>

RESOLVED / NOT RESOLVED:
  [x] <done - committed/confirmed>
  [ ] <not resolved - still open / uncommitted>
  [?] <unknown - can't tell from the evidence>

FIRST ACTION ON RETURN:
<the single thing to do first, and the rule it won on.>

WATCH OUT FOR:
<loose files, stale memories, risks.>
```

## Rules the template enforces

- The conflict callout goes FIRST when present - catching a false memory is the
  highest-value thing the map does (rules.md Section 1).
- FIRST ACTION is exactly one thing, chosen by the rules and defensible (rules.md 3/4),
  never an arbitrary "do this first."
- WHERE YOU WERE is grounded in the evidence, not the brain-dump's memory.
- RESOLVED / NOT RESOLVED marks each loop done / not / unknown - never guess a status.
