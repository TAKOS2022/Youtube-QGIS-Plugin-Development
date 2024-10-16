#-----------------------------------------------------------
# Copyright (C) 2015 Martin Dobias
#-----------------------------------------------------------
# Licensed under the terms of GNU GPL 2
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#---------------------------------------------------------------------
import os
import inspect
from PyQt5.QtWidgets import QAction, QMessageBox
from PyQt5.QtGui import QIcon
from  qgis.core import QgsVectorLayer, QgsProject

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

def classFactory(iface):
    return MinimalPlugin(iface)


class MinimalPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        icon = os.path.join(os.path.join(cmd_folder, 'logo.png'))
        self.action = QAction(QIcon(icon), 'Load data',self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        path_to_usa_election_layers =r'D:\Youtube\Formation\QGIS_PLugin_Development\1_Setup_minimal\Result\Data\UsaCountyElection2020.shp'

        path_to_usa_style = r'D:\Youtube\Formation\QGIS_PLugin_Development\1_Setup_minimal\Result\styles\usa_styles_votes.qml'

        usa_layer = QgsVectorLayer(path_to_usa_election_layers, "Usa Count Elections", "ogr")

        if not usa_layer.isValid():
            print("Layer failed to load!")
        else:
            usa_layer.loadNamedStyle(path_to_usa_style)
            QgsProject.instance().addMapLayer(usa_layer)

       