#!/usr/bin/env python3
"""Copy the template's shared vault files into the example vault repos.

The example vaults (night-post-vault, curbside-cycles-vault) live in their own
repos and carry copies of the template's protocol pages and skills. This script
keeps those copies in step with template/:

- vault-guide/       every page, with each example's own date and title kept
- .claude/skills/    copied as is; files removed from the template are removed
- pointer files      CLAUDE.md, GEMINI.md, .cursorrules, .windsurfrules, copied as is

Usage:
    scripts/sync-examples.py                 sync ../night-post-vault and ../curbside-cycles-vault
    scripts/sync-examples.py PATH [PATH...]  sync the given example vaults
    scripts/sync-examples.py --check         report drift without writing; exit 1 if any

Run it from anywhere. After syncing, review and commit in each example repo.
"""

import filecmp
import re
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMPLATE = REPO / "template"
DEFAULT_EXAMPLES = [REPO.parent / "night-post-vault", REPO.parent / "curbside-cycles-vault"]


def vault_start_date(vault):
    """The vault's creation date: the first ## YYYY-MM-DD heading in session-history.md."""
    history = (vault / "session-history.md").read_text(encoding="utf-8")
    m = re.search(r"^## (\d{4}-\d{2}-\d{2})", history, re.M)
    return m.group(1) if m else None


def adapt_page(text, date, existing):
    """Fill the template page's placeholder date and keep the example's title line."""
    if date:
        text = re.sub(r"^date: YYYY-MM-DD$", f"date: {date}", text, count=1, flags=re.M)
    title = None
    if existing:
        m = re.search(r"\A---\n(?:.*\n)*?(title: .*)\n", existing)
        title = m.group(1) if m else None
    if title and text.startswith("---\n") and not re.search(r"\A---\n(?:.*\n)*?title: ", text):
        text = "---\n" + title + "\n" + text[4:]
    return text


def sync_guide(vault, check):
    changes = []
    date = vault_start_date(vault)
    src_root, dst_root = TEMPLATE / "vault-guide", vault / "vault-guide"
    for src in sorted(src_root.rglob("*.md")):
        dst = dst_root / src.relative_to(src_root)
        existing = dst.read_text(encoding="utf-8") if dst.exists() else None
        new = adapt_page(src.read_text(encoding="utf-8"), date, existing)
        if new != existing:
            changes.append(dst)
            if not check:
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(new, encoding="utf-8")
    for dst in sorted(dst_root.rglob("*.md")):
        if not (src_root / dst.relative_to(dst_root)).exists():
            changes.append(dst)
            if not check:
                dst.unlink()
    return changes


def sync_skills(vault, check):
    changes = []
    src_root, dst_root = TEMPLATE / ".claude" / "skills", vault / ".claude" / "skills"
    for src in sorted(p for p in src_root.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        dst = dst_root / src.relative_to(src_root)
        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            changes.append(dst)
            if not check:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
    for dst in sorted(p for p in dst_root.rglob("*") if p.is_file() and "__pycache__" not in p.parts):
        if not (src_root / dst.relative_to(dst_root)).exists():
            changes.append(dst)
            if not check:
                dst.unlink()
    return changes


POINTERS = ["CLAUDE.md", "GEMINI.md", ".cursorrules", ".windsurfrules"]


def sync_pointers(vault, check):
    changes = []
    for name in POINTERS:
        src, dst = TEMPLATE / name, vault / name
        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            changes.append(dst)
            if not check:
                shutil.copy2(src, dst)
    return changes


def main(argv):
    check = "--check" in argv
    paths = [Path(a).resolve() for a in argv if not a.startswith("--")] or DEFAULT_EXAMPLES
    drift = False
    for vault in paths:
        if not (vault / "AGENTS.md").exists():
            print(f"skip {vault}: no AGENTS.md")
            continue
        changes = sync_guide(vault, check) + sync_skills(vault, check) + sync_pointers(vault, check)
        verb = "would change" if check else "changed"
        print(f"{vault.name}: {len(changes)} file(s) {verb}")
        for c in changes:
            print(f"  {c.relative_to(vault)}")
        drift = drift or bool(changes)
    return 1 if check and drift else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
