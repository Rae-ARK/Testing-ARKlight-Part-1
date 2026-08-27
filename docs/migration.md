# Migration Plan: freeCodeCamp News -> ARKlight

## Goal

Rebuild the public-facing freeCodeCamp News site (currently `Source/`, an
11ty + Ghost JAMstack app) as an ARKlight site: authored in Python,
compiled to plain dependency-free HTML/CSS/JS. We are doing this
incrementally, patch by patch, against this repo -- not a rewrite in one
shot.

This is a trial run for ARKlight itself as much as it is a website
migration: it exercises the compiler against a real, non-trivial content
site (articles, listings, tags/authors, i18n) rather than a toy demo.

## Why this repo

- Permissive MIT license (see repo README) -- safe to use as a source
  reference and to publish a derivative build from.
- Real, content-heavy structure: article pages, listing/index pages,
  author and tag pages, RSS, multiple locales -- a good stress test for
  ARKlight's `Site`/`Page`/backend model rather than a single static
  page.
- Existing build is 11ty (static-site generator) pulling from Ghost as a
  CMS, so the *shape* of the output (what HTML gets produced) is a
  reasonable spec to target even though the toolchain is being replaced
  entirely.

## What we are not doing

- Not standing up Ghost, Docker, or the existing pnpm/11ty toolchain.
  `Source/` stays only as a read-only reference for markup/behavior we
  are re-implementing.
- Not migrating content/CMS data. This trial targets the page
  *templates* and site structure, not a live content pipeline.
- Not chasing 1:1 pixel parity on day one. Structural/semantic parity
  first (correct pages, correct routes, correct content model in
  ARKlight's IR), visual polish after.

## Target architecture (ARKlight side)

- A new top-level ARKlight site module (e.g. `ark/site.py`) using
  `Site()` + `@site.page(...)` per route, per ARKlight's existing
  authoring model.
- Pages composed from ARKlight's structured component API (`Page`,
  `Heading`, `Text`, etc. and friends) -- no raw HTML escape hatch.
- Output compiled via `arklight build` to a plain static `ARK/`
  (or similar) output directory: HTML from the HTML backend, styling
  from the CSS backend, any interactivity from the JS backend's
  `State`/`Bind`/`Action.*` registries.
- No Python, no Ghost, no build framework in the deployed artifact --
  just static files, matching ARKlight's core premise.

## Page/route inventory to port

Working list, refined as we go (see `Source/` for the current
templates/behavior each of these corresponds to):

1. Home / listing page (paginated article feed)
2. Article page (single post)
3. Tag page (articles filtered by tag)
4. Author page (articles filtered by author)
5. Search results page
6. Static/legal pages (about, RSS notice, etc.)
7. i18n variants of the above (English first; other locales deferred)

## Sequencing (patch by patch)

Each patch below should be small enough to review on its own and land
as a single PR/commit against this repo:

1. **Scaffold** -- `arklight` added as a dependency/reference, empty
   `Site()` with a single placeholder route, `arklight build` wired up
   and producing output. No real content yet.
2. **Home/listing page** -- static (hard-coded/fixture) article list
   rendered via ARKlight components, matching `Source/`'s listing
   markup structurally.
3. **Article page** -- single-post template, including head metadata
   (`title`, `description`, `og_*`, `favicon` -- all supported by
   `Page(...)` already) ported from the fixture data.
4. **Navigation/shared layout** -- header/footer/nav extracted into
   reusable pieces so pages 2-3 stop duplicating markup.
5. **Tag and author pages** -- filtered listing variants reusing the
   home page's listing component.
6. **Search page** -- initially static/no-op UI; wiring to ARKlight's
   `State`/`Bind` model considered once v0.054 (JS backend capability
   expansion) lands upstream.
7. **Styling pass** -- CSS backend pass for visual parity (design
   tokens, responsive `@media` support already in ARKlight as of
   v0.048).
8. **i18n** -- revisit once (1)-(7) are stable for English.

Later patches will be re-numbered/split further as we learn where the
real friction is -- this list is a starting plan, not a contract.

## Reference material

- `Source/` in this repo -- the current freeCodeCamp News implementation
  (11ty + Ghost), used only as a structural/behavioral reference.
- Upstream ARKlight repo (`Rae-ARK/ARKlight`, `alpha` branch) --
  `README.md`, `docs/ARCHITECTURE.md`, and `PROGRESS.md` there track
  what the compiler currently supports and what's still in design.

## Open questions

- How much of Ghost's content model (tags, authors, pagination
  metadata) needs a fixture/stub layer vs. being hard-coded per patch
  early on.
- Whether search becomes a build-time static index or waits on
  ARKlight's upcoming reactive-state work.
- Where i18n routing (per-locale path prefixes) fits ARKlight's current
  routing model -- needs a spike before patch 8.
