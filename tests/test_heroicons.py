from xml.etree import ElementTree

import pytest

import heroicons


def test_load_icon_success_outline():
    svg = heroicons._load_icon("outline", "academic-cap")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_success_solid():
    svg = heroicons._load_icon("solid", "academic-cap")
    assert isinstance(svg, ElementTree.Element)
    assert svg.tag == ElementTree.QName("svg")


def test_load_icon_fail_unknown():
    with pytest.raises(heroicons.IconDoesNotExist) as excinfo:
        heroicons._load_icon("solid", "hoome")

    assert excinfo.value.args == (
        "The icon 'hoome' with style 'solid' does not exist.",
    )
