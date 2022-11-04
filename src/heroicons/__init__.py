from __future__ import annotations

import functools
from contextlib import closing
from copy import deepcopy
from xml.etree import ElementTree
from zipfile import ZipFile

from heroicons._compat import open_binary
from heroicons._compat import str_removeprefix


class IconDoesNotExist(Exception):
    pass


@functools.lru_cache(maxsize=128)
def _load_icon(style: str, name: str) -> ElementTree.Element:
    zip_data = open_binary("heroicons", "heroicons.zip")
    with closing(zip_data), ZipFile(zip_data, "r") as zip_file:
        try:
            svg_bytes = zip_file.read(f"{style}/{name}.svg")
        except KeyError:
            raise IconDoesNotExist(
                f"The icon {name!r} with style {style!r} does not exist."
            )

        svg = ElementTree.fromstring(svg_bytes.decode())
        for node in svg.iter():
            # Prevent output using the 'ns0' prefix for tags
            node.tag = ElementTree.QName(
                str_removeprefix(node.tag, "{http://www.w3.org/2000/svg}")
            )  # type: ignore[assignment]  # unclear if really allowed
        return svg


_PATH_ATTR_NAMES = frozenset(
    {
        "stroke-linecap",
        "stroke-linejoin",
        "vector-effect",
    }
)


def _render_icon(style: str, name: str, size: int | None, **kwargs: object) -> str:
    svg = deepcopy(_load_icon(style, name))
    if size is not None:
        svg.attrib["width"] = svg.attrib["height"] = str(size)

    svg_attrs = {}
    path_attrs = {}
    for raw_name, value in kwargs.items():
        name = raw_name.replace("_", "-")
        if name in _PATH_ATTR_NAMES:
            path_attrs[name] = str(value)
        else:
            svg_attrs[name] = str(value)

    svg.attrib.update(svg_attrs)
    if path_attrs:
        for path in svg.findall("path"):
            path.attrib.update(path_attrs)

    string = ElementTree.tostring(svg, encoding="unicode")
    # Inline SVG's don't need xmlns
    return string.replace(' xmlns="http://www.w3.org/2000/svg"', "", 1)
