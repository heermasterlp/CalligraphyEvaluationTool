# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smoothmanuallymainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 181, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_btn.setObjectName("open_btn")
        self.verticalLayout.addWidget(self.open_btn)
        self.clear_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout.addWidget(self.clear_btn)
        self.contour_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.contour_btn.setObjectName("contour_btn")
        self.verticalLayout.addWidget(self.contour_btn)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.maxerror_ledit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.maxerror_ledit.setObjectName("maxerror_ledit")
        self.horizontalLayout.addWidget(self.maxerror_ledit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.smooth_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.smooth_btn.setObjectName("smooth_btn")
        self.verticalLayout.addWidget(self.smooth_btn)
        self.autosmooth_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.autosmooth_btn.setObjectName("autosmooth_btn")
        self.verticalLayout.addWidget(self.autosmooth_btn)
        self.save_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)
        self.exit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exit_btn.setObjectName("exit_btn")
        self.verticalLayout.addWidget(self.exit_btn)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(220, 10, 801, 611))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 609))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.contour_gview = QtWidgets.QGraphicsView(self.scrollAreaWidgetContents)
        self.contour_gview.setGeometry(QtCore.QRect(0, 0, 801, 611))
        self.contour_gview.setObjectName("contour_gview")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_btn.setText(_translate("MainWindow", "Open"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.contour_btn.setText(_translate("MainWindow", "Contour"))
        self.label.setText(_translate("MainWindow", "Max Error:"))
        self.maxerror_ledit.setPlaceholderText(_translate("MainWindow", "0"))
        self.smooth_btn.setText(_translate("MainWindow", "Smooth"))
        self.autosmooth_btn.setText(_translate("MainWindow", "Auto-Smooth"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))

