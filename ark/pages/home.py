"""Home / listing page.

Stage 2 (docs/migration.md, sequencing step 2): renders the fixture
article list from `ark/content/articles.py` via the shared
`article_list()` card component. Stage 1's placeholder body is gone --
this is the real (if fixture-backed) listing now.
"""

from arklight import Heading, Text

from components.article_card import article_list
from components.layout import SITE_NAME, page_shell
from content.articles import ARTICLES


def home_page():
    return page_shell(
        Heading(SITE_NAME, level=1),
        Text(
            "Developer news and tutorials, rebuilt on ARKlight.",
            class_name="muted",
        ),
        article_list(ARTICLES),
        title=SITE_NAME,
        description="freeCodeCamp's developer news, rebuilt on ARKlight.",
    )
