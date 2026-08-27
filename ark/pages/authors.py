"""Author directory page -- stage 5.

Fills in the `/authors` nav placeholder from
`ark/components/layout.py`, mirroring `tags.py` for authors.
"""

from arklight import Container, Heading, Link, Text

from components.layout import SITE_NAME, page_shell
from content.articles import ARTICLES
from content.taxonomy import all_authors, articles_by_author, author_slug


def authors_page():
    authors = all_authors(ARTICLES)
    return page_shell(
        Heading("Authors", level=1),
        Container(
            *(
                Link(
                    f"{name} ({len(articles_by_author(author_slug(name), ARTICLES))})",
                    href=f"/authors/{author_slug(name)}",
                    class_name="author",
                )
                for name in authors
            ),
            class_name="author-directory",
        ),
        Link("Back to all articles", href="/"),
        title=f"Authors - {SITE_NAME}",
        description=f"Browse every author on {SITE_NAME}.",
    )
