#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='tidytern',
    version='0.0.0',
    description='Disciplined versioned schema migration of PostgreSQL databases',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Alexandre Gravier',
    author_email='al.gravier@gmail.com',
    url='https://github.com/agravier/tidytern',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Database',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://tidytern.readthedocs.io/',
        'Changelog': 'https://tidytern.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/agravier/tidytern/issues',
    },
    keywords=[
        'postgresql', 'migration', 'database'
    ],
    python_requires='>=3.7',
    install_requires=[
        'click',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    setup_requires=[
        'wheel'
    ],
    entry_points={
        'console_scripts': [
            'tidytern = tidytern.cli:main',
        ]
    },
)
