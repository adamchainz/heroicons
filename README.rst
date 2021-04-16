=========
heroicons
=========

.. image:: https://img.shields.io/github/workflow/status/adamchainz/heroicons/CI/main?style=for-the-badge
   :target: https://github.com/adamchainz/heroicons/actions?workflow=CI

.. image:: https://img.shields.io/codecov/c/github/adamchainz/heroicons/main?style=for-the-badge
   :target: https://app.codecov.io/gh/adamchainz/heroicons

.. image:: https://img.shields.io/pypi/v/heroicons.svg?style=for-the-badge
   :target: https://pypi.org/project/heroicons/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

Use `heroicons <https://heroicons.com/>`__ in your Django and Jinja templates.

Requirements
------------

Python 3.6 to 3.9 supported.

Django 2.2 to 3.2 supported.

----

**Are your tests slow?**
Check out my book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

Usage
-----

The ``heroicons`` package supports both Django templates and Jinja2 templates.
Follow the appropriate guide below.

Django templates
~~~~~~~~~~~~~~~~

1. Install with ``python -m pip install heroicons[django]``.

2. Add to your ``INSTALLED_APPS``:

   .. code-block:: python

       INSTALLED_APPS = [
           ...,
           'heroicons',
           ...,
       ]

Now in your templates you can load the template library with:

.. code-block:: django

    {% load heroicons %}

This provides two tags to render ``<svg>`` icons: ``heroicon_outline`` and ``heroicon_solid``, corresponding to the two icon styles in the set.
The tags take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `heroicons.com grid <https://heroicons.com/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed sizes: ``24`` for outline and ``20`` for solid.

* Any number of keyword arguments.
  These will be added as HTML attributes to the output ``<svg>`` tag.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

For example, to render an outline “academic-cap” icon, at 48x48, with some extra CSS classes and a data attribute “controller”, you would write:

.. code-block:: django

    {% heroicon_outline "academic-cap" size=48 class="h-4 w-4 inline" data_controller="academia" %}

Jinja templates
~~~~~~~~~~~~~~~

1. Install with ``python -m pip install heroicons[jinja]``.

2. Adjust your Jinja ``Environment`` to add the two global functions ``heroicon_outline`` and ``heroicon_solid``, imported from ``heroicons.jinja``.
   For example:

   .. code-block:: python

       from heroicons.jinja import heroicon_outline, heroicon_solid
       from jinja2 import Environment

       env = Environment()
       env.globals.update(
           {
               "heroicon_outline": heroicon_outline,
               "heroicon_solid": heroicon_solid,
           }
       )

Now in your templates you can call those two functions, which render ``<svg>`` icons corresponding to the two icon styles in the set.
The functions take these arguments:

* ``name``, positional: the name of the icon to use.
  You can see the icon names on the `heroicons.com grid <https://heroicons.com/>`__.

* ``size``, keyword: an integer that will be used for the width and height attributes of the output ``<svg>`` tag.
  Defaults to the icons’ designed sizes: ``24`` for outline and ``20`` for solid.

* Any number of keyword arguments.
  These will be added as HTML attributes to the output ``<svg>`` tag.
  Underscores in attribute names will be replaced with dashes, allowing you to define e.g. ``data-`` attributes.

For example, to render an outline “academic-cap” icon, at 48x48, with some extra CSS classes and a data attribute “controller”, you would write:

.. code-block:: jinja

    {{ heroicon_outline("academic-cap", size=48, class="h-4 w-4 inline", data_controller="academia") %}
