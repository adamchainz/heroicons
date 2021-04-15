from __future__ import annotations

from django import template
from django.utils.html import format_html, mark_safe

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
    start = format_html(start, size, size, *kwargs.values())
    svg = svg.replace("<svg ", start, 1)
    return mark_safe(svg)
