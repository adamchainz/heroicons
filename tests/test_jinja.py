from jinja2 import DictLoader, Environment

from heroicons.jinja import heroicon_outline, heroicon_solid


def make_environment(index_template):
    env = Environment(loader=DictLoader({"index": index_template}))
    env.globals.update(
        {
            "heroicon_outline": heroicon_outline,
            "heroicon_solid": heroicon_solid,
        }
    )
    return env


def test_success_outline_simple():
    env = make_environment('{{ heroicon_outline("academic-cap") }}')
    template = env.get_template("index")

    result = template.render()

    assert result.startswith(
        '<svg width="24" height="24" fill="none" viewBox="0 0 24 24" '
        + 'stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")


def test_success_outline_complete():
    env = make_environment(
        '{{ heroicon_outline("academic-cap", size=48, class="h-4 w-4", '
        + 'data_test="a < 2") }}'
    )
    template = env.get_template("index")

    result = str(template.render())

    assert result.startswith(
        '<svg width="48" height="48" class="h-4 w-4" data-test="a &lt; 2" '
        + 'fill="none" viewBox="0 0 24 24" stroke="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")


def test_success_solid():
    env = make_environment(
        '{{ heroicon_solid("academic-cap", size=40, class="h-4 w-4 inline") }}'
    )
    template = env.get_template("index")

    result = template.render()

    assert result.startswith(
        '<svg width="40" height="40" class="h-4 w-4 inline" '
        + 'viewBox="0 0 20 20" fill="currentColor">'
    )
    assert "<path" in result
    assert result.endswith("</svg>\n")
