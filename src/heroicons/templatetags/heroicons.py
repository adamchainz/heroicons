from django import template
from django.utils.safestring import SafeString, mark_safe

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_outline(name: str, *, size: int = 24, **kwargs: object) -> str:
    return _render_icon("outline", name, size, **kwargs)


@register.simple_tag
def heroicon_solid(name: str, *, size: int = 20, **kwargs: object) -> str:
    return _render_icon("solid", name, size, **kwargs)


def _render_icon(style: str, name: str, size: int, **kwargs: object) -> str:
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    fixed_kwargs = {
        key: (value + "" if isinstance(value, SafeString) else value)
        for key, value in kwargs.items()
    }
    return mark_safe(heroicons._render_icon(style, name, size, **fixed_kwargs))
