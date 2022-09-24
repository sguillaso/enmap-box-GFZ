from dualbandpseudocolorapp.dualbandpseudocolordialog import DualbandPseudocolorDialog
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QMenu, QAction

from decorrelationstretchapp.decorrelationstretchdialog import DecorrelationStretchDialog
from enmapbox.gui.applications import EnMAPBoxApplication
from typeguard import typechecked


def enmapboxApplicationFactory(enmapBox):
    return [DualbandPseudocolorApp(enmapBox)]


@typechecked
class DualbandPseudocolorApp(EnMAPBoxApplication):
    def __init__(self, enmapBox, parent=None):
        super().__init__(enmapBox, parent=parent)

        self.name = DualbandPseudocolorApp.__name__
        self.version = 'dev'
        self.licence = 'GNU GPL-3'

    @classmethod
    def icon(cls):
        return QIcon(':/images/themes/default/propertyicons/symbology.svg')

    @classmethod
    def title(cls):
        return 'Dualband Pseudocolor Renderer'

    def menu(self, appMenu: QMenu):
        appMenu: QMenu = self.enmapbox.menu('Tools')
        a = self.utilsAddActionInAlphanumericOrder(appMenu, self.title())
        assert isinstance(a, QAction)
        a.setIcon(self.icon())
        a.triggered.connect(self.startGUI)
        return appMenu

    def startGUI(self):
        DualbandPseudocolorDialog(parent=self.enmapbox.ui)
        w.show()
