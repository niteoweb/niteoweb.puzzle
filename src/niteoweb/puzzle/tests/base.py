# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone import api
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.testing import z2

import unittest2 as unittest


class NiteowebPuzzleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import niteoweb.puzzle
        self.loadZCML(package=niteoweb.puzzle)
        z2.installProduct(app, 'niteoweb.puzzle')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'niteoweb.puzzle:default')

        # Login and create some test
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        api.content.create(
            container=portal,
            type='Folder',
            id='folder',
        )

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'niteoweb.puzzle')


FIXTURE = NiteowebPuzzleLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="NiteowebPuzzleLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="NiteowebPuzzleLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
