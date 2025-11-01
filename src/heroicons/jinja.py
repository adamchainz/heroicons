from __future__ import annotations

from typing import Any

from markupsafe import Markup

import heroicons


def heroicon_micro(name: str, *, size: int | None = 16, **attrs: Any) -> str:
    return _render_icon("micro", name, size, attrs)


def heroicon_mini(name: str, *, size: int | None = 20, **attrs: Any) -> str:
    return _render_icon("mini", name, size, attrs)


def heroicon_outline(name: str, *, size: int | None = 24, **attrs: Any) -> str:
    return _render_icon("outline", name, size, attrs)


def heroicon_solid(name: str, *, size: int | None = 24, **attrs: Any) -> str:
    return _render_icon("solid", name, size, attrs)


def _render_icon(style: str, name: str, size: int | None, attrs: dict[str, Any]) -> str:
    return Markup(heroicons._render_icon(style, name, size, attrs))
