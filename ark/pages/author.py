"""Per-author article listing page -- stage 5.

Same pattern as `ark/pages/tag.py` and `ark/pages/article.py`: one
closure per author, registered under `/authors/<slug>` in
`ark/site.py` for each slug returned by
`content.taxonomy.all_authors()` + `author_slug()`.
"""

from arklight import Heading, Link, Text

from components.article_card import article_list
from components.layout import SITE_NAME, page_shell
from content.taxonomy import articles_by_author


def author_page(name, slug, articles):
    """Return a content-building function listing `articles` by `name`.

    `slug` is passed in (rather than recomputed from `name`) so this
    stays a pure "build a page for this author" function -- the
    slug/name pairing itself is `content.taxonomy`'s job.
    """

    matching = articles_by_author(slug, articles)

    def render():
        return page_shell(
            Heading(name, level=1),
            Text(
                f"{len(matching)} article(s) by {name}.",
                class_name="muted",
            ),
            article_list(matching),
            Link("Back to all articles", href="/"),
            title=f"{name} - {SITE_NAME}",
            description=f"Articles by {name} on {SITE_NAME}.",
        )

    return render
