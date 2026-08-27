"""Reusable article-listing card, shared by the home page and (once
patches 5/6 land) the tag/author listing pages.

Same "reuse is just a Python function" pattern as
`ark/components/layout.py` -- see that module's docstring for why.
"""

from arklight import Article, Container, Heading, Link, Text, Time

from content.taxonomy import author_slug


def article_card(article):
    """Build a single listing card from a fixture article dict.

    `article` -- one entry from `ark/content/articles.py`'s `ARTICLES`
    (or anything with the same `slug`/`title`/`excerpt`/`author`/
    `published`/`tags` keys).
    """
    return Article(
        Heading(article["title"], level=2),
        Text(article["excerpt"], class_name="excerpt"),
        Link("Read more", href=f"/articles/{article['slug']}", class_name="read-more"),
        Container(
            Container(
                Text("By ", class_name="author-label"),
                Link(
                    article["author"],
                    href=f"/authors/{author_slug(article['author'])}",
                    class_name="author",
                ),
                class_name="byline",
            ),
            Time(article["published"], datetime=article["published"]),
            Container(
                *(
                    Link(tag, href=f"/tags/{tag}", class_name="tag")
                    for tag in article["tags"]
                ),
                class_name="tags",
            ),
            class_name="article-meta",
        ),
        class_name="article-card",
    )


def article_list(articles):
    """Build the listing container from a sequence of fixture articles."""
    return Container(
        *(article_card(article) for article in articles),
        class_name="article-list",
    )
