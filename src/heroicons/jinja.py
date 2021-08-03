from copy import deepcopy
from xml.etree import ElementTree

from markupsafe import Markup

import heroicons


def heroicon_outline(name, *, size=24, **kwargs):
    return _heroicon("outline", name, size, **kwargs)


def heroicon_solid(name, *, size=20, **kwargs):
    return _heroicon("solid", name, size, **kwargs)


def _heroicon(style, name, size, **kwargs):
    svg = deepcopy(heroicons.load_icon(style, name))
    svg.attrib["width"] = svg.attrib["height"] = str(size)
    svg.attrib.update(
        {key.replace("_", "-"): str(value) for key, value in kwargs.items()}
    )
    return Markup(ElementTree.tostring(svg, xml_declaration=False, encoding="unicode"))
