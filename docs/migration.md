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
   and producing output. No real content yet. **Landed**: `ark/site.py`
   + package-shaped `ark/pages/`, building via
   `arklight build ark/site.py -o ARK`.
2. **Home/listing page** -- static (hard-coded/fixture) article list
   rendered via ARKlight components, matching `Source/`'s listing
   markup structurally. **Landed**: `ark/content/articles.py` (fixture
   data) + `ark/components/article_card.py` (`article_card()`,
   `article_list()`), rendered from `ark/pages/home.py`. Card links
   point at `/articles/<slug>` and `/tags/<tag>` routes that don't
   exist yet -- patches 3 and 5.
3. **Article page** -- single-post template, including head metadata
   (`title`, `description`, `og_*`, `favicon` -- all supported by
   `Page(...)` already) ported from the fixture data. **Landed**:
   `ark/pages/article.py`'s `article_page(article)` builds one
   content function per fixture article, registered in `ark/site.py`
   under `/articles/<slug>` via a loop (`site.page(route)(fn)` as a
   plain call rather than `@` syntax, since the slugs aren't known
   statically -- see that file's docstring for why this still
   satisfies ARKlight's static-discovery check).
4. **Navigation/shared layout** -- header/footer/nav extracted into
   reusable pieces so pages 2-3 stop duplicating markup. **Landed
   ahead of schedule, alongside patch 1**: `ark/components/layout.py`
   (`site_nav()`, `site_header()`, `site_footer()`, `page_shell()`) --
   built at the same time as the scaffold since a single placeholder
   page still needed somewhere to put reusable structure from day one.
5. **Tag and author pages** -- filtered listing variants reusing the
   home page's listing component. Nav links to `/tags`, `/authors`,
   `/search` already exist in `ark/components/layout.py` as
   placeholders pointing at routes that don't exist yet. **Landed**:
   `ark/content/taxonomy.py` derives tags/authors (and an invented
   `author_slug()`) from `ark/content/articles.py` directly -- no
   separate tag/author fixture. `ark/pages/tag.py` and
   `ark/pages/author.py` build one page per tag/author (registered in
   `ark/site.py` via the same slug-loop pattern as patch 3's article
   pages); `ark/pages/tags.py` and `ark/pages/authors.py` fill in the
   `/tags`/`/authors` directory routes the nav already linked to.
   `ark/components/article_card.py`'s byline now links to the
   author's new page. `/search` is still a placeholder -- patch 6.
6. **Search page** -- initially static/no-op UI; wiring to ARKlight's
   `State`/`Bind` model considered once v0.054 (JS backend capability
   expansion) lands upstream. **Landed**: `ark/pages/search.py`
   registers `/search` in `ark/site.py` as a plain page (no loop,
   unlike patches 3/5 -- it's a single static page). The form itself
   is deliberately non-functional (`disabled` input/button, no
   `action`) until v0.054 lands upstream; `ark/components/layout.py`'s
   nav comment updated to match.
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
