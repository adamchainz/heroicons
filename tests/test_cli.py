from __future__ import annotations

import pytest

from heroicons import __main__  # noqa: F401
from heroicons.cli import main


def test_no_subcommand(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main([])

    assert excinfo.value.code == 2
    out, err = capsys.readouterr()
    assert err == (
        "usage: __main__.py [-h] {update} ...\n"
        + "__main__.py: error: the following arguments are required: command\n"
    )
    assert out == ""


def test_help():
    with pytest.raises(SystemExit) as excinfo:
        main(["--help"])

    assert excinfo.value.code == 0


def test_update_no_files(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main(["update"])

    assert excinfo.value.code == 2
    out, err = capsys.readouterr()
    assert err == (
        "usage: __main__.py update [-h] file [file ...]\n"
        + "__main__.py update: error: the following arguments are required: file\n"
    )
    assert out == ""


def test_update_empty(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text("")

    result = main(["update", str(path)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
    assert path.read_text() == ""


def test_update_django_no_rename(capsys, tmp_path):
    path = tmp_path / "example.html"
    source = (
        '{% heroicon_outline "academic-cap" stroke_width=1'
        + ' data_controller="academia" %}\n'
    )
    path.write_text(source)

    result = main(["update", str(path)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
    assert path.read_text() == source


def test_update_django_simple(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{% heroicon_outline "adjustments" %}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{% heroicon_outline "adjustments-vertical" %}\n'


def test_update_django_single_quotes(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text("{% heroicon_outline 'archive' %}\n")

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == "{% heroicon_outline 'archive-box' %}\n"


def test_update_django_solid(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text("{% heroicon_solid 'archive' %}\n")

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == "{% heroicon_solid 'archive-box' %}\n"


def test_update_django_arguments(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text(
        '{% heroicon_outline "adjustments" stroke_width=1 data_year="2022" %}\n'
    )

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == (
        '{% heroicon_outline "adjustments-vertical" stroke_width=1'
        + ' data_year="2022" %}\n'
    )


def test_update_django_no_space(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{%heroicon_outline "adjustments"%}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{%heroicon_outline "adjustments-vertical"%}\n'


def test_update_django_extra_space(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{%   heroicon_outline   "adjustments"   %}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{%   heroicon_outline   "adjustments-vertical"   %}\n'


def test_update_jinja_no_rename(capsys, tmp_path):
    path = tmp_path / "example.html"
    source = (
        '{{ heroicon_outline("academic-cap", stroke_width=1,'
        + ' data_controller="academia") }}\n'
    )
    path.write_text(source)

    result = main(["update", str(path)])

    assert result == 0
    out, err = capsys.readouterr()
    assert out == ""
    assert err == ""
    assert path.read_text() == source


def test_update_jinja_simple(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{{ heroicon_outline("adjustments") }}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{{ heroicon_outline("adjustments-vertical") }}\n'


def test_update_jinja_single_quotes(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text("{{ heroicon_outline('archive') }}\n")

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == "{{ heroicon_outline('archive-box') }}\n"


def test_update_jinja_solid(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text("{{ heroicon_solid('archive') }}\n")

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == "{{ heroicon_solid('archive-box') }}\n"


def test_update_jinja_arguments(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text(
        '{{ heroicon_outline("adjustments", stroke_width=1, data_year="2022") }}\n'
    )

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == (
        '{{ heroicon_outline("adjustments-vertical", stroke_width=1,'
        + ' data_year="2022") }}\n'
    )


def test_update_jinja_no_space(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{{heroicon_outline("adjustments")}}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{{heroicon_outline("adjustments-vertical")}}\n'


def test_update_jinja_extra_space(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{{   heroicon_outline(  "adjustments"  )   }}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert (
        path.read_text() == '{{   heroicon_outline(  "adjustments-vertical"  )   }}\n'
    )


def test_update_jinja_multiline(capsys, tmp_path):
    path = tmp_path / "example.html"
    path.write_text('{{\nheroicon_outline(\n"adjustments"\n)\n}}\n')

    result = main(["update", str(path)])

    assert result == 1
    out, err = capsys.readouterr()
    assert out == ""
    assert err == f"Rewriting {path}\n"
    assert path.read_text() == '{{\nheroicon_outline(\n"adjustments-vertical"\n)\n}}\n'
