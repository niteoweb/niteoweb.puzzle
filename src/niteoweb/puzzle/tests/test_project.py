# -*- coding: utf-8 -*-
"""Test Project content type."""

from niteoweb.puzzle.tests.base import IntegrationTestCase
from plone import api

import unittest2 as unittest


class TestRequests(IntegrationTestCase):
    """Test the Project content type."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.folder = self.portal.folder

    def test_add_project(self):
        """Test that we can add a Project."""
        api.content.create(
            container=self.folder,
            type="project",
            title=u"Über gig",
            url=u"http://www.abc.xyz",
            released=u"30/September/2012",
            ongoing=True,
            technologies=[u"Python", u"Plone"],
            description=u"Über consulting gig in Plone",
            body=u"Über consulting gig in Plone powered by eggs.",
        )
        self.assertEquals(self.folder['uber-gig'].title, u'Über gig')
        self.assertEquals(self.folder['uber-gig'].url, u'http://www.abc.xyz')
        self.assertEquals(
            self.folder['uber-gig'].released,
            u'30/September/2012'
        )
        self.assertEquals(self.folder['uber-gig'].ongoing, True)
        self.assertEquals(
            self.folder['uber-gig'].technologies,
            [u'Python', u'Plone']
        )
        self.assertEquals(
            self.folder['uber-gig'].description,
            u'Über consulting gig in Plone'
        )
        self.assertEquals(
            self.folder['uber-gig'].body,
            u'Über consulting gig in Plone powered by eggs.'
        )


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
