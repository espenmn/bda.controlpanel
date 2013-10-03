from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('bda.controlpanel')


#just needed for bda.plone.shop
from zope.interface import alsoProvides
from plone.directives import form
from bda.plone.shop.interfaces import IShopSettingsProvider


class IBdaControlpanelSettings(Interface):
    """ Controlpanel for bda shopviews
    """

    block_fields = schema.TextLine(title=_(u"Rich text fields to block"),
                                  description=_(u"help_block_fields",
                                                default=u"Enter the Field to block."),
                                  required=True,
                                  default=u'',)
                                  
                                  
                                  
                                  
class IShopEspenSettings(form.Schema):
    """Adds settings to bda.plone.shop's controlpanel
    """

    form.fieldset(
        'espen',
        label=_(u'Espen Settings'),
        fields=[
            'default_espen',
            ],
        )



    default_espen = schema.TextLine(
        title=_(u"label_default_espen", default=u'Her tester jeg litt'),
        description=_(u"help_default_espen",
                      default=u"Specify something")
        )


alsoProvides(IShopEspenSettings, IShopSettingsProvider)