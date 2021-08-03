import functools
import sys
from contextlib import closing
from copy import deepcopy
from xml.etree import ElementTree
from zipfile import ZipFile

if sys.version_info >= (3, 7):
    from importlib.resources import open_binary
else:
    from importlib_resources import open_binary


class IconDoesNotExist(Exception):
    pass


# Prevent 'ns0' prefix on SVG element and attributes
ElementTree.register_namespace("", "http://www.w3.org/2000/svg")


@functools.lru_cache(maxsize=128)
def load_icon(style, name):
    zip_data = open_binary("heroicons", "heroicons.zip")
    with closing(zip_data), ZipFile(zip_data, "r") as zip_file:
        try:
            svg_bytes = zip_file.read(f"{style}/{name}.svg")
        except KeyError:
            raise IconDoesNotExist(
                f"The icon {name!r} with style {style!r} does not exist."
            )

        return ElementTree.fromstring(svg_bytes.decode())


def make_icon(style, name, size, **kwargs):
    svg = deepcopy(load_icon(style, name))
    svg.attrib["width"] = svg.attrib["height"] = str(size)
    svg.attrib.update(
        {key.replace("_", "-"): str(value) for key, value in kwargs.items()}
    )
    return ElementTree.tostring(svg, encoding="unicode")
