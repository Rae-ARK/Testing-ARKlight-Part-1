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
        "body": [
            (
                "For a few years, it looked like every new content site "
                "needed a client-side framework, a build pipeline, and a "
                "hosted rendering layer just to show some text and images. "
                "Lately that trend has started to reverse."
            ),
            (
                "Part of it is cost: a static file served from a CDN is "
                "close to free to host and nearly impossible to take down "
                "with traffic. Part of it is speed -- there's no framework "
                "to hydrate before the page is actually usable."
            ),
            (
                "The rest is maintenance. A folder of HTML and CSS doesn't "
                "have a dependency tree that needs updating every few "
                "months, and it still works exactly the same way in ten "
                "years. That durability is worth more than it used to get "
                "credit for."
            ),
        ],
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
        "body": [
            (
                "Python has supported type hints for a long time now, but "
                "a lot of codebases still don't use them -- often because "
                "it's not obvious what they actually buy you if the "
                "interpreter ignores them anyway."
            ),
            (
                "The honest answer is: they buy you tooling. A good "
                "editor can catch a whole class of mistakes -- passing "
                "the wrong type, calling a method that doesn't exist on "
                "that type -- before you ever run the code."
            ),
            (
                "Start small. Annotate function signatures first, since "
                "that's where hints pay off the most: anyone calling the "
                "function immediately knows what it expects and what it "
                "returns, without reading the implementation."
            ),
        ],
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
        "body": [
            (
                "Grid and Flexbox get compared so often that it's easy to "
                "forget they were designed for different jobs. Flexbox is "
                "one-dimensional -- it lays things out in a row or a "
                "column. Grid is two-dimensional from the start."
            ),
            (
                "In practice, that means Flexbox is usually the right "
                "call for a nav bar, a button group, or anything where "
                "items just need to flow along one axis and wrap sanely."
            ),
            (
                "Grid earns its keep once you're placing things by row "
                "and column at the same time -- a page layout, a card "
                "grid, anything where content needs to line up on two "
                "axes at once. Most real layouts end up using both."
            ),
        ],
    },
]
