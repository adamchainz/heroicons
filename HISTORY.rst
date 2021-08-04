=======
History
=======

* Allow customizing icons by pushing some attributes (``stroke-linecap``, ``stroke-linejoin``, ``stroke-width``, ``vector-effect``) onto the ``<path>`` elements.
* Fix a bug where non-string values would crash in Django templates.

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
