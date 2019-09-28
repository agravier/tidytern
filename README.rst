========
tidytern
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
        | |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/tidytern/badge/?style=flat
    :target: https://readthedocs.org/projects/tidytern
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/agravier/tidytern.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/agravier/tidytern

.. |codecov| image:: https://codecov.io/github/agravier/tidytern/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/agravier/tidytern

.. |codacy| image:: https://img.shields.io/codacy/grade/fbd3c8649ac647b490c5412145d19bd9.svg
    :target: https://www.codacy.com/app/agravier/tidytern
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/tidytern.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/tidytern

.. |wheel| image:: https://img.shields.io/pypi/wheel/tidytern.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/tidytern

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tidytern.svg
    :alt: Supported versions
    :target: https://pypi.org/project/tidytern

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tidytern.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/tidytern

.. |commits-since| image:: https://img.shields.io/github.com/commits-since/agravier/tidytern/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/agravier/tidytern/compare/v0.0.0...master

.. end-badges

Disciplined versioned schema migration of PostgreSQL databases

Installation
============

::

    pip install tidytern

You can also install the in-development version with::

    pip install https://github.com/agravier/tidytern/archive/master.zip


Documentation
=============


https://tidytern.readthedocs.io/


Development
===========

The testing (tox.ini and .travis.yml) configuration is generated from templates. For your convenience there's an initial bootstrap tox.ini, to get the initial generation going just run:

tox
You can later regenerate tox.ini and .travis.yml by running (if you enabled the test_matrix_configurator option):

tox -e bootstrap
After this you can create the initial repository (make sure you create an empty Github project):

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


TODOs
=====

- Change '3.8-dev' to '3.8' once the final release of Python 3.8 has landed



Credits
=======

The initial project was setup with the help of `ionelmc's cookiecutter template <https://github.com/ionelmc/cookiecutter-pylibrary>`_.
