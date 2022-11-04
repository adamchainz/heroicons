from __future__ import annotations

import sys
from typing import Any

import django
from django.conf import settings
from django.template import Context
from django.template import Template

settings.configure(
    ROOT_URLCONF=__name__,  # Make this module the urlconf
    SECRET_KEY="insecure",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "APP_DIRS": False,
        },
    ],
    INSTALLED_APPS=["heroicons"],
)
urlpatterns: list[Any] = []
django.setup()


def test_success_outline_simple():
    template = Template('{% load heroicons %}{% heroicon_outline "academic-cap" %}')

    result = template.render(Context())

    expected_py37 = (
        '<svg aria-hidden="true" fill="none" height="24" stroke="currentColor"'
        ' stroke-width="1.5" viewBox="0 0 24 24" width="24">\n  <path d="M4.26'
        " 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627"
        " 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0"
        " 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399"
        " 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112"
        " 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000"
        " 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75"
        ' 15.75v-1.5" stroke-linecap="round" stroke-linejoin="round" />\n</svg>'
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"'
        ' aria-hidden="true" width="24" height="24">\n  <path stroke-linecap="round"'
        ' stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627'
        " 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0"
        " 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112"
        " 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482"
        " 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0"
        " 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007"
        ' 11.55A5.981 5.981 0 006.75 15.75v-1.5" />\n</svg>'
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_outline_path_attr():
    template = Template(
        "{% load heroicons %}"
        + '{% heroicon_outline "academic-cap" stroke_linecap="butt" %}'
    )

    result = template.render(Context())

    expected_py37 = (
        '<svg aria-hidden="true" fill="none" height="24" stroke="currentColor"'
        ' stroke-width="1.5" viewBox="0 0 24 24" width="24">\n  <path d="M4.26'
        " 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627"
        " 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0"
        " 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399"
        " 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112"
        " 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000"
        " 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75"
        ' 15.75v-1.5" stroke-linecap="butt" stroke-linejoin="round" />\n</svg>'
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"'
        ' aria-hidden="true" width="24" height="24">\n  <path stroke-linecap="butt"'
        ' stroke-linejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627'
        " 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0"
        " 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112"
        " 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482"
        " 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0"
        " 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007"
        ' 11.55A5.981 5.981 0 006.75 15.75v-1.5" />\n</svg>'
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_outline_complete():
    template = Template(
        "{% load heroicons %}"
        + '{% heroicon_outline "academic-cap" size=48 class="h-4 w-4" '
        + 'data_test="a < 2" %}'
    )

    result = template.render(Context())

    expected_py37 = (
        '<svg aria-hidden="true" class="h-4 w-4" data-test="a &lt; 2" fill="none"'
        ' height="48" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"'
        ' width="48">\n  <path d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627'
        " 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0"
        " 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112"
        " 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482"
        " 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0"
        " 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007"
        ' 11.55A5.981 5.981 0 006.75 15.75v-1.5" stroke-linecap="round"'
        ' stroke-linejoin="round" />\n</svg>'
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"'
        ' aria-hidden="true" width="48" height="48" class="h-4 w-4" data-test="a &lt;'
        ' 2">\n  <path stroke-linecap="round" stroke-linejoin="round" d="M4.26'
        " 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627"
        " 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0"
        " 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399"
        " 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112"
        " 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000"
        " 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75"
        ' 15.75v-1.5" />\n</svg>'
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_outline_size_none():
    template = Template(
        "{% load heroicons %}" + '{% heroicon_outline "academic-cap" size=None %}'
    )

    result = template.render(Context())

    expected_py37 = (
        '<svg aria-hidden="true" fill="none"'
        ' stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">\n '
        ' <path d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627'
        " 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0"
        " 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112"
        " 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482"
        " 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0"
        " 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007"
        ' 11.55A5.981 5.981 0 006.75 15.75v-1.5" stroke-linecap="round"'
        ' stroke-linejoin="round" />\n</svg>'
    )
    expected_py38plus = (
        '<svg fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"'
        ' aria-hidden="true">\n '
        ' <path stroke-linecap="round" stroke-linejoin="round" d="M4.26'
        " 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627"
        " 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0"
        " 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399"
        " 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112"
        " 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000"
        " 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75"
        ' 15.75v-1.5" />\n</svg>'
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_solid():
    template = Template(
        "{% load heroicons %}"
        + '{% heroicon_solid "academic-cap" size=40 class="h-4 w-4 inline" %}'
    )

    result = template.render(Context())

    expected_py37 = (
        '<svg aria-hidden="true" class="h-4 w-4 inline" fill="currentColor" height="40"'
        ' viewBox="0 0 24 24" width="40">\n  <path d="M11.7 2.805a.75.75 0 01.6 0A60.65'
        " 60.65 0 0122.83 8.72a.75.75 0 01-.231 1.337 49.949 49.949 0 00-9.902"
        " 3.912l-.003.002-.34.18a.75.75 0 01-.707 0A50.009 50.009 0 007.5"
        " 12.174v-.224c0-.131.067-.248.172-.311a54.614 54.614 0 014.653-2.52.75.75 0"
        " 00-.65-1.352 56.129 56.129 0 00-4.78 2.589 1.858 1.858 0 00-.859 1.228 49.803"
        ' 49.803 0 00-4.634-1.527.75.75 0 01-.231-1.337A60.653 60.653 0 0111.7 2.805z"'
        ' />\n  <path d="M13.06 15.473a48.45 48.45 0 017.666-3.282c.134 1.414.22'
        " 2.843.255 4.285a.75.75 0 01-.46.71 47.878 47.878 0 00-8.105 4.342.75.75 0"
        " 01-.832 0 47.877 47.877 0 00-8.104-4.342.75.75 0"
        " 01-.461-.71c.035-1.442.121-2.87.255-4.286A48.4 48.4 0 016 13.18v1.27a1.5 1.5"
        " 0 00-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.661a6.729"
        " 6.729 0 00.551-1.608 1.5 1.5 0 00.14-2.67v-.645a48.549 48.549 0 013.44 1.668"
        ' 2.25 2.25 0 002.12 0z" />\n  <path d="M4.462 19.462c.42-.419.753-.89'
        " 1-1.394.453.213.902.434 1.347.661a6.743 6.743 0 01-1.286 1.794.75.75 0"
        ' 11-1.06-1.06z" />\n</svg>'
    )
    expected_py38plus = (
        '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true" width="40"'
        ' height="40" class="h-4 w-4 inline">\n  <path d="M11.7 2.805a.75.75 0 01.6'
        " 0A60.65 60.65 0 0122.83 8.72a.75.75 0 01-.231 1.337 49.949 49.949 0 00-9.902"
        " 3.912l-.003.002-.34.18a.75.75 0 01-.707 0A50.009 50.009 0 007.5"
        " 12.174v-.224c0-.131.067-.248.172-.311a54.614 54.614 0 014.653-2.52.75.75 0"
        " 00-.65-1.352 56.129 56.129 0 00-4.78 2.589 1.858 1.858 0 00-.859 1.228 49.803"
        ' 49.803 0 00-4.634-1.527.75.75 0 01-.231-1.337A60.653 60.653 0 0111.7 2.805z"'
        ' />\n  <path d="M13.06 15.473a48.45 48.45 0 017.666-3.282c.134 1.414.22'
        " 2.843.255 4.285a.75.75 0 01-.46.71 47.878 47.878 0 00-8.105 4.342.75.75 0"
        " 01-.832 0 47.877 47.877 0 00-8.104-4.342.75.75 0"
        " 01-.461-.71c.035-1.442.121-2.87.255-4.286A48.4 48.4 0 016 13.18v1.27a1.5 1.5"
        " 0 00-.14 2.508c-.09.38-.222.753-.397 1.11.452.213.901.434 1.346.661a6.729"
        " 6.729 0 00.551-1.608 1.5 1.5 0 00.14-2.67v-.645a48.549 48.549 0 013.44 1.668"
        ' 2.25 2.25 0 002.12 0z" />\n  <path d="M4.462 19.462c.42-.419.753-.89'
        " 1-1.394.453.213.902.434 1.347.661a6.743 6.743 0 01-1.286 1.794.75.75 0"
        ' 11-1.06-1.06z" />\n</svg>'
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected


def test_success_mini():
    template = Template(
        "{% load heroicons %}"
        + '{% heroicon_mini "academic-cap" size=40 class="h-4 w-4 inline" %}'
    )

    result = template.render(Context())

    expected_py37 = (
        '<svg aria-hidden="true" class="h-4 w-4 inline" fill="currentColor" height="40"'
        ' viewBox="0 0 20 20" width="40">\n  <path clip-rule="evenodd" d="M9.664'
        " 1.319a.75.75 0 01.672 0 41.059 41.059 0 018.198 5.424.75.75 0 01-.254 1.285"
        " 31.372 31.372 0 00-7.86 3.83.75.75 0 01-.84 0 31.508 31.508 0"
        " 00-2.08-1.287V9.394c0-.244.116-.463.302-.592a35.504 35.504 0"
        " 013.305-2.033.75.75 0 00-.714-1.319 37 37 0 00-3.446 2.12A2.216 2.216 0 006"
        " 9.393v.38a31.293 31.293 0 00-4.28-1.746.75.75 0 01-.254-1.285 41.059 41.059 0"
        " 018.198-5.424zM6 11.459a29.848 29.848 0 00-2.455-1.158 41.029 41.029 0 00-.39"
        " 3.114.75.75 0 00.419.74c.528.256 1.046.53"
        " 1.554.82-.21.324-.455.63-.739.914a.75.75 0 101.06"
        " 1.06c.37-.369.69-.77.96-1.193a26.61 26.61 0 013.095 2.348.75.75 0 00.992 0"
        " 26.547 26.547 0 015.93-3.95.75.75 0 00.42-.739 41.053 41.053 0 00-.39-3.114"
        " 29.925 29.925 0 00-5.199 2.801 2.25 2.25 0 01-2.514"
        " 0c-.41-.275-.826-.541-1.25-.797a6.985 6.985 0 01-1.084 3.45 26.503 26.503 0"
        ' 00-1.281-.78A5.487 5.487 0 006 12v-.54z" fill-rule="evenodd" />\n</svg>'
    )
    expected_py38plus = (
        '<svg viewBox="0 0 20 20" fill="currentColor" aria-hidden="true" width="40"'
        ' height="40" class="h-4 w-4 inline">\n  <path fill-rule="evenodd" d="M9.664'
        " 1.319a.75.75 0 01.672 0 41.059 41.059 0 018.198 5.424.75.75 0 01-.254 1.285"
        " 31.372 31.372 0 00-7.86 3.83.75.75 0 01-.84 0 31.508 31.508 0"
        " 00-2.08-1.287V9.394c0-.244.116-.463.302-.592a35.504 35.504 0"
        " 013.305-2.033.75.75 0 00-.714-1.319 37 37 0 00-3.446 2.12A2.216 2.216 0 006"
        " 9.393v.38a31.293 31.293 0 00-4.28-1.746.75.75 0 01-.254-1.285 41.059 41.059 0"
        " 018.198-5.424zM6 11.459a29.848 29.848 0 00-2.455-1.158 41.029 41.029 0 00-.39"
        " 3.114.75.75 0 00.419.74c.528.256 1.046.53"
        " 1.554.82-.21.324-.455.63-.739.914a.75.75 0 101.06"
        " 1.06c.37-.369.69-.77.96-1.193a26.61 26.61 0 013.095 2.348.75.75 0 00.992 0"
        " 26.547 26.547 0 015.93-3.95.75.75 0 00.42-.739 41.053 41.053 0 00-.39-3.114"
        " 29.925 29.925 0 00-5.199 2.801 2.25 2.25 0 01-2.514"
        " 0c-.41-.275-.826-.541-1.25-.797a6.985 6.985 0 01-1.084 3.45 26.503 26.503 0"
        ' 00-1.281-.78A5.487 5.487 0 006 12v-.54z" clip-rule="evenodd" />\n</svg>'
    )
    if sys.version_info < (3, 8):
        expected = expected_py37
    else:
        expected = expected_py38plus
    assert result == expected
