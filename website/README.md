# Documentation Site

Source for the Agentic Vault documentation site, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Pushing to `main` publishes it to GitHub Pages through `.github/workflows/docs.yml`.

## Run It Locally

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
cd website
uv run mkdocs serve
```

The first run sets up Python 3.13 and the pinned dependencies into `website/.venv`. The site runs at `http://127.0.0.1:8000` and reloads when you save a file.

Run `uv run mkdocs build` to check for broken links before pushing. It writes to `site/`, which git ignores.

To preview the interactive Night Post vault, run `website/quartz/build.sh --serve` from the repo root (needs Node 22 or later). It downloads Quartz into `website/quartz/.quartz/` on first run and serves at `http://localhost:8080`.

To add or upgrade a dependency, run `uv add <package>` and commit the updated `pyproject.toml` and `uv.lock`.

## Layout

- **`mkdocs.yml`**: site settings and navigation. Add new pages to `nav`.
- **`pyproject.toml`** and **`uv.lock`**: Python dependencies, pinned.
- **`docs/`**: the pages.
- **`docs/examples`**: a symlink to the repo's `examples/` folder. Edit the example vaults there, not here.
- **`hooks/wikilinks.py`**: turns Obsidian `[[wikilinks]]` in the example vaults into working links.
- **`quartz/`**: config and build script for the interactive Night Post site, published at `/night-post/` next to the docs.
