# -*- coding: utf-8 -*-
"""A Folder view that lists Project content types."""

from five import grok
from Products.ATContentTypes.interface import IATFolder
from collections import OrderedDict


# Search for templates in the current directory.
# Hopefully this line won't be needed in the future as I hope that we can tell
# grok to look in the current dir by default.
grok.templatedir('.')


class Portfolio(grok.View):
    """A BrowserView to display the Project listing on a Folder."""

    grok.context(IATFolder)  # type of object on which this View is available
    grok.require('zope2.View')  # what permission is needed for access

    def folders(self):
        folders = OrderedDict()
        for name, item in self.context.items():
            if not item.portal_type == "Folder":
                continue
            projects = []
            for subname, subitem in item.items():
                if subitem.portal_type == "project":
                    projects += [subitem]
            folders[item.Title] = projects
        return folders
