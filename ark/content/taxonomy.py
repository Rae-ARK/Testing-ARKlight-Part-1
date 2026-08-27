"""Tag/author derivation helpers -- stage 5.

Nothing here is its own fixture: tags and authors aren't separate
content types, they're just facets of `ark/content/articles.py`'s
`ARTICLES`. This module derives the tag/author route list and the
filtered listings from that one source of truth, the same way
`ark/pages/site.py`'s article loop derives `/articles/<slug>` routes
from `ARTICLES` directly rather than a separate slug list.

Author *slugs* are invented here (there's no fixture field for one,
unlike articles which already have `slug`) -- `author_slug()` is the
single place that turns "Priya Nandakumar" into "priya-nandakumar",
so every route/link agrees on the same spelling.
"""

import re

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def author_slug(name):
    """Turn a display name into a URL-safe slug, e.g. 'Priya Nandakumar'
    -> 'priya-nandakumar'. The inverse of this (slug -> display name) is
    `author_name_for_slug()` below -- both must agree on the mapping.
    """
    return _SLUG_RE.sub("-", name.strip().lower()).strip("-")


def all_tags(articles):
    """Every distinct tag across `articles`, sorted for a stable route/
    listing order (fixture order isn't a meaningful ordering here)."""
    return sorted({tag for article in articles for tag in article["tags"]})


def all_authors(articles):
    """Every distinct author display name across `articles`, sorted."""
    return sorted({article["author"] for article in articles})


def articles_by_tag(tag, articles):
    """Fixture articles carrying `tag`, in fixture order."""
    return [article for article in articles if tag in article["tags"]]


def articles_by_author(slug, articles):
    """Fixture articles by whichever author's name maps to `slug`."""
    return [article for article in articles if author_slug(article["author"]) == slug]


def author_name_for_slug(slug, articles):
    """The display name matching `slug`, or `None` if no article's
    author maps to it. Only needed because pages take a slug (from the
    route) but want to render the human-readable name."""
    for article in articles:
        if author_slug(article["author"]) == slug:
            return article["author"]
    return None
