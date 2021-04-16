from django import template
from django.utils.html import format_html

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_outline(name, *, size=24, **kwargs):
    return _heroicon("outline", name, size, **kwargs)


@register.simple_tag
def heroicon_solid(name, *, size=20, **kwargs):
    return _heroicon("solid", name, size, **kwargs)


def _heroicon(style, name, size, **kwargs):
    svg = heroicons.load_icon(style, name)
    start = '<svg width="{}" height="{}" '
    if kwargs:
        start += " ".join(f'{name.replace("_", "-")}="{{}}"' for name in kwargs)
        start += " "

    svg = svg.replace("<svg ", start, 1)

    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    unsafe_values = [v + "" for v in kwargs.values()]

    return format_html(svg, size, size, *unsafe_values)
