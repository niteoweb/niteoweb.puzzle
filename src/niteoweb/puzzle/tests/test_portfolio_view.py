# -*- coding: utf-8 -*-
"""Test @@portfolio BrowserView."""

from niteoweb.puzzle.tests.base import IntegrationTestCase
from plone import api
from DateTime import DateTime
from plone.app.textfield.value import RichTextValue

import unittest2 as unittest


class TestView(IntegrationTestCase):
    """Test the @@portfolio BrowserView."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.folder = self.portal.folder

        # Set @@portfolio as default display view for folder
        self.folder.setLayout("portfolio")

        # get the view
        self.view = api.content.get_view(
            name='portfolio',
            context=self.folder,
            request=self.request
        )

    def test_no_projects(self):
        """Test HTML output when there are no Projects."""
        output = self.view()
        self.assertIn('No Project content types added yet, add some!', output)
        self.assertNotIn('<table class="listing"', output)

    def test_listing(self):
        """Test HTML listing output."""

        # create a sub folder
        self.subfolder = api.content.create(
            container=self.folder,
            type='Folder',
            id='subfolder',
        )

        released_date = DateTime('2012/01/10')
        project_body = RichTextValue(u"Wonderful project in Plone powered by eggs")

        # create a project
        api.content.create(
            container=self.subfolder,
            type="project",
            title=u"Try Brulé!",
            url=u"http://www.abc.xyz",
            released=released_date,
            ongoing=True,
            technologies=[u"Python", u"Plone"],
            description=u"Wonderful project in Plone",
            body=project_body,
        )

        # get view output
        output = self.view()

        # check that the 'no items found' msg is not shown
        self.assertNotIn(
            'No Project content types added yet, add some!',
            output
        )

        # check for content
        self.assertIn('collapsedOnLoad', output)
        self.assertIn('collapsibleHeader', output)
        self.assertIn('collapsibleContent', output)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
