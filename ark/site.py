"""ARKlight site entrypoint -- stage 0 scaffold.

Build with:

    arklight build ark/site.py -o ARK

`site` is the single `Site()` instance every page registers against.
Nothing about a page is compiled at import time -- `arklight build`
loads this file, then calls each `@site.page(...)`-registered function
to get that page's ARK AST.

Every `@site.page(...)` decorator lives in *this* file, even though the
content each route renders is built in `pages/`. ARKlight's static
discovery (`arklight/parser/discover.py`) only recognizes a real
`@site.page(...)` decorator, and only in the entry file's own source --
so a decorator in `pages/home.py` would be invisible to it. Each
`pages/*.py` module instead exports a plain content-building function,
imported and wrapped here.

`pages` and `components` are imported bare (not as `ark.pages`) because
ARKlight's loader adds this file's own directory (`ark/`) to `sys.path`
for exactly this: a package-shaped site's sibling packages resolve as
ordinary top-level imports, the same as `arklight new --template
production`'s scaffold does.

See docs/migration.md for the overall plan and patch sequence this
scaffold is patch 1 of.
"""

from arklight import Site

from pages.home import home_page

site = Site(name="arklight-news", lang="en")


@site.page("/")
def home():
    return home_page()
