# -*- coding: utf-8 -*-
""" Content type defition for Citem """

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema

from collective.atcassandrastorage.storage import CassandraFieldStorage

from niteoweb.puzzle.interfaces import ICitem
from niteoweb.puzzle.config import PROJECTNAME


CitemSchema = ATFolderSchema.copy() + atapi.Schema((
    atapi.StringField(
        'cfield',
        storage=atapi.AnnotationStorage(),
        #storage=CassandraFieldStorage("AKeyspace", "AColumnFamily"),
        widget=atapi.StringWidget(
            label=u'This field gets stored in Cassandra',
        ),
    ),
))


class Citem(ATFolder):
    """ Citem content type """

    implements(ICitem)

    portal_type = 'Citem'
    schema = CitemSchema

    _at_rename_after_creation = True

    citem = atapi.ATFieldProperty('citem')


atapi.registerType(Citem, PROJECTNAME)
