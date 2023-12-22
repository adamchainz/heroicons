from __future__ import annotations

from markupsafe import Markup

import heroicons


def heroicon_micro(name: str, *, size: int | None = 16, **kwargs: object) -> str:
    return _render_icon("micro", name, size, **kwargs)


def heroicon_mini(name: str, *, size: int | None = 20, **kwargs: object) -> str:
    return _render_icon("mini", name, size, **kwargs)


def heroicon_outline(name: str, *, size: int | None = 24, **kwargs: object) -> str:
    return _render_icon("outline", name, size, **kwargs)


def heroicon_solid(name: str, *, size: int | None = 24, **kwargs: object) -> str:
    return _render_icon("solid", name, size, **kwargs)


def _render_icon(style: str, name: str, size: int | None, **kwargs: object) -> str:
    return Markup(heroicons._render_icon(style, name, size, **kwargs))
