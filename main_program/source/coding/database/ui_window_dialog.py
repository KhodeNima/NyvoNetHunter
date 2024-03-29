#!/usr/bin/env python3
"""
The Graphical User Interface window skeleton class.
"""


def setup_database_import_path() -> None:
    from sys import path as module_paths
    import pathlib

    project_root_directory = pathlib.Path.cwd()

    module_paths.append(f"{project_root_directory}/main_program/source/coding")
    module_paths.append(f"{project_root_directory}/main_program/source/coding/database")


setup_database_import_path()

from data import DirectRunError
from packages import (
    QtWebEngineWidgets,
    QSizePolicy,
    QtWidgets,
    QtCore,
    QIcon,
    QtGui,
    Path,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1192, 685)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        Dialog.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("main_program/source/ui_design/resources/pictures/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowOpacity(5.0)
        self.searchButton = QtWidgets.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(430, 530, 211, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.searchButton.setFont(font)
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchButton.setWhatsThis("")
        self.searchButton.setStyleSheet("QPushButton { border: 2px solid white; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)) }\n"
"\n"
"QPushButton:hover{\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("main_program/source/ui_design/../../../../../../.designer/backup/resources/pictures/pushbuttonicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QtCore.QSize(35, 35))
        self.searchButton.setDefault(False)
        self.searchButton.setFlat(True)
        self.searchButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 490, 561, 31))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit { border: 2px solid white; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));  }\n"
"\n"
"QLineEdit:hover{\n"
"        background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLineEdit {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:on {\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.lineEdit.setMaxLength(50)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(250, 180, 561, 301))
        self.graphicsView.setStyleSheet("QGraphicsView { border: 2px solid white; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));  }\n"
"\n"
"QLineEdit:hover{\n"
"        background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLineEdit {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:on {\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.graphicsView.setObjectName("graphicsView")
        self.responseLabel = QtWidgets.QLabel(Dialog)
        self.responseLabel.setGeometry(QtCore.QRect(280, 190, 501, 281))
        self.responseLabel.setText("")
        self.responseLabel.setObjectName("responseLabel")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView_2.setGeometry(QtCore.QRect(50, 180, 191, 301))
        self.graphicsView_2.setStyleSheet("QGraphicsView { border: 2px solid white; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));  }\n"
"\n"
"QLineEdit:hover{\n"
"        background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLineEdit {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:on {\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QGraphicsView:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.countryCheckBox = QtWidgets.QCheckBox(Dialog)
        self.countryCheckBox.setGeometry(QtCore.QRect(60, 200, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.countryCheckBox.setFont(font)
        self.countryCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.countryCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.countryCheckBox.setObjectName("countryCheckBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 140, 191, 31))
        self.label_3.setStyleSheet("QLabel{ border: 2px solid white; background-color: qlineargradient(spread:reflect, x1:0.00947867, y1:1, x2:0.838863, y2:0.222, stop:0.0663507 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QLabel:hover{\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLabel {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.regionCheckBox = QtWidgets.QCheckBox(Dialog)
        self.regionCheckBox.setGeometry(QtCore.QRect(60, 220, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.regionCheckBox.setFont(font)
        self.regionCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.regionCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.regionCheckBox.setObjectName("regionCheckBox")
        self.cityCheckBox = QtWidgets.QCheckBox(Dialog)
        self.cityCheckBox.setGeometry(QtCore.QRect(60, 240, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cityCheckBox.setFont(font)
        self.cityCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cityCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.cityCheckBox.setObjectName("cityCheckBox")
        self.zipcodeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.zipcodeCheckBox.setGeometry(QtCore.QRect(60, 260, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.zipcodeCheckBox.setFont(font)
        self.zipcodeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zipcodeCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.zipcodeCheckBox.setObjectName("zipcodeCheckBox")
        self.timezoneCheckBox = QtWidgets.QCheckBox(Dialog)
        self.timezoneCheckBox.setGeometry(QtCore.QRect(60, 280, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timezoneCheckBox.setFont(font)
        self.timezoneCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timezoneCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.timezoneCheckBox.setObjectName("timezoneCheckBox")
        self.ispCheckBox = QtWidgets.QCheckBox(Dialog)
        self.ispCheckBox.setGeometry(QtCore.QRect(60, 300, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ispCheckBox.setFont(font)
        self.ispCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ispCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.ispCheckBox.setObjectName("ispCheckBox")
        self.latitudeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.latitudeCheckBox.setGeometry(QtCore.QRect(60, 330, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.latitudeCheckBox.setFont(font)
        self.latitudeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.latitudeCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.latitudeCheckBox.setObjectName("latitudeCheckBox")
        self.longitudeCheckBox = QtWidgets.QCheckBox(Dialog)
        self.longitudeCheckBox.setGeometry(QtCore.QRect(60, 350, 131, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.longitudeCheckBox.setFont(font)
        self.longitudeCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.longitudeCheckBox.setStyleSheet("QCheckBox {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  cursor: pointer;\n"
"  margin-right: -22px;\n"
"  appearance: none;\n"
"  border-radius: 5px;\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 76, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   : 2;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
".container {\n"
"  width: 35px;\n"
"  height: 35px;\n"
"  position: relative;\n"
"  top: 4px;\n"
"  left: -8%;\n"
"  border-radius: 5px;\n"
"  background-color: #6593cf;\n"
"   : all 0.3s;\n"
"}\n"
"\n"
"QCheckBox::before {\n"
"  content: \"\";\n"
"  background-color: #6593cf;\n"
"  position: relative;\n"
"  display: flex;\n"
"  top: 45%;\n"
"  left: 50%;\n"
"  width: 55px;\n"
"  height: 3px;\n"
"  border-radius: 25px;\n"
"  : translate(100px, 0px) scale(0);\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QCheckBox:checked::before {\n"
"  : translateX(2em);\n"
"  top: 12px;\n"
"   : ease-out 0.15s;\n"
"}\n"
"\n"
"QcheckBox:hover {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
"QCheckBox:checked {\n"
"  : translate(4px, 4px);\n"
"   : ease-out 0.15s;\n"
"  background-color: #6593cf;\n"
"}\n"
"\n"
".svg-icon {\n"
"  position: absolute;\n"
"  width: 25px;\n"
"  height: 25px;\n"
"  display: flex;\n"
"   : 3;\n"
"  top: 35%;\n"
"  left: 11%;\n"
"  color: #fefefe;\n"
"  font-family: \"Gill Sans\", \"Gill Sans MT\", Calibri, \"Trebuchet MS\", sans-serif;\n"
"  : rotate(0deg) scale(0);\n"
"   : ease-in 0.2s;\n"
"}\n"
"\n"
"QCheckBoxchecked ~ .svg-icon {\n"
"  : rotate(360deg) scale(1);\n"
"   : ease-in 0.2s;\n"
"}\n"
"")
        self.longitudeCheckBox.setObjectName("longitudeCheckBox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 10, 191, 31))
        self.label_4.setStyleSheet("QLabel{ border: 2px solid white; background-color: qlineargradient(spread:reflect, x1:0.00947867, y1:1, x2:0.838863, y2:0.222, stop:0.0663507 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QLabel:hover{\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLabel {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QLabel:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.connection_status_label = QtWidgets.QLabel(Dialog)
        self.connection_status_label.setGeometry(QtCore.QRect(50, 50, 191, 81))
        self.connection_status_label.setText("")
        self.connection_status_label.setObjectName("connection_status_label")
        self.webView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webView.setGeometry(QtCore.QRect(820, 180, 300, 301))
        self.webView.setStyleSheet("QWebView{ border: 2px solid red; background-color: orange }\n"
"\n"
"QWebView:hover{\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #ffd9aa,\n"
"                stop :   0.5 #ffbb6e, stop :   0.55 #feae42, stop :   1.0 #fedb74);\n"
"}\n"
"\n"
"QWebView {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #f5f9ff,\n"
"                stop :   0.5 #c7dfff, stop :   0.55 #afd2ff, stop :   1.0 #c0dbff);\n"
"        color: #006aff;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QWebView:pressed {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #c0dbff,\n"
"        stop :   0.5 #cfd26f, stop :   0.55 #c7df6f, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QWebView:on {\n"
"        background: qlineargradient(x1 : 0, y1 : 0, x2 : 0, y2 :   1, stop :   0.0 #5AA72D,\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QWebView:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: black;\n"
"}\n"
"")


        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(250, 140, 561, 31))
        self.progressBar.setFormat("                               %p%")
        self.progressBar.setStyleSheet("QProgressBar { border: 2px solid black; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));  }\n"
"QProgrssBar {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        color: black; \n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"QProgrssBar:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar:on {\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QProgressBar:disabled {\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"}\n"
"QProgressBar:chunk {\n"
"        background-color: #ffffff;\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar_2")
        self.copyButton = QtWidgets.QPushButton(Dialog)
        self.copyButton.setGeometry(QtCore.QRect(820, 487, 301, 31))
        self.copyButton.setObjectName("copyButton")
        self.callstatusLabel = QtWidgets.QLabel(Dialog)
        self.callstatusLabel.setGeometry(QtCore.QRect(450, 50, 161, 81))
        self.callstatusLabel.setText("")
        self.callstatusLabel.setObjectName("callstatusLabel")
        

        self.copyButton.setStyleSheet("QPushButton { border: 2px solid white; background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255)) }\n"
"\n"
"QPushButton:hover{\n"
"}\n"
"\n"
"QPushButton {\n"
"        border: 1px solid #6593cf;\n"
"        border-radius: 2px;\n"
"        padding: 5px 15px 2px 5px;\n"
"        color: #000000;\n"
"        font: bold large \"Arial\";\n"
"        height: 30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"        color: #000000; \n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton:on {\n"
"        stop :   0.5 #B3E296, stop :   0.55 #B3E296, stop :   1.0 #f5f9ff);\n"
"        padding-top: 2px;\n"
"        padding-left: 3px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"        background: transparent #e5e9ee;\n"
"        padding-top: 2px;        \n"
"        padding-left: 3px;\n"
"        color: #000000;\n"
"}")
        self.copyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.no_connection_movie = QtGui.QMovie("main_program/source/ui_design/resources/gifs/no_connection.gif")
        self.no_connection_movie.setScaledSize(QtCore.QSize(self.connection_status_label.width(), self.connection_status_label.height()))

        self.connected_movie = QtGui.QMovie("main_program/source/ui_design/resources/gifs/connected.gif")
        self.connected_movie.setScaledSize(QtCore.QSize(self.connection_status_label.width(), self.connection_status_label.height()))

        self.examining_movie = QtGui.QMovie("main_program/source/ui_design/resources/gifs/examining.gif")
        self.examining_movie.setScaledSize(QtCore.QSize(self.callstatusLabel.width(), self.callstatusLabel.height()))

        self.awaiting_icon = QtGui.QPixmap("main_program/source/ui_design/resources/pictures/awaiting.png")
        self.awaiting_icon = self.awaiting_icon.scaled(self.callstatusLabel.width(), self.callstatusLabel.height())

        self.webviewSettings = self.webView.settings()
        self.webviewSettings.setAttribute(QtWebEngineWidgets.QWebEngineSettings.WebAttribute.JavascriptEnabled, True)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NyvoNetHunter"))
        self.searchButton.setToolTip(_translate("Dialog", "<html><head/><body><p>Examine the ENDPOINT!</p></body></html>"))
        self.searchButton.setText(_translate("Dialog", "Examine"))
        self.lineEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>IP example: <span style=\" font-style:italic; text-decoration: underline;\">144.145.146.147</span><span style=\" font-weight:400;\">. </span>( IP addresses maximum octet digit is 255 )</p><p>URL example: <span style=\" font-style:italic; text-decoration: underline;\">https://github.com</span> OR <span style=\" font-style:italic; text-decoration: underline;\">https://discord.com</span><span style=\" font-weight:400;\">.</span></p><p><br/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter your desired IP or URL to examine: "))
        self.graphicsView.setToolTip(_translate("Dialog", "<html><head/><body><p>The examine operation outputs will be shown <span style=\" font-style:italic; text-decoration: underline;\">here.</span></p></body></html>"))
        self.graphicsView_2.setToolTip(_translate("Dialog", "<html><head/><body><p>The examine operation outputs will be shown <span style=\" font-style:italic; text-decoration: underline;\">here.</span></p></body></html>"))
        self.countryCheckBox.setText(_translate("Dialog", "Country"))
        self.label_3.setText(_translate("Dialog", "Examine options"))
        self.regionCheckBox.setText(_translate("Dialog", "Region"))
        self.cityCheckBox.setText(_translate("Dialog", "City"))
        self.zipcodeCheckBox.setText(_translate("Dialog", "Zip code"))
        self.timezoneCheckBox.setText(_translate("Dialog", "Time zone"))
        self.ispCheckBox.setToolTip(_translate("Dialog", "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>"))
        self.ispCheckBox.setText(_translate("Dialog", "ISP"))
        self.latitudeCheckBox.setToolTip(_translate("Dialog", "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>"))
        self.latitudeCheckBox.setText(_translate("Dialog", "latitude"))
        self.longitudeCheckBox.setToolTip(_translate("Dialog", "<html><head/><body><p>The IP user Internet Service Provider.</p><p><br/></p><p>Examples: Mobin Net Communication Company, SURFnet II c.</p></body></html>"))
        self.longitudeCheckBox.setText(_translate("Dialog", "Longitude"))
        self.label_4.setText(_translate("Dialog", "Connection Status"))
        self.copyButton.setText(_translate("Dialog", "copy"))
