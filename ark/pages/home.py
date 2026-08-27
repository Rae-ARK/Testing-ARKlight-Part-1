"""Home / listing page -- stage 0 scaffold placeholder.

This is a plain content-building function, not a route itself: ARKlight's
static discovery only recognizes a real `@site.page(...)` decorator, and
only in the *entry* file's own source (`arklight/parser/discover.py`).
So the decorator lives in `ark/site.py`, which imports `home_page` from
here and wraps it -- this module just builds the ARKNode tree.

This confirms the ARKlight build pipeline is wired up end-to-end
(`ark/site.py` -> `arklight build` -> static HTML) using the shared
`page_shell()`. The real article listing (docs/migration.md,
sequencing step 2) replaces this body with fixture-backed article
cards.
"""

from arklight import Heading, Text

from components.layout import SITE_NAME, page_shell


def home_page():
    return page_shell(
        Heading(SITE_NAME, level=1),
        Text(
            "This site is being rebuilt on ARKlight, one page at a time. "
            "See docs/migration.md in this repo for the plan.",
            class_name="muted",
        ),
        title=SITE_NAME,
        description="freeCodeCamp's developer news, rebuilt on ARKlight.",
    )
