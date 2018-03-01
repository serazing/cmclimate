#!/usr/bin/env python

from os.path import exists
from setuptools import setup

DISTNAME = 'cmclimate'
PACKAGES = ['cmclimate']
TESTS = [p + '.tests' for p in PACKAGES]
INSTALL_REQUIRES = ['numpy >= 1.11', 'matplotlib>=1.5']
TESTS_REQUIRE = ['pytest >= 2.7.1']

URL = 'http://github.com/serazing/cmclimate'
AUTHOR = 'Guillaume Serazin'
AUTHOR_EMAIL = 'guillaume.serazin@legos.obs-mip.fr'
LICENSE = 'MIT'
DESCRIPTION = 'NCL colormaps for climate studies'
LONG_DESCRIPTION = (open('README.rst').read() if exists('README.rst') else '')
VERSION = 0.1

setup(name=DISTNAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url=URL,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      keywords=['NCL', 'colormaps'],
      packages=PACKAGES + TESTS,
      package_data = {'cmclimate': ['data/*.json']},
      install_requires=INSTALL_REQUIRES,
      zip_safe=False)
