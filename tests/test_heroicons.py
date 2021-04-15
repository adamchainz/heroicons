import heroicons


def test_success_outline():
    svg = heroicons.load_icon("outline", "academic-cap")
    assert svg.startswith("<svg")


def test_success_solid():
    svg = heroicons.load_icon("solid", "academic-cap")
    assert svg.startswith("<svg")
