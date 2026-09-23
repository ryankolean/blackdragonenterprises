# tools

The HTML pages in this repo are generated. Edit the generator, not the HTML.

```bash
python3 tools/build_bde.py
```

- `build_bde.py` writes every page to the repo root.
- `contrast_lib.py` computes the WCAG contrast ratios shown on `specimen.html`.
- `testimonials_bde.py` holds the 17 testimonials, verbatim from the current site.
