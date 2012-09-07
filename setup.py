# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


# shamlessly stolen from Hexagon IT guys
def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('src', 'niteoweb', 'puzzle', 'version.txt').strip()

long_description = \
    read('README.rst') + \
    read('docs', 'HISTORY.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='niteoweb.puzzle',
    version=version,
    description="A mostly theming oriented package to convert a default \
        Plone 4 into our corporate website with a few pages and a blog.",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='NiteoWeb Ltd.',
    author_email='info@niteoweb.com',
    url='http://www.niteoweb.com',
    license='Restricted',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['niteoweb'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'collective.portlet.embed',
        'five.grok',
        'five.pt',
        'niteoweb.fabfile',
        'niteoweb.loginas',
        'Pillow',
        'Plone',
        'plone.app.caching',
        'plone.app.dexterity',
        'plone.app.theming',
        'Products.ContentWellPortlets',
        'setuptools',
        'z3c.jbot',
        'plone.api',
    ],
    extras_require={
        'test': [
            'mock',
            'plone.app.testing',
            'unittest2',
        ],
        'develop': [
            'jarn.mkrelease',
            'pep8',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.Clouseau',
            'Products.DocFinderTab',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'setuptools-flakes',
            'zest.releaser',
            'zptlint',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
