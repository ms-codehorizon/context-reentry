#!/usr/bin/env python3
"""
gather.py - the evidence collector for the Context Re-Entry Specialist.

Re-entry shouldn't depend on your memory. This reads the trail you already left
behind in a repo - commits, uncommitted work, branches, recently touched files,
stale TODOs - and prints an EVIDENCE PACK. Feed that (optionally plus a 2-minute
brain-dump) to the specialist; the rules treat this output as ground truth and
your memory as a hypothesis to reconcile against it.

Zero dependencies. Python 3.8+. Read-only: runs only `git` plus file reads.

Usage:
    python3 gather.py [path-to-repo]        # defaults to current directory
    python3 gather.py ~/code/acme-portal > evidence.md
"""

import subprocess, sys, os, time
from datetime import datetime, timezone

MAX_COMMITS   = 20
MAX_BRANCHES  = 8
MAX_FILES     = 15
MAX_TODOS     = 20
DIFF_STAT_CAP = 40   # lines of diffstat to show


def run(args, cwd):
    """Run a command, return (stdout, ok). Never raises."""
    try:
        p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=20)
        return p.stdout.strip(), p.returncode == 0
    except Exception as e:
        return f"(could not run {' '.join(args)}: {e})", False


def is_git(repo):
    out, ok = run(["git", "rev-parse", "--is-inside-work-tree"], repo)
    return ok and out.strip() == "true"


def section(title):
    return f"\n## {title}\n"


def gather(repo):
    repo = os.path.abspath(os.path.expanduser(repo))
    name = os.path.basename(repo.rstrip("/")) or repo
    out = []
    out.append(f"# EVIDENCE PACK - {name}")
    out.append(f"_collected {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M %Z')} "
               f"by gather.py - this is the repo's trail, treat it as ground truth (EVIDENCE)._")
    out.append(f"\n- **Path:** `{repo}`")

    if not os.path.isdir(repo):
        out.append(f"\n> Path does not exist. Nothing to reconstruct.")
        return "\n".join(out)

    if not is_git(repo):
        out.append("\n> Not a git repo. Falling back to filesystem signals only.\n")
        out.append(section("Recently modified files (by mtime)"))
        out.append(recent_files_fs(repo))
        return "\n".join(out)

    # branch + how long since you last committed
    branch, _ = run(["git", "rev-parse", "--abbrev-ref", "HEAD"], repo)
    last_iso, ok = run(["git", "log", "-1", "--format=%cI"], repo)
    out.append(f"- **Current branch:** `{branch}`")
    if ok and last_iso:
        try:
            dt = datetime.fromisoformat(last_iso)
            days = (datetime.now(timezone.utc) - dt.astimezone(timezone.utc)).days
            out.append(f"- **Last commit:** {last_iso.split('T')[0]} "
                       f"({days} day{'s' if days != 1 else ''} ago)")
        except Exception:
            out.append(f"- **Last commit:** {last_iso}")

    # working tree state - the highest-signal part for safety-first
    out.append(section("Working tree state (uncommitted = your unfinished thought)"))
    porcelain, _ = run(["git", "status", "--porcelain"], repo)
    if porcelain:
        out.append("```\n" + porcelain + "\n```")
        out.append("_Uncommitted/untracked changes present - the base is NOT clean. "
                   "Section 2 (safety-first) likely applies._")
    else:
        out.append("_Clean working tree - everything is committed._")

    # staged vs unstaged diffstat
    unstaged, _ = run(["git", "diff", "--stat"], repo)
    staged, _   = run(["git", "diff", "--cached", "--stat"], repo)
    if unstaged or staged:
        out.append(section("What's changed but not committed (diffstat)"))
        if staged:
            out.append("**Staged:**\n```\n" + cap(staged) + "\n```")
        if unstaged:
            out.append("**Unstaged:**\n```\n" + cap(unstaged) + "\n```")

    # recent commits - what you were actually doing
    out.append(section(f"Recent commits (last {MAX_COMMITS})"))
    commits, _ = run(["git", "log", f"-{MAX_COMMITS}",
                      "--pretty=format:%h  %cd  %s", "--date=short"], repo)
    out.append("```\n" + (commits or "(no commits)") + "\n```")

    # other branches you may have left mid-thought
    out.append(section(f"Recent branches (last {MAX_BRANCHES} by activity)"))
    branches, _ = run(["git", "for-each-ref", "--sort=-committerdate", "refs/heads",
                       f"--count={MAX_BRANCHES}",
                       "--format=%(refname:short)  |  %(committerdate:relative)  |  %(contents:subject)"],
                      repo)
    out.append("```\n" + (branches or "(none)") + "\n```")

    # files you touched most recently (tracked)
    out.append(section(f"Most recently touched files (last {MAX_FILES})"))
    out.append(recent_files_git(repo))

    # stale intent you left in the code
    todos = grep_todos(repo)
    if todos:
        out.append(section(f"TODO / FIXME / HACK left in tracked files (max {MAX_TODOS})"))
        out.append("```\n" + todos + "\n```")

    out.append("\n---\n_End of evidence pack. Hand this to the specialist; add a "
               "brain-dump only for intent the repo can't show (the *why*)._")
    return "\n".join(out)


def cap(text, n=DIFF_STAT_CAP):
    lines = text.splitlines()
    if len(lines) <= n:
        return text
    return "\n".join(lines[:n] + [f"... (+{len(lines)-n} more)"])


def recent_files_git(repo):
    out, ok = run(["git", "log", "--name-only", "--pretty=format:", "-n", "40"], repo)
    if not ok or not out:
        return recent_files_fs(repo)
    seen, ordered = set(), []
    for line in out.splitlines():
        f = line.strip()
        if f and f not in seen:
            seen.add(f); ordered.append(f)
        if len(ordered) >= MAX_FILES:
            break
    return "```\n" + ("\n".join(ordered) or "(none)") + "\n```"


def recent_files_fs(repo):
    items = []
    for root, dirs, files in os.walk(repo):
        dirs[:] = [d for d in dirs if d not in
                   (".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build")]
        for f in files:
            if f.startswith("."):
                continue
            p = os.path.join(root, f)
            try:
                items.append((os.path.getmtime(p), os.path.relpath(p, repo)))
            except OSError:
                pass
    items.sort(reverse=True)
    rows = [f"{datetime.fromtimestamp(m).strftime('%Y-%m-%d %H:%M')}  {rel}"
            for m, rel in items[:MAX_FILES]]
    return "```\n" + ("\n".join(rows) or "(none)") + "\n```"


def grep_todos(repo):
    out, ok = run(["git", "grep", "-n", "-E", r"TODO|FIXME|HACK|XXX"], repo)
    if not ok or not out:
        return ""
    lines = out.splitlines()[:MAX_TODOS]
    return "\n".join(lines)


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(gather(target))
