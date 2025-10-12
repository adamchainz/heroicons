from __future__ import annotations

from django import template
from django.utils.safestring import SafeString, mark_safe

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_micro(name: str, *, size: int | None = 16, **attributes: dict) -> str:
    return _render_icon("micro", name, size, attributes)


@register.simple_tag
def heroicon_mini(name: str, *, size: int | None = 20, **attributes: dict) -> str:
    return _render_icon("mini", name, size, attributes)


@register.simple_tag
def heroicon_outline(name: str, *, size: int | None = 24, **attributes: dict) -> str:
    return _render_icon("outline", name, size, attributes)


@register.simple_tag
def heroicon_solid(name: str, *, size: int | None = 24, **attributes: dict) -> str:
    return _render_icon("solid", name, size, attributes)


def _render_icon(style: str, name: str, size: int | None, attributes: dict) -> str:
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    fixed_attributes = {
        key: (value + "" if isinstance(value, SafeString) else value)
        for key, value in attributes.items()
    }
    return mark_safe(heroicons._render_icon(style, name, size, fixed_attributes))
