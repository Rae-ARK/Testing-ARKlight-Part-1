"""Shared, reusable layout pieces for every page.

ARKlight doesn't have a dedicated "component" mechanism yet (that
arrives with the planned v0.010 Components milestone, per ARKlight's
own docs/ARCHITECTURE.md) -- today, reuse is just calling plain Python
functions that return ARKNode trees, the same pattern its own
`examples/hello_site/site.py` uses. This module applies that pattern
to the News rebuild: one nav, one header, one footer, and a
`page_shell()` every page in `ark/pages/` builds on top of, so the
site only has one place to change any of them.
"""

from arklight import Container, Footer, Header, Link, Nav, Page, Text

SITE_NAME = "freeCodeCamp News"

# Tags/Authors are real routes as of stage 5 (see
# `ark/pages/tags.py`/`ark/pages/authors.py` and the loops in
# `ark/site.py`). Search is a real route too as of stage 6, but its
# form is deliberately non-functional -- see `ark/pages/search.py`.
_NAV_LINKS = (
    ("Tags", "/tags"),
    ("Authors", "/authors"),
    ("Search", "/search"),
)


def site_nav():
    """Primary site navigation, reused on every page."""
    return Nav(
        Link(SITE_NAME, href="/", class_name="brand"),
        Container(
            *(Link(label, href=href) for label, href in _NAV_LINKS),
            class_name="nav-links",
        ),
        class_name="site-nav",
    )


def site_header():
    """Page header wrapping the shared nav."""
    return Header(site_nav(), class_name="site-header")


def site_footer():
    """Footer reused on every page."""
    return Footer(
        Text(f"{SITE_NAME} -- rebuilt on ARKlight."),
        Link(
            "View source",
            href="https://github.com/Rae-ARK/Testing-ARKlight-Part-1",
        ),
        class_name="site-footer",
    )


def page_shell(*content, title, **page_kwargs):
    """Wrap a page's own content with the shared header/nav/footer.

    Every page module should build its body with this instead of
    calling `Page(...)` directly, so the header/nav/footer stay
    consistent -- and only need to change in one place -- across all
    pages. Extra `Page(...)` kwargs (`description`, `og_title`,
    `og_description`, `og_image`, `favicon`, `responsive_style`, ...)
    pass straight through untouched.
    """
    return Page(
        site_header(),
        Container(*content, class_name="page-content"),
        site_footer(),
        title=title,
        **page_kwargs,
    )
