"""Resolve Obsidian wikilinks in example vaults.

Example vaults use vault-root-relative wikilinks ([[decisions/product/PDR-P001]]).
Each example lives at docs/examples/<name>/, so a link resolves against that
example's root, then by filename within it. Code spans and fences are skipped.
Unresolved links render as plain text.
"""

import posixpath
import re

WIKILINK = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]+))?\]\]")
CODE = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)


def _vault_root(src_path):
    parts = src_path.split("/")
    if len(parts) > 2 and parts[0] == "examples":
        return "/".join(parts[:2])
    return None


def _index(files, root):
    by_path, by_name = {}, {}
    for f in files:
        if f.src_uri.startswith(root + "/") and f.src_uri.endswith(".md"):
            rel = f.src_uri[len(root) + 1 : -3]
            by_path[rel] = f.src_uri
            by_name.setdefault(posixpath.basename(rel), f.src_uri)
    return by_path, by_name


def on_page_markdown(markdown, page, config, files):
    root = _vault_root(page.file.src_uri)
    if root is None:
        return markdown
    by_path, by_name = _index(files, root)
    here = posixpath.dirname(page.file.src_uri)

    def link(m):
        target = m.group(1).strip().removesuffix(".md")
        label = m.group(3) or m.group(1).strip()
        dest = by_path.get(target) or by_name.get(posixpath.basename(target))
        if dest is None:
            return label
        return f"[{label}]({posixpath.relpath(dest, here)}{m.group(2) or ''})"

    pieces = CODE.split(markdown)
    for i in range(0, len(pieces), 2):
        pieces[i] = WIKILINK.sub(link, pieces[i])
    return "".join(pieces)
