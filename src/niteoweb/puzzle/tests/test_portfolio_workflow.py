# -*- coding: utf-8 -*-
"""Test Portfolio workflow."""

from niteoweb.puzzle.tests.base import IntegrationTestCase
from plone import api
from DateTime import DateTime
from plone.app.textfield.value import RichTextValue

import unittest2 as unittest


class TestWorkflowServices(IntegrationTestCase):
    """Test the Portfolio workflow."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.folder = self.portal.folder
        self.request = self.layer['request']

        # create a sub folder
        self.subfolder = api.content.create(
            container=self.folder,
            type='Folder',
            id='subfolder',
        )

        released_date = DateTime('2012/01/10')
        project_body = RichTextValue(
            u"Wonderful project in Plone powered by eggs"
        )

        # create a project
        self.project = api.content.create(
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

    def test_project_workflow(self):
        api.content.transition(self.project, transition='publish')
        self.assertEqual(api.content.get_state(self.project), 'published')
        api.content.transition(self.project, transition='hide')
        self.assertEqual(api.content.get_state(self.project), 'private')

    def test_nonexistant_workflow(self):
        try:
            api.content.transition(self.project, transition='foobar')
        except api.exc.InvalidParameterError as e:
            self.assertEqual(
                str(e),
                "Invalid transition 'foobar'. \nValid transitions are:\npublish"
            )


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
