"""Search page -- stage 6.

Per docs/migration.md's sequencing step 6, this is intentionally
static/no-op: a real search needs either a build-time static index or
ARKlight's reactive `State`/`Bind` model (still upstream -- see
`ark/site.py`'s stage 5 note and ARKlight's own CHANGELOG.md, which has
that JS backend capability expansion planned for v0.054, not yet
released as of the v0.048 this site builds against).

So for now the form doesn't submit anywhere and its input is
`disabled` -- rendering the shape of the eventual UI without pretending
it works, rather than wiring it to a route or JS handler that doesn't
exist yet. Revisit once v0.054 lands upstream.
"""

from arklight import Button, Form, Heading, Input, Label, Link, Text

from components.layout import SITE_NAME, page_shell


def search_page():
    return page_shell(
        Heading("Search", level=1),
        Text(
            "Search isn't wired up yet -- this is a placeholder for the "
            "eventual UI. Browse by tag or author in the meantime.",
            class_name="muted",
        ),
        Form(
            Label("Search articles", for_="search-query"),
            Input(
                type="search",
                id="search-query",
                name="q",
                placeholder="Coming soon",
                disabled=True,
            ),
            Button("Search", type="submit", disabled=True),
            class_name="search-form",
        ),
        Link("Back to all articles", href="/"),
        title=f"Search - {SITE_NAME}",
        description=f"Search {SITE_NAME} (coming soon).",
    )
