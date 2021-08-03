from copy import deepcopy
from xml.etree import ElementTree

from django import template
from django.utils.safestring import mark_safe

import heroicons

register = template.Library()


@register.simple_tag
def heroicon_outline(name, *, size=24, **kwargs):
    return _heroicon("outline", name, size, **kwargs)


@register.simple_tag
def heroicon_solid(name, *, size=20, **kwargs):
    return _heroicon("solid", name, size, **kwargs)


def _heroicon(style, name, size, **kwargs):
    svg = deepcopy(heroicons.load_icon(style, name))
    svg.attrib["width"] = svg.attrib["height"] = str(size)
    # simple_tag's parsing loads passed strings as safe, but they aren't
    # Cast the SafeString's back to normal strings the only way possible, by
    # concatenating the empty string.
    svg.attrib.update(
        {key.replace("_", "-"): (value + "") for key, value in kwargs.items()}
    )
    return mark_safe(ElementTree.tostring(svg, encoding="unicode"))
