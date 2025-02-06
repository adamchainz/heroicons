=========
heroicons
=========

.. image:: https://img.shields.io/github/actions/workflow/status/adamchainz/heroicons/main.yml.svg?branch=main&style=for-the-badge
   :target: https://github.com/adamchainz/heroicons/actions?workflow=CI

.. image:: https://img.shields.io/badge/Coverage-100%25-success?style=for-the-badge
   :target: https://github.com/adamchainz/heroicons/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/heroicons.svg?style=for-the-badge
   :target: https://pypi.org/project/heroicons/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Use `heroicons <https://heroicons.com/>`__ in your Django and Jinja templates.

----

**Improve your Django and Git skills** with `my books <https://adamj.eu/books/>`__.

----

Requirements
------------

Python 3.9 to 3.13 supported.

Django 4.2 to 5.2 supported.

Usage
-----

The ``heroicons`` package supports both Django templates and Jinja templates.
Follow the appropriate guide below.

Django templates
~~~~~~~~~~~~~~~~

1. Install with ``python -m pip install heroicons[django]``.

2. Add to your ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = [
           ...,
           "heroicons",
           ...,
       ]

Now your templates can load the template library with:

.. code-block:: django

    {% load heroicons %}

Alternatively, make the library available in all templates by adding it to `the builtins option <https://docs.djangoproject.com/en/stable/topics/templates/#django.template.backends.django.DjangoTemplates>`__:

.. code-block:: python

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            # ...
            "OPTIONS": {
                # ...
                "builtins": [
                    ...,
                    "heroicons.templatetags.heroicons",
                    ...,
                ],
            },
        }
    ]

The library provides these tags to render SVG icons in their corresponding styles:

* ``heroicon_micro``
* ``heroicon_mini``
* ``heroicon_outline``
* ``heroicon_solid``

The tags take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `heroicons.com grid <https://heroicons.com/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed sizes: ``24`` for outline and solid, ``20`` for mini, and ``16`` for micro.
  Can be ``None``, in which case no width or height attributes will be output.

* Any number of keyword arguments.
  These will be added as attributes in the output HTML.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

  Most attributes will be added to the ``<svg>`` tag containing the icon, but these attributes will be attached to the inner ``<path>`` tags instead:

  * ``stroke-linecap``
  * ``stroke-linejoin``
  * ``vector-effect``

Note: unlike the SVG code you can copy from `heroicons.com <https://heroicons.com/>`__, there is no default ``class``.

Examples
^^^^^^^^

An outline “academic-cap” icon:

.. code-block:: django

    {% heroicon_outline "academic-cap" %}

The same icon, solid, at 40x40 pixels, and a CSS class:

.. code-block:: django

    {% heroicon_outline "academic-cap" size=40 class="mr-4" %}

That icon again, but with the paths changed to a narrower stroke width, and a "data-controller" attribute declared:

.. code-block:: django

    {% heroicon_outline "academic-cap" stroke_width=1 data_controller="academia" %}

Jinja templates
~~~~~~~~~~~~~~~

1. Install with ``python -m pip install heroicons[jinja]``.

2. Adjust your Jinja ``Environment`` to add the global ``heroicon_*`` functions from ``heroicons.jinja``.
   For example:

   .. code-block:: python

       from heroicons.jinja import (
           heroicon_micro,
           heroicon_mini,
           heroicon_outline,
           heroicon_solid,
       )
       from jinja2 import Environment

       env = Environment()
       env.globals.update(
           {
               "heroicon_micro": heroicon_micro,
               "heroicon_mini": heroicon_mini,
               "heroicon_outline": heroicon_outline,
               "heroicon_solid": heroicon_solid,
           }
       )

Now in your templates you can call those functions, which render ``<svg>`` icons corresponding to the icon styles in the set.
The functions take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `heroicons.com grid <https://heroicons.com/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed sizes: ``24`` for outline and solid, ``20`` for mini, and ``16`` for micro.
  Can be ``None``, in which case no width or height attributes will be output.

* Any number of keyword arguments.
  These will be added as HTML attributes to the output HTML.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

  Most attributes will be added to the ``<svg>`` tag containing the icon, but these attributes will be attached to the inner ``<path>`` tags instead:

  * ``stroke-linecap``
  * ``stroke-linejoin``
  * ``vector-effect``

Note: unlike the SVG code you can copy from `heroicons.com <https://heroicons.com/>`__, there is no default ``class``.

Examples
^^^^^^^^

An outline “academic-cap” icon:

.. code-block:: jinja

    {{ heroicon_outline("academic-cap") }}

The same icon, solid, at 40x40 pixels, and a CSS class:

.. code-block:: jinja

    {{ heroicon_solid("academic-cap", size=40, class="mr-4") %}

That icon again, but with the paths changed to a narrower stroke width, and a "data-controller" attribute declared:

.. code-block:: jinja

    {{ heroicon_outline("academic-cap", stroke_width=1, data_controller="academia") %}

CLI
---

Many icons were renamed in version 2 of heroicons.
To assist you with migrating from version 1, this package includes a CLI that can update your heroicons template tags.

Invoke the CLI like so:

.. code-block:: console

    $ python -m heroicons update <filename> <filename2> ...

To run it on all your template files, you can use |git ls-files pipe xargs|__:

.. |git ls-files pipe xargs| replace:: ``git ls-files | xargs``
__ https://adamj.eu/tech/2022/03/09/how-to-run-a-command-on-many-files-in-your-git-repository/

.. code-block:: console

    $ git ls-files -- '*.html' | xargs python -m heroicons update

The tool will update icon names for those that were renamed in v2, as per the table in the `heroicons release notes <https://github.com/tailwindlabs/heroicons/releases/tag/v2.0.0>`__.
It should find both Django and Jinja template tags:

.. code-block:: diff

  -{% heroicon_outline "archive" class="mr-2" %}
  +{% heroicon_outline "archive-box" class="mr-2" %}

  -{{ heroicon_solid("archive", class="mr-2") }}
  +{{ heroicon_solid("archive-box", class="mr-2") }}

Also note that ``solid`` icons changed their default size from 20px to 24px.
If you are using them without specifying a size, they will now be larger, which could break some designs.
You can keep the v1 size by specifying it exactly:

.. code-block:: django

    {% heroicon_solid "archive-box" size=20 %}

.. code-block:: jinja

    {{ heroicon_solid("archive-box", size=20) }}

Or through other mechanisms:

* Tailwind’s `width <https://tailwindcss.com/docs/width>`__ and `height <https://tailwindcss.com/docs/height>`__ classes: ``w-5 h-5``
* other CSS classes
* sizing the containing elements

Due to the variety of ways to size icons, it’s unfortunately not possible to automatically add the size to unsized solid icons.

Good luck, and may the odds be ever in your favour.
