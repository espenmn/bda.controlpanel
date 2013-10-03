from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('bda.controlpanel')


#just needed for bda.plone.shop
from zope.interface import alsoProvides
from plone.directives import form
from bda.plone.shop.interfaces import IShopSettingsProvider

#from plone.registry.interfaces import IRegistry

class IBdaControlpanelSettings(Interface):
    """ An extra controlpanel for bda shop
    """

    block_fields = schema.TextLine(title=_(u"Rich text fields to block"),
                                  description=_(u"help_block_fields",
                                                default=u"Enter the Field to block."),
                                  required=True,
                                  default=u'',)
                                  
                                                         
                                  
class IShopExtraSettings(form.Schema):
    """Adds settings to bda.plone.shop's controlpanel
    """

    form.fieldset(
        'extra',
        label=_(u'Extra Settings'),
        fields=[
            'block_fields',
            ],
        )

    block_fields = schema.TextLine(
        title=_(u"label_block_fields", default=u"Her tester jeg litt"),
        description=_(u"help_block_fields",
                      default=u"Block some fields")
        )


alsoProvides(IShopExtraSettings, IShopSettingsProvider)

