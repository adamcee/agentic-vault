# Documentation Site

Source for the Agentic Vault documentation site, built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/). Pushing to `main` publishes it to GitHub Pages through `.github/workflows/docs.yml`.

## Run It Locally

The first time, create a virtual environment and install the dependencies:

```bash
cd website
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After that, activate the environment and start the server:

```bash
cd website
source .venv/bin/activate
mkdocs serve
```

The site runs at `http://127.0.0.1:8000` and reloads when you save a file. Run `mkdocs build` to check for broken links before pushing; it writes to `site/`, which git ignores.

## Layout

- **`mkdocs.yml`**: site settings and navigation. Add new pages to `nav`.
- **`docs/`**: the pages.
- **`docs/examples`**: a symlink to the repo's `examples/` folder. Edit the example vaults there, not here.
- **`hooks/wikilinks.py`**: turns Obsidian `[[wikilinks]]` in the example vaults into working links.
