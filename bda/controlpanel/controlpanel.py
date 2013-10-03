from plone.app.registry.browser import controlpanel

from bda.controlpanel.interfaces import IBdaControlpanelSettings, _


class BdaControlpanelSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IBdaControlpanelSettings
    label = _(u"BdaControlpanel settings")
    description = _(u"""""")

    def updateFields(self):
        super(BdaControlpanelSettingsEditForm, self).updateFields()


    def updateWidgets(self):
        super(BdaControlpanelSettingsEditForm, self).updateWidgets()

class BdaControlpanelSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = BdaControlpanelSettingsEditForm
