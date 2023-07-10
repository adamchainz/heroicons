=========
Changelog
=========

2.4.0 (2023-07-10)
------------------

* Drop Python 3.7 support.

2.3.0 (2023-06-16)
------------------

* Support Python 3.12.

2.2.0 (2023-02-25)
------------------

* Support Django 4.2.

* Upgrade embedded icon set to version 2.0.13.
  This has one fix to the ``minus`` icon.

  See the `upstream changelog <https://github.com/tailwindlabs/heroicons/blob/master/CHANGELOG.md>`__.

2.1.1 (2022-10-29)
------------------

* Upgrade embedded icon set to version 2.0.12.
  This has one fix to the ``information-circle`` icon.

  See the `changes in the upstream repo <https://github.com/tailwindlabs/heroicons/compare/v2.0.11...v2.0.12>`__.

2.1.0 (2022-10-07)
------------------

* Support ``size=None`` to disable setting the ``width`` and ``height`` icon attributes.

2.0.0 (2022-10-05)
------------------

* Upgrade embedded icon set to v2, specifically v2.0.11.
  See the `heroicons v2 release notes <https://github.com/tailwindlabs/heroicons/releases/tag/v2.0.0>`__.

  heroicons v2 is a substantially different icon set that makes a number of breaking changes:

  * Every icon has been redrawn.
  * Many icons have been renamed.
  * The “solid” style no longer defaults to 20px dimensions, but 24px.
  * There’s a new “mini” style, solid icons with 20px dimensions.

  You’ll proboably need to make some code and design changes when updating to this release.
  You don’t necessarily need to upgrade, but it’s unlikely this package will be maintained for the 1.x series icons going forwards.

  To assist with upgrading, this package now includes a CLI for updating templates:

  .. code-block:: console

      $ python -m heroicons update <filenames>

  See the `CLI documentation section <https://github.com/adamchainz/heroicons#cli>`__.

  Thanks to Andrew Ingram for upgrading the icon set in `PR #143 <https://github.com/adamchainz/heroicons/pull/143>`__.

1.8.0 (2022-06-05)
------------------

* Support Python 3.11.

* Support Django 4.1.

1.7.0 (2022-05-10)
------------------

* Drop support for Django 2.2, 3.0, and 3.1.

1.6.0 (2022-04-01)
------------------

* Upgrade embedded icon set to version 1.0.6.
  Check out the `changes in the upstream repo <https://github.com/tailwindlabs/heroicons/commits/master>`__.

  One key change is that the ``stroke-width`` attribute is now on ``<svg>`` elements rather than ``<path>``\s.
  This may require you to change your CSS, and allows you to use Tailwind’s ``stroke-<n>`` classes.
  See `upstream issue #241 <https://github.com/tailwindlabs/heroicons/issues/241>`__.

1.5.0 (2022-01-10)
------------------

* Drop Python 3.6 support.

1.4.0 (2021-10-23)
------------------

* On Python < 3.7, depend on importlib-resources >= 1.3.

* Upgrade embedded icon set to version 1.0.5.
  Check out the `changes in the upstream repo <https://github.com/tailwindlabs/heroicons/commits/master>`__.

1.3.0 (2021-10-05)
------------------

* Support Python 3.10.

1.2.0 (2021-09-28)
------------------

* Support Django 4.0.

1.1.0 (2021-08-04)
------------------

* Allow customizing icons by pushing some attributes (``stroke-linecap``, ``stroke-linejoin``, ``stroke-width``, ``vector-effect``) onto the ``<path>`` elements.
* Fix a bug where non-string values would crash in Django templates.
* Upgrade embedded icon set to version 1.0.3.
  Check out the `changes in the upstream repo <https://github.com/tailwindlabs/heroicons/compare/v1.0.2...v1.0.3>`__.

1.0.4 (2021-07-22)
------------------

* Upgrade embedded icon set to version 1.0.2.
  Check out the `changes in the upstream repo <https://github.com/tailwindlabs/heroicons/compare/v1.0.1...v1.0.2>`__.

1.0.3 (2021-04-30)
------------------

* Fix ``ResourceWarning`` from not closing the zip file after loading an icon.

1.0.2 (2021-04-22)
------------------

* Fix link on PyPI.

1.0.1 (2021-04-16)
------------------

* Fix examples in README.

1.0.0 (2021-04-16)
------------------

* First version, with Django and Jinja tags, bundling heroicons version 1.0.1.
