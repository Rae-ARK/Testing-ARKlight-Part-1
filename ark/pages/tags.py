"""Tag directory page -- stage 5.

Fills in the `/tags` nav placeholder from `ark/components/layout.py`
with a real page: one function (unlike `tag.py`'s per-tag closures)
since there's only ever one directory listing every tag.
"""

from arklight import Container, Heading, Link, Text

from components.layout import SITE_NAME, page_shell
from content.articles import ARTICLES
from content.taxonomy import all_tags, articles_by_tag


def tags_page():
    tags = all_tags(ARTICLES)
    return page_shell(
        Heading("Tags", level=1),
        Container(
            *(
                Link(
                    f"{tag} ({len(articles_by_tag(tag, ARTICLES))})",
                    href=f"/tags/{tag}",
                    class_name="tag",
                )
                for tag in tags
            ),
            class_name="tag-directory",
        ),
        Link("Back to all articles", href="/"),
        title=f"Tags - {SITE_NAME}",
        description=f"Browse every tag on {SITE_NAME}.",
    )
