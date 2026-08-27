"""Article detail page -- stage 3.

Unlike `home.py`'s single `home_page()`, there's no single content
function here: each article gets its own, closed over its own fixture
record, because ARKlight routes are one function per route (see
`ark/site.py` for how these get registered under `/articles/<slug>`).
`article_page(article)` builds and returns that per-article function.
"""

from arklight import Container, Heading, Link, Text, Time

from components.layout import SITE_NAME, page_shell


def article_page(article):
    """Return a content-building function for one fixture article."""

    def render():
        return page_shell(
            Heading(article["title"], level=1),
            Container(
                Text(f"By {article['author']}", class_name="author"),
                Time(article["published"], datetime=article["published"]),
                class_name="article-meta",
            ),
            *(Text(paragraph) for paragraph in article["body"]),
            Container(
                *(
                    Link(tag, href=f"/tags/{tag}", class_name="tag")
                    for tag in article["tags"]
                ),
                class_name="tags",
            ),
            Link("Back to all articles", href="/"),
            title=f"{article['title']} - {SITE_NAME}",
            description=article["excerpt"],
            og_title=article["title"],
            og_description=article["excerpt"],
        )

    return render
