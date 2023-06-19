# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MapLibraryDialog
                                 A QGIS plugin
 a map library which makes it easy to add much used maps to your project
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-02-15
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Marco Duiker - MD-kwadraat
        email                : md@md-kwadraat.nl
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'map_library_dialog_base.ui'))


class MapLibraryDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, mapLibrary, parent=None):
        """Constructor."""
        super(MapLibraryDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.mapLibrary = mapLibrary
        self.setupUi(self)

    def closeEvent(self, event):
        self.mapLibrary.close_dialog()
        super(MapLibraryDialog, self).closeEvent(event)
