from django import template
from django.utils.safestring import SafeString, mark_safe

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_outline(name, *, size=24, **kwargs):
    return _heroicon("outline", name, size, **kwargs)


@register.simple_tag
def heroicon_solid(name, *, size=20, **kwargs):
    return _heroicon("solid", name, size, **kwargs)


def _heroicon(style, name, size, **kwargs):
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    fixed_kwargs = {
        key: (value + "" if isinstance(value, SafeString) else value)
        for key, value in kwargs.items()
    }
    return mark_safe(heroicons.make_icon(style, name, size, **fixed_kwargs))
