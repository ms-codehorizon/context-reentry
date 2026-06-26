# Reference: Output Schema (JSON)

The canonical machine-readable contract for the re-entry map. The interface's live
mode asks the model to emit exactly this JSON, then renders it. The human-readable
shape lives in `reentry-doc-template.md`; this is the same map, typed.

Emit raw JSON only - no markdown fences, no prose around it.

```json
{
  "project": "string - the repo / project name",
  "last_active": "string - date of the last commit, e.g. '2026-06-10'",
  "returning_after": "string - rough gap, e.g. '14 days'",
  "conflict": {
    "believed": "string - what the user's memory claimed",
    "evidence": "string - what the repo actually shows",
    "resolution": "string - repo wins; the corrected take"
  },
  "where_you_were": "string - 1-3 sentences, grounded in the evidence (last commits, working tree)",
  "open_decision": "string - the one decision or question left open",
  "resolved": [
    { "status": "done | not | unknown", "text": "string - one line" }
  ],
  "first_action": "string - the single rule-chosen thing to do first, and why",
  "watch_out_for": "string - loose files, stale memories, risks",
  "stop": null
}
```

`conflict` is `null` when memory and repo agree (or there's no brain-dump to reconcile).
Set it whenever Section 1 finds a contradiction - it renders first, as a callout.

## The STOP case (rules.md Section 5)

When the rules hit a STOP gate (two competing clocks that can't be ranked, or no
evidence and a dump too thin), set `stop` and keep the rest best-effort:

```json
"stop": {
  "rule": "5a | 5b",
  "question": "string - the single question to ask the user",
  "resolution": "string - what happens once they answer"
}
```

## Section mapping (so the methodology stays intact)

- `where_you_were` and `open_decision` come from Section 1 reconstruction (EVIDENCE first).
- `resolved` is the open-loops list with a status each: `done` (committed/confirmed),
  `not` (still open / uncommitted), `unknown` (can't tell from evidence).
- `first_action` is the rule-chosen action from rules.md Section 3/4 - cite the rule it won on.
- `conflict` is the Section 1 catch; `watch_out_for` carries safety (Section 2) notes and risks.
- All values are HTML-escaped before rendering (the page trusts none of this text).
