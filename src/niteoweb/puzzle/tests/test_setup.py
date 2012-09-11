# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from niteoweb.puzzle.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName
from plone import api

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

    # metadata.xml
    def test_dependencies_installed(self):
        """Test that all dependencies are installed."""
        installer = api.portal.get_tool('portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('plone.app.dexterity'))
        self.assertTrue(installer.isProductInstalled('collective.portlet.embed'))
        self.assertTrue(installer.isProductInstalled('ContentWellPortlets'))
        self.assertTrue(installer.isProductInstalled('plone.app.theming'))

    # types/Folder.xml
    def test_folder_available_layouts(self):
        """Test that our custom display layout (@@todo) is available on folders
        and that the default ones are also still there.
        """
        layouts = self.portal.folder.getAvailableLayouts()
        layout_ids = [id for id, title in layouts]

        # default layouts
        self.assertIn('folder_listing', layout_ids)
        self.assertIn('folder_summary_view', layout_ids)
        self.assertIn('folder_tabular_view', layout_ids)
        self.assertIn('atct_album_view', layout_ids)
        self.assertIn('folder_full_view', layout_ids)

        # our custom one
        self.assertIn('portfolio', layout_ids)

    # types/project.xml
    def test_project_installed(self):
        """Test that Todo Item content type is listed in portal_types."""
        types = api.portal.get_tool('portal_types')
        self.assertIn('project', types.objectIds())

    # workflows/project_workflow/definition.xml
    def test_project_workflow_installed(self):
        """"Test that project_workflow is listed in portal_workflow."""
        workflow = api.portal.get_tool('portal_workflow')
        self.assertIn('project_workflow', workflow.objectIds())

    # workflows.xml
    def test_project_workflow(self):
        """Test if project is present and mapped to Portfolio content type."""
        workflow = api.portal.get_tool('portal_workflow')
        for portal_type, chain in workflow.listChainOverrides():
            if portal_type in ('project', ):
                self.assertEquals(('project_workflow',), chain)

    # jsregistry.xml
    def test_js_registered(self):
        """Test if collapsiblesections.js JavaScript file is registered in
        portal_javascript.
        """
        resources = self.portal.portal_javascripts.getResources()
        ids = [r.getId() for r in resources]

        self.assertIn('collapsiblesections.js', ids)

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
