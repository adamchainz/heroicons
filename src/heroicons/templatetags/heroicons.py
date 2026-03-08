from __future__ import annotations

from django import template
from django.utils.safestring import SafeString, mark_safe

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_micro(name: str, *, size: int | None = 16, **attrs: object) -> str:
    return _render_icon("micro", name, size, attrs)


@register.simple_tag
def heroicon_mini(name: str, *, size: int | None = 20, **attrs: object) -> str:
    return _render_icon("mini", name, size, attrs)


@register.simple_tag
def heroicon_outline(name: str, *, size: int | None = 24, **attrs: object) -> str:
    return _render_icon("outline", name, size, attrs)


@register.simple_tag
def heroicon_solid(name: str, *, size: int | None = 24, **attrs: object) -> str:
    return _render_icon("solid", name, size, attrs)


def _render_icon(
    style: str, name: str, size: int | None, attrs: dict[str, object]
) -> str:
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    fixed_attrs = {
        key: (value + "" if isinstance(value, SafeString) else value)
        for key, value in attrs.items()
    }
    return mark_safe(heroicons._render_icon(style, name, size, fixed_attrs))
