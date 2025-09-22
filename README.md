# Galaxy‑SynBioCAD • Tutorials (skeleton)

## Getting Started

1. Install locally:

   ```bash
   pip install mkdocs-material
   mkdocs serve
   ```

2. Open <http://127.0.0.1:8000> to preview.
3. Push to GitHub; the workflow will publish to `gh-pages`.

## GitHub Pages Deployment

- The workflow `.github/workflows/deploy.yml` builds the site and publishes `./site` to `gh-pages`.
- In **Settings → Pages**, choose *Deploy from a branch* then `gh-pages` branch (`/` folder).

## Customization

- Edit `mkdocs.yml` (title, navigation, palette).
- Add a logo in `docs/assets/` and reference it in `mkdocs.yml`:

  ```yaml
  theme:
    logo: assets/logo.svg
    favicon: assets/favicon.ico
  ```