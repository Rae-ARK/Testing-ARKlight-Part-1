# Testing-ARKlight-Part-1

This is a trial of trying to make https://github.com/freeCodeCamp/news website using the capabilities
ARKlight provides. It's permissive MIT License is the reason for it being choosen to be a good candidate.

## Status

We are actively rebuilding the site on ARKlight, one page/component at a
time. The reference implementation lives in `Source/` (the original
eleventy/Ghost-based freeCodeCamp News codebase, kept as-is for
comparison). The migration plan, scope, and patch-by-patch sequencing
live in [`docs/migration.md`](docs/migration.md) -- start there.

## The ARKlight site (`ark/`)

- `ark/site.py` -- the `Site()` instance and ARKlight build entrypoint.
- `ark/components/layout.py` -- shared, reusable nav/header/footer and
  a `page_shell()` every page builds on.
- `ark/pages/` -- one module per route; each registers itself with
  `@site.page(...)` when imported.

Install ARKlight (see [`requirements.txt`](requirements.txt) for the
exact steps -- it's not on PyPI yet), then build:

```bash
arklight build ark/site.py -o ARK
```

This writes plain, dependency-free HTML/CSS/JS to `ARK/` -- no Python
in the output.