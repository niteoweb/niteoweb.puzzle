# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from niteoweb.puzzle.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName

import unittest2 as unittest


class TestInstall(IntegrationTestCase):
    """Test installation of niteoweb.puzzle into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if niteoweb.puzzle is installed with portal_quickinstaller."""
        self.failUnless(self.installer.isProductInstalled('niteoweb.puzzle'))

    def test_uninstall(self):
        """Test if niteoweb.puzzle is cleanly uninstalled."""
        self.installer.uninstallProducts(['niteoweb.puzzle'])
        self.failIf(self.installer.isProductInstalled('niteoweb.puzzle'))

    # properties.xml
    def test_portal_title(self):
        """Test if portal title was correctly updated."""
        title = self.portal.getProperty('title')
        self.assertEquals("Puzzle Site", title)

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that INiteowebPuzzleLayer is registered."""
        from niteoweb.puzzle.interfaces import INiteowebPuzzleLayer
        from plone.browserlayer import utils
        self.failUnless(INiteowebPuzzleLayer in utils.registered_layers())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
