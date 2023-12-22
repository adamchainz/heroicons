from __future__ import annotations

from django import template
from django.utils.safestring import mark_safe
from django.utils.safestring import SafeString

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_micro(name: str, *, size: int | None = 16, **kwargs: object) -> str:
    return _render_icon("micro", name, size, **kwargs)


@register.simple_tag
def heroicon_mini(name: str, *, size: int | None = 20, **kwargs: object) -> str:
    return _render_icon("mini", name, size, **kwargs)


@register.simple_tag
def heroicon_outline(name: str, *, size: int | None = 24, **kwargs: object) -> str:
    return _render_icon("outline", name, size, **kwargs)


@register.simple_tag
def heroicon_solid(name: str, *, size: int | None = 24, **kwargs: object) -> str:
    return _render_icon("solid", name, size, **kwargs)


def _render_icon(style: str, name: str, size: int | None, **kwargs: object) -> str:
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    fixed_kwargs = {
        key: (value + "" if isinstance(value, SafeString) else value)
        for key, value in kwargs.items()
    }
    return mark_safe(heroicons._render_icon(style, name, size, **fixed_kwargs))
