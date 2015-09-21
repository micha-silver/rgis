# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_rivergis.ui'
#
# Created: Fri Sep 18 14:44:27 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RiverGIS(object):
    def setupUi(self, RiverGIS):
        RiverGIS.setObjectName(_fromUtf8("RiverGIS"))
        RiverGIS.setEnabled(True)
        RiverGIS.resize(593, 351)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/rivergis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RiverGIS.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(RiverGIS)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelCurSchema = QtGui.QLabel(self.centralwidget)
        self.labelCurSchema.setObjectName(_fromUtf8("labelCurSchema"))
        self.gridLayout.addWidget(self.labelCurSchema, 0, 3, 1, 1)
        self.labelCurDatabase = QtGui.QLabel(self.centralwidget)
        self.labelCurDatabase.setObjectName(_fromUtf8("labelCurDatabase"))
        self.gridLayout.addWidget(self.labelCurDatabase, 0, 0, 1, 1)
        self.schemasCbo = QtGui.QComboBox(self.centralwidget)
        self.schemasCbo.setMinimumSize(QtCore.QSize(200, 0))
        self.schemasCbo.setObjectName(_fromUtf8("schemasCbo"))
        self.gridLayout.addWidget(self.schemasCbo, 0, 4, 1, 1)
        self.connsCbo = QtGui.QComboBox(self.centralwidget)
        self.connsCbo.setMinimumSize(QtCore.QSize(200, 0))
        self.connsCbo.setObjectName(_fromUtf8("connsCbo"))
        self.gridLayout.addWidget(self.connsCbo, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.crsWidget = QgsProjectionSelectionWidget(self.centralwidget)
        self.crsWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.crsWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.crsWidget.setObjectName(_fromUtf8("crsWidget"))
        self.horizontalLayout.addWidget(self.crsWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        RiverGIS.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RiverGIS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuRASMapping = QtGui.QMenu(self.menubar)
        self.menuRASMapping.setObjectName(_fromUtf8("menuRASMapping"))
        self.menu_Geometry = QtGui.QMenu(self.menubar)
        self.menu_Geometry.setObjectName(_fromUtf8("menu_Geometry"))
        self.menuXS_Cut_Line_Attributes = QtGui.QMenu(self.menu_Geometry)
        self.menuXS_Cut_Line_Attributes.setObjectName(_fromUtf8("menuXS_Cut_Line_Attributes"))
        self.menuStreamCenterlineAttributes = QtGui.QMenu(self.menu_Geometry)
        self.menuStreamCenterlineAttributes.setObjectName(_fromUtf8("menuStreamCenterlineAttributes"))
        self.menuUtilities = QtGui.QMenu(self.menu_Geometry)
        self.menuUtilities.setObjectName(_fromUtf8("menuUtilities"))
        self.menuDB = QtGui.QMenu(self.menubar)
        self.menuDB.setObjectName(_fromUtf8("menuDB"))
        RiverGIS.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RiverGIS)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RiverGIS.setStatusBar(self.statusbar)
        self.actionCreate2dAreaPerimeter = QtGui.QAction(RiverGIS)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/2darea_perimeter.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate2dAreaPerimeter.setIcon(icon1)
        self.actionCreate2dAreaPerimeter.setObjectName(_fromUtf8("actionCreate2dAreaPerimeter"))
        self.actionRASCorrectLateralWeirs = QtGui.QAction(RiverGIS)
        self.actionRASCorrectLateralWeirs.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/correctLateralWeir.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASCorrectLateralWeirs.setIcon(icon2)
        self.actionRASCorrectLateralWeirs.setObjectName(_fromUtf8("actionRASCorrectLateralWeirs"))
        self.actionRASCreate2dArea = QtGui.QAction(RiverGIS)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/2darea.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASCreate2dArea.setIcon(icon3)
        self.actionRASCreate2dArea.setObjectName(_fromUtf8("actionRASCreate2dArea"))
        self.actionAbout = QtGui.QAction(RiverGIS)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelpContents = QtGui.QAction(RiverGIS)
        self.actionHelpContents.setObjectName(_fromUtf8("actionHelpContents"))
        self.actionLoad_2D_WSEL_from_HDF = QtGui.QAction(RiverGIS)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/loadWselHdf.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_2D_WSEL_from_HDF.setIcon(icon4)
        self.actionLoad_2D_WSEL_from_HDF.setObjectName(_fromUtf8("actionLoad_2D_WSEL_from_HDF"))
        self.actionRASWaterSurfaceGeneration = QtGui.QAction(RiverGIS)
        self.actionRASWaterSurfaceGeneration.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/createWselRaster.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASWaterSurfaceGeneration.setIcon(icon5)
        self.actionRASWaterSurfaceGeneration.setObjectName(_fromUtf8("actionRASWaterSurfaceGeneration"))
        self.actionImportRiverFromIsokp = QtGui.QAction(RiverGIS)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/importFromIsok.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImportRiverFromIsokp.setIcon(icon6)
        self.actionImportRiverFromIsokp.setObjectName(_fromUtf8("actionImportRiverFromIsokp"))
        self.actionRefreshConnections = QtGui.QAction(RiverGIS)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/action_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefreshConnections.setIcon(icon7)
        self.actionRefreshConnections.setObjectName(_fromUtf8("actionRefreshConnections"))
        self.actionRASFloodplainDelineation = QtGui.QAction(RiverGIS)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/createDepthsAndRange.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASFloodplainDelineation.setIcon(icon8)
        self.actionRASFloodplainDelineation.setObjectName(_fromUtf8("actionRASFloodplainDelineation"))
        self.actionLoad_1D_WSEL_from_HDF = QtGui.QAction(RiverGIS)
        self.actionLoad_1D_WSEL_from_HDF.setObjectName(_fromUtf8("actionLoad_1D_WSEL_from_HDF"))
        self.actionRASImportRasData = QtGui.QAction(RiverGIS)
        self.actionRASImportRasData.setIcon(icon4)
        self.actionRASImportRasData.setObjectName(_fromUtf8("actionRASImportRasData"))
        self.actionCreate_1d_PostGIS_Tables = QtGui.QAction(RiverGIS)
        self.actionCreate_1d_PostGIS_Tables.setObjectName(_fromUtf8("actionCreate_1d_PostGIS_Tables"))
        self.actionRASSaveMeshPointsToHECRASGeometry = QtGui.QAction(RiverGIS)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/save2dmeshPtsToGeo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASSaveMeshPointsToHECRASGeometry.setIcon(icon9)
        self.actionRASSaveMeshPointsToHECRASGeometry.setObjectName(_fromUtf8("actionRASSaveMeshPointsToHECRASGeometry"))
        self.actionRASPreview2DMesh = QtGui.QAction(RiverGIS)
        self.actionRASPreview2DMesh.setEnabled(True)
        self.actionRASPreview2DMesh.setObjectName(_fromUtf8("actionRASPreview2DMesh"))
        self.actionRASCreateRdbTables = QtGui.QAction(RiverGIS)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/createPgTables.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASCreateRdbTables.setIcon(icon10)
        self.actionRASCreateRdbTables.setObjectName(_fromUtf8("actionRASCreateRdbTables"))
        self.actionRASManningsNValues = QtGui.QAction(RiverGIS)
        self.actionRASManningsNValues.setObjectName(_fromUtf8("actionRASManningsNValues"))
        self.actionRASExport1DRASData = QtGui.QAction(RiverGIS)
        self.actionRASExport1DRASData.setObjectName(_fromUtf8("actionRASExport1DRASData"))
        self.actionRASTopology1D = QtGui.QAction(RiverGIS)
        self.actionRASTopology1D.setObjectName(_fromUtf8("actionRASTopology1D"))
        self.actionAaa = QtGui.QAction(RiverGIS)
        self.actionAaa.setObjectName(_fromUtf8("actionAaa"))
        self.actionRASLengthsStations = QtGui.QAction(RiverGIS)
        self.actionRASLengthsStations.setObjectName(_fromUtf8("actionRASLengthsStations"))
        self.actionRASCenterlineElevations = QtGui.QAction(RiverGIS)
        self.actionRASCenterlineElevations.setObjectName(_fromUtf8("actionRASCenterlineElevations"))
        self.actionRASStreamCenterlineAll = QtGui.QAction(RiverGIS)
        self.actionRASStreamCenterlineAll.setObjectName(_fromUtf8("actionRASStreamCenterlineAll"))
        self.actionRASXSRiverReachNames = QtGui.QAction(RiverGIS)
        self.actionRASXSRiverReachNames.setObjectName(_fromUtf8("actionRASXSRiverReachNames"))
        self.actionRASXSStationing = QtGui.QAction(RiverGIS)
        self.actionRASXSStationing.setObjectName(_fromUtf8("actionRASXSStationing"))
        self.actionRASXSBankStations = QtGui.QAction(RiverGIS)
        self.actionRASXSBankStations.setObjectName(_fromUtf8("actionRASXSBankStations"))
        self.actionRASXSDownstreamReachLengths = QtGui.QAction(RiverGIS)
        self.actionRASXSDownstreamReachLengths.setObjectName(_fromUtf8("actionRASXSDownstreamReachLengths"))
        self.actionRASXSElevations = QtGui.QAction(RiverGIS)
        self.actionRASXSElevations.setObjectName(_fromUtf8("actionRASXSElevations"))
        self.actionRASXSAll = QtGui.QAction(RiverGIS)
        self.actionRASXSAll.setObjectName(_fromUtf8("actionRASXSAll"))
        self.actionRASImportLayersIntoRdbTables = QtGui.QAction(RiverGIS)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/importLayersIntoRdb.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASImportLayersIntoRdbTables.setIcon(icon11)
        self.actionRASImportLayersIntoRdbTables.setObjectName(_fromUtf8("actionRASImportLayersIntoRdbTables"))
        self.actionRASLevees = QtGui.QAction(RiverGIS)
        self.actionRASLevees.setObjectName(_fromUtf8("actionRASLevees"))
        self.actionRASIneffectiveFlowAreas = QtGui.QAction(RiverGIS)
        self.actionRASIneffectiveFlowAreas.setObjectName(_fromUtf8("actionRASIneffectiveFlowAreas"))
        self.actionRASBlockedObstructions = QtGui.QAction(RiverGIS)
        self.actionRASBlockedObstructions.setObjectName(_fromUtf8("actionRASBlockedObstructions"))
        self.actionRASFlipXSDirection = QtGui.QAction(RiverGIS)
        self.actionRASFlipXSDirection.setObjectName(_fromUtf8("actionRASFlipXSDirection"))
        self.actionRASLoadRdbTablesIntoQGIS = QtGui.QAction(RiverGIS)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/loadRdbTablesIntoQgis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRASLoadRdbTablesIntoQGIS.setIcon(icon12)
        self.actionRASLoadRdbTablesIntoQGIS.setObjectName(_fromUtf8("actionRASLoadRdbTablesIntoQGIS"))
        self.menuHelp.addAction(self.actionHelpContents)
        self.menuRASMapping.addAction(self.actionRASImportRasData)
        self.menuRASMapping.addSeparator()
        self.menuRASMapping.addAction(self.actionRASWaterSurfaceGeneration)
        self.menuRASMapping.addAction(self.actionRASFloodplainDelineation)
        self.menuXS_Cut_Line_Attributes.addAction(self.actionRASXSRiverReachNames)
        self.menuXS_Cut_Line_Attributes.addAction(self.actionRASXSStationing)
        self.menuXS_Cut_Line_Attributes.addAction(self.actionRASXSBankStations)
        self.menuXS_Cut_Line_Attributes.addAction(self.actionRASXSDownstreamReachLengths)
        self.menuXS_Cut_Line_Attributes.addSeparator()
        self.menuXS_Cut_Line_Attributes.addAction(self.actionRASXSElevations)
        self.menuXS_Cut_Line_Attributes.addSeparator()
        self.menuXS_Cut_Line_Attributes.addAction(self.actionRASXSAll)
        self.menuStreamCenterlineAttributes.addAction(self.actionRASTopology1D)
        self.menuStreamCenterlineAttributes.addAction(self.actionRASLengthsStations)
        self.menuStreamCenterlineAttributes.addSeparator()
        self.menuStreamCenterlineAttributes.addAction(self.actionRASCenterlineElevations)
        self.menuStreamCenterlineAttributes.addSeparator()
        self.menuStreamCenterlineAttributes.addAction(self.actionRASStreamCenterlineAll)
        self.menuUtilities.addAction(self.actionRASFlipXSDirection)
        self.menu_Geometry.addAction(self.actionRASCreateRdbTables)
        self.menu_Geometry.addAction(self.actionRASLoadRdbTablesIntoQGIS)
        self.menu_Geometry.addAction(self.actionRASImportLayersIntoRdbTables)
        self.menu_Geometry.addAction(self.menuStreamCenterlineAttributes.menuAction())
        self.menu_Geometry.addAction(self.menuXS_Cut_Line_Attributes.menuAction())
        self.menu_Geometry.addAction(self.actionRASManningsNValues)
        self.menu_Geometry.addAction(self.actionRASLevees)
        self.menu_Geometry.addAction(self.actionRASIneffectiveFlowAreas)
        self.menu_Geometry.addAction(self.actionRASBlockedObstructions)
        self.menu_Geometry.addAction(self.menuUtilities.menuAction())
        self.menu_Geometry.addSeparator()
        self.menu_Geometry.addAction(self.actionRASExport1DRASData)
        self.menu_Geometry.addSeparator()
        self.menu_Geometry.addAction(self.actionRASCreate2dArea)
        self.menu_Geometry.addAction(self.actionRASPreview2DMesh)
        self.menu_Geometry.addAction(self.actionRASSaveMeshPointsToHECRASGeometry)
        self.menu_Geometry.addAction(self.actionRASCorrectLateralWeirs)
        self.menu_Geometry.addSeparator()
        self.menuDB.addAction(self.actionRefreshConnections)
        self.menuDB.addAction(self.actionImportRiverFromIsokp)
        self.menubar.addAction(self.menuDB.menuAction())
        self.menubar.addAction(self.menu_Geometry.menuAction())
        self.menubar.addAction(self.menuRASMapping.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RiverGIS)
        QtCore.QMetaObject.connectSlotsByName(RiverGIS)

    def retranslateUi(self, RiverGIS):
        RiverGIS.setWindowTitle(_translate("RiverGIS", "RiverGIS", None))
        self.labelCurSchema.setText(_translate("RiverGIS", "Schema:", None))
        self.labelCurDatabase.setText(_translate("RiverGIS", "DB Connection:", None))
        self.label.setText(_translate("RiverGIS", "Projection", None))
        self.menuHelp.setTitle(_translate("RiverGIS", "Help", None))
        self.menuRASMapping.setTitle(_translate("RiverGIS", "RAS Mapping", None))
        self.menu_Geometry.setTitle(_translate("RiverGIS", "RAS Geometry", None))
        self.menuXS_Cut_Line_Attributes.setTitle(_translate("RiverGIS", "XS Cut Line Attributes", None))
        self.menuStreamCenterlineAttributes.setTitle(_translate("RiverGIS", "Stream Centerline Attributes", None))
        self.menuUtilities.setTitle(_translate("RiverGIS", "Utilities", None))
        self.menuDB.setTitle(_translate("RiverGIS", "Database", None))
        self.actionCreate2dAreaPerimeter.setText(_translate("RiverGIS", "2D Area (Perimeter)", None))
        self.actionRASCorrectLateralWeirs.setText(_translate("RiverGIS", "Correct Lateral Weirs", None))
        self.actionRASCreate2dArea.setText(_translate("RiverGIS", "Create 2D Flow Areas", None))
        self.actionAbout.setText(_translate("RiverGIS", "About", None))
        self.actionHelpContents.setText(_translate("RiverGIS", "Contents", None))
        self.actionLoad_2D_WSEL_from_HDF.setText(_translate("RiverGIS", "Load 2D WSEL from HDF", None))
        self.actionRASWaterSurfaceGeneration.setText(_translate("RiverGIS", "Water Surface Generation", None))
        self.actionImportRiverFromIsokp.setText(_translate("RiverGIS", "Import River Data From ISOKP Database", None))
        self.actionRefreshConnections.setText(_translate("RiverGIS", "Refresh Connections List", None))
        self.actionRASFloodplainDelineation.setText(_translate("RiverGIS", "Floodplain Delineation Using Rasters", None))
        self.actionLoad_1D_WSEL_from_HDF.setText(_translate("RiverGIS", "Load 1D WSEL from HDF", None))
        self.actionRASImportRasData.setText(_translate("RiverGIS", "Import RAS Data", None))
        self.actionCreate_1d_PostGIS_Tables.setText(_translate("RiverGIS", "Create 1D PostGIS Tables", None))
        self.actionRASSaveMeshPointsToHECRASGeometry.setText(_translate("RiverGIS", "Save mesh points to HEC-RAS geometry file", None))
        self.actionRASPreview2DMesh.setText(_translate("RiverGIS", "Preview 2D Mesh", None))
        self.actionRASCreateRdbTables.setText(_translate("RiverGIS", "Create River Database Tables", None))
        self.actionRASManningsNValues.setText(_translate("RiverGIS", "Extract Manning\'s n Values", None))
        self.actionRASExport1DRASData.setText(_translate("RiverGIS", "Export 1D RAS Data", None))
        self.actionRASTopology1D.setText(_translate("RiverGIS", "Topology", None))
        self.actionAaa.setText(_translate("RiverGIS", "aaa", None))
        self.actionRASLengthsStations.setText(_translate("RiverGIS", "Lengths/Stations", None))
        self.actionRASCenterlineElevations.setText(_translate("RiverGIS", "Elevations", None))
        self.actionRASStreamCenterlineAll.setText(_translate("RiverGIS", "All", None))
        self.actionRASXSRiverReachNames.setText(_translate("RiverGIS", "River/Reach Names", None))
        self.actionRASXSStationing.setText(_translate("RiverGIS", "Stationing", None))
        self.actionRASXSBankStations.setText(_translate("RiverGIS", "Bank Stations", None))
        self.actionRASXSDownstreamReachLengths.setText(_translate("RiverGIS", "Downstream Reach Lengths", None))
        self.actionRASXSElevations.setText(_translate("RiverGIS", "Elevations", None))
        self.actionRASXSAll.setText(_translate("RiverGIS", "All", None))
        self.actionRASImportLayersIntoRdbTables.setText(_translate("RiverGIS", "Import Layers Into River Database Tables", None))
        self.actionRASLevees.setText(_translate("RiverGIS", "Levees", None))
        self.actionRASIneffectiveFlowAreas.setText(_translate("RiverGIS", "Ineffective Flow Areas", None))
        self.actionRASBlockedObstructions.setText(_translate("RiverGIS", "Blocked Obstructions", None))
        self.actionRASFlipXSDirection.setText(_translate("RiverGIS", "Flip Cross Sections", None))
        self.actionRASLoadRdbTablesIntoQGIS.setText(_translate("RiverGIS", "Load River Database Tables Into QGIS", None))

from qgsprojectionselectionwidget import QgsProjectionSelectionWidget
import resources_rc
