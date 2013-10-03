from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('bda.controlpanel')


class IBdaControlpanelSettings(Interface):
    """ Controlpanel for bda shopviews
    """

    block_fields = schema.TextLine(title=_(u"Rich text fields to block"),
                                  description=_(u"help_block_fields",
                                                default=u"Enter the Field to block."),
                                  required=True,
                                  default=u'',)