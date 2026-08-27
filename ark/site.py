"""ARKlight site entrypoint.

Build with:

    arklight build ark/site.py -o ARK

`site` is the single `Site()` instance every page registers against.
Nothing about a page is compiled at import time -- `arklight build`
loads this file, then calls each registered function to get that
page's ARK AST.

Every `@site.page(...)` decorator lives in *this* file, even though the
content each route renders is built in `pages/`. ARKlight's static
discovery (`arklight/parser/discover.py`) only recognizes a real
`@site.page(...)` decorator, and only in the entry file's own source --
so a decorator in `pages/home.py` would be invisible to it. Each
`pages/*.py` module instead exports a plain content-building function,
imported and wrapped here.

Article pages (stage 3) are the exception to "one `@site.page(...)`
decorator": there's one per fixture article, and the set of slugs
isn't known until `content/articles.py` is imported, so those are
registered with a loop calling `site.page(route)(fn)` as a plain
function call instead of `@` syntax. That's fine at *runtime* --
`Site.build_ark_ast()` iterates `site.routes`, which this populates
identically either way -- static discovery just needs to see *some*
literal `@site.page(...)` decorator here to pass its "site has pages"
check, and the `/` route below already satisfies that.

`pages` and `components` are imported bare (not as `ark.pages`) because
ARKlight's loader adds this file's own directory (`ark/`) to `sys.path`
for exactly this: a package-shaped site's sibling packages resolve as
ordinary top-level imports, the same as `arklight new --template
production`'s scaffold does.

See docs/migration.md for the overall plan and patch sequence this
scaffold is patch 1 of.
"""

from arklight import Site

from content.articles import ARTICLES
from pages.article import article_page
from pages.home import home_page

site = Site(name="arklight-news", lang="en")


@site.page("/")
def home():
    return home_page()


for _article in ARTICLES:
    site.page(f"/articles/{_article['slug']}")(article_page(_article))
