"""Per-tag article listing page -- stage 5.

Same shape as `ark/pages/article.py`: no single content function,
since each tag needs its own page closed over its own filtered
article set. `tag_page(tag, articles)` builds and returns that
per-tag function; `ark/site.py` registers one per tag returned by
`content.taxonomy.all_tags()` under `/tags/<tag>`.
"""

from arklight import Heading, Link, Text

from components.article_card import article_list
from components.layout import SITE_NAME, page_shell
from content.taxonomy import articles_by_tag


def tag_page(tag, articles):
    """Return a content-building function listing `articles` tagged `tag`."""

    matching = articles_by_tag(tag, articles)

    def render():
        return page_shell(
            Heading(f"Tagged \u201c{tag}\u201d", level=1),
            Text(
                f"{len(matching)} article(s) tagged \u201c{tag}\u201d.",
                class_name="muted",
            ),
            article_list(matching),
            Link("Back to all articles", href="/"),
            title=f"{tag} - {SITE_NAME}",
            description=f"Articles tagged {tag} on {SITE_NAME}.",
        )

    return render
