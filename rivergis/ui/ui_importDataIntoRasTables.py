# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_importDataIntoRasTables.ui'
#
# Created: Mon Sep 14 18:08:51 2015
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

class Ui_importDataIntoRasTables(object):
    def setupUi(self, importDataIntoRasTables):
        importDataIntoRasTables.setObjectName(_fromUtf8("importDataIntoRasTables"))
        importDataIntoRasTables.resize(346, 470)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(importDataIntoRasTables.sizePolicy().hasHeightForWidth())
        importDataIntoRasTables.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(importDataIntoRasTables)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(importDataIntoRasTables)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.cboRivers = QtGui.QComboBox(importDataIntoRasTables)
        self.cboRivers.setObjectName(_fromUtf8("cboRivers"))
        self.verticalLayout.addWidget(self.cboRivers)
        self.label_2 = QtGui.QLabel(importDataIntoRasTables)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.cboXsecs = QtGui.QComboBox(importDataIntoRasTables)
        self.cboXsecs.setObjectName(_fromUtf8("cboXsecs"))
        self.verticalLayout.addWidget(self.cboXsecs)
        self.label_4 = QtGui.QLabel(importDataIntoRasTables)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.cboBanks = QtGui.QComboBox(importDataIntoRasTables)
        self.cboBanks.setObjectName(_fromUtf8("cboBanks"))
        self.verticalLayout.addWidget(self.cboBanks)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_9 = QtGui.QLabel(importDataIntoRasTables)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_2.addWidget(self.label_9)
        self.cboBanklineType = QtGui.QComboBox(importDataIntoRasTables)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboBanklineType.sizePolicy().hasHeightForWidth())
        self.cboBanklineType.setSizePolicy(sizePolicy)
        self.cboBanklineType.setObjectName(_fromUtf8("cboBanklineType"))
        self.horizontalLayout_2.addWidget(self.cboBanklineType)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_7 = QtGui.QLabel(importDataIntoRasTables)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.cboFlowPaths = QtGui.QComboBox(importDataIntoRasTables)
        self.cboFlowPaths.setObjectName(_fromUtf8("cboFlowPaths"))
        self.verticalLayout.addWidget(self.cboFlowPaths)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_8 = QtGui.QLabel(importDataIntoRasTables)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.cboFlowpathType = QtGui.QComboBox(importDataIntoRasTables)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFlowpathType.sizePolicy().hasHeightForWidth())
        self.cboFlowpathType.setSizePolicy(sizePolicy)
        self.cboFlowpathType.setMinimumSize(QtCore.QSize(0, 0))
        self.cboFlowpathType.setObjectName(_fromUtf8("cboFlowpathType"))
        self.horizontalLayout.addWidget(self.cboFlowpathType)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtGui.QLabel(importDataIntoRasTables)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.cboLevees = QtGui.QComboBox(importDataIntoRasTables)
        self.cboLevees.setObjectName(_fromUtf8("cboLevees"))
        self.verticalLayout.addWidget(self.cboLevees)
        self.label_5 = QtGui.QLabel(importDataIntoRasTables)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.cboIneffective = QtGui.QComboBox(importDataIntoRasTables)
        self.cboIneffective.setObjectName(_fromUtf8("cboIneffective"))
        self.verticalLayout.addWidget(self.cboIneffective)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_10 = QtGui.QLabel(importDataIntoRasTables)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_3.addWidget(self.label_10)
        self.cboIneffElev = QtGui.QComboBox(importDataIntoRasTables)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboIneffElev.sizePolicy().hasHeightForWidth())
        self.cboIneffElev.setSizePolicy(sizePolicy)
        self.cboIneffElev.setObjectName(_fromUtf8("cboIneffElev"))
        self.horizontalLayout_3.addWidget(self.cboIneffElev)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_6 = QtGui.QLabel(importDataIntoRasTables)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.cboObstructions = QtGui.QComboBox(importDataIntoRasTables)
        self.cboObstructions.setObjectName(_fromUtf8("cboObstructions"))
        self.verticalLayout.addWidget(self.cboObstructions)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_11 = QtGui.QLabel(importDataIntoRasTables)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_4.addWidget(self.label_11)
        self.cboObstructionsElev = QtGui.QComboBox(importDataIntoRasTables)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboObstructionsElev.sizePolicy().hasHeightForWidth())
        self.cboObstructionsElev.setSizePolicy(sizePolicy)
        self.cboObstructionsElev.setObjectName(_fromUtf8("cboObstructionsElev"))
        self.horizontalLayout_4.addWidget(self.cboObstructionsElev)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtGui.QDialogButtonBox(importDataIntoRasTables)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(importDataIntoRasTables)
        QtCore.QMetaObject.connectSlotsByName(importDataIntoRasTables)

    def retranslateUi(self, importDataIntoRasTables):
        importDataIntoRasTables.setWindowTitle(_translate("importDataIntoRasTables", "Import Data Into RAS PostGIS Tables", None))
        self.label.setText(_translate("importDataIntoRasTables", "Rivers Layer", None))
        self.label_2.setText(_translate("importDataIntoRasTables", "Cross-sections Layer", None))
        self.label_4.setText(_translate("importDataIntoRasTables", "Banks Layer", None))
        self.label_9.setText(_translate("importDataIntoRasTables", "Type attribute", None))
        self.label_7.setText(_translate("importDataIntoRasTables", "Flow Paths Layer", None))
        self.label_8.setText(_translate("importDataIntoRasTables", "Type attribute", None))
        self.label_3.setText(_translate("importDataIntoRasTables", "Levees Layer", None))
        self.label_5.setText(_translate("importDataIntoRasTables", "Ineffective Flow Areas Layer", None))
        self.label_10.setText(_translate("importDataIntoRasTables", "Elevation attribute", None))
        self.label_6.setText(_translate("importDataIntoRasTables", "Blocked Obstructions Layer", None))
        self.label_11.setText(_translate("importDataIntoRasTables", "Elevation attribute", None))

