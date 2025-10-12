from __future__ import annotations

from markupsafe import Markup

import heroicons


def heroicon_micro(name: str, *, size: int | None = 16, **attributes: dict) -> str:
    return _render_icon("micro", name, size, attributes)


def heroicon_mini(name: str, *, size: int | None = 20, **attributes: dict) -> str:
    return _render_icon("mini", name, size, attributes)


def heroicon_outline(name: str, *, size: int | None = 24, **attributes: dict) -> str:
    return _render_icon("outline", name, size, attributes)


def heroicon_solid(name: str, *, size: int | None = 24, **attributes: dict) -> str:
    return _render_icon("solid", name, size, attributes)


def _render_icon(style: str, name: str, size: int | None, attributes: dict) -> str:
    return Markup(heroicons._render_icon(style, name, size, attributes))
