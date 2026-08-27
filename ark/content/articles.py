"""Fixture article data for the home/listing page.

Invented placeholder content -- standing in for whatever real content
source eventually backs this (see docs/migration.md's open questions
on the Ghost content model). Each entry mirrors the shape a real
article record would need: enough to render a listing card and, once
patch 3 lands, an article detail page at the same slug.
"""

ARTICLES = [
    {
        "slug": "why-static-sites-are-having-a-moment",
        "title": "Why Static Sites Are Having a Moment",
        "excerpt": (
            "A look at why teams keep coming back to plain HTML and CSS "
            "for content-heavy sites, even with a decade of framework "
            "churn behind them."
        ),
        "author": "Priya Nandakumar",
        "published": "2026-06-02",
        "tags": ["web-development", "static-sites"],
    },
    {
        "slug": "a-beginners-guide-to-python-type-hints",
        "title": "A Beginner's Guide to Python Type Hints",
        "excerpt": (
            "Type hints don't make Python statically typed, but they do "
            "make it a lot easier to read, refactor, and catch bugs "
            "before runtime. Here's where to start."
        ),
        "author": "Marcus Webb",
        "published": "2026-05-21",
        "tags": ["python"],
    },
    {
        "slug": "css-grid-versus-flexbox-in-2026",
        "title": "CSS Grid vs. Flexbox in 2026: Do You Still Need Both?",
        "excerpt": (
            "Grid and Flexbox solve overlapping problems. This piece "
            "walks through when each one is actually the better fit."
        ),
        "author": "Sofia Reyes",
        "published": "2026-05-09",
        "tags": ["css", "web-development"],
    },
]
