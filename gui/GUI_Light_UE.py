# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Light_UE.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1100, 830))
        self.widget.setStyleSheet("QPushButton#Browse_btn_1{\n"
"    background-color:  #000000;\n"
"    color:#fff;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Browse_btn_1:hover{\n"
"    background-color: #1c1f23;\n"
"}\n"
"\n"
"QPushButton#Browse_btn_1:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#0e1856;\n"
"}\n"
"\n"
"QPushButton#Browse_btn_2{\n"
"    background-color:  #000000;\n"
"    color:#fff;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Browse_btn_2:hover{\n"
"    background-color: #1c1f23;\n"
"}\n"
"\n"
"QPushButton#Browse_btn_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#0e1856;\n"
"}\n"
"\n"
"QPushButton#SetSettings_btn{\n"
"    background-color:  #000000;\n"
"    color:#fff;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#SetSettings_btn:hover{\n"
"    background-color: #1c1f23;\n"
"}\n"
"\n"
"QPushButton#SetSettings_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#0e1856;\n"
"}\n"
"\n"
"QPushButton#Start_RL_btn{\n"
"    background-color:  #000000;\n"
"    color:#fff;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#Start_RL_btn:hover{\n"
"    background-color: #1c1f23;\n"
"}\n"
"\n"
"QPushButton#Start_RL_btn:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:#0e1856;\n"
"}")
        self.widget.setObjectName("widget")
        self.Background_Rechts = QtWidgets.QLabel(self.widget)
        self.Background_Rechts.setGeometry(QtCore.QRect(450, 0, 650, 850))
        self.Background_Rechts.setStyleSheet("background-color:#FAFAFA;")
        self.Background_Rechts.setText("")
        self.Background_Rechts.setObjectName("Background_Rechts")
        self.Meshes_Distances = QtWidgets.QLabel(self.widget)
        self.Meshes_Distances.setGeometry(QtCore.QRect(510, 50, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Meshes_Distances.setFont(font)
        self.Meshes_Distances.setStyleSheet("color: #000000;")
        self.Meshes_Distances.setObjectName("Meshes_Distances")
        self.Min_Distance = QtWidgets.QLineEdit(self.widget)
        self.Min_Distance.setGeometry(QtCore.QRect(510, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Min_Distance.setFont(font)
        self.Min_Distance.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Min_Distance.setObjectName("Min_Distance")
        self.Max_Distance = QtWidgets.QLineEdit(self.widget)
        self.Max_Distance.setGeometry(QtCore.QRect(700, 110, 171, 31))
        self.Max_Distance.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Max_Distance.setObjectName("Max_Distance")
        self.Step_Distance = QtWidgets.QLineEdit(self.widget)
        self.Step_Distance.setGeometry(QtCore.QRect(890, 110, 171, 31))
        self.Step_Distance.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Step_Distance.setObjectName("Step_Distance")
        self.Light_Distributions = QtWidgets.QLabel(self.widget)
        self.Light_Distributions.setGeometry(QtCore.QRect(510, 190, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Light_Distributions.setFont(font)
        self.Light_Distributions.setStyleSheet("color:#000000;")
        self.Light_Distributions.setObjectName("Light_Distributions")
        self.Right_Light = QtWidgets.QLineEdit(self.widget)
        self.Right_Light.setGeometry(QtCore.QRect(510, 250, 421, 41))
        self.Right_Light.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Right_Light.setObjectName("Right_Light")
        self.Left_Light = QtWidgets.QLineEdit(self.widget)
        self.Left_Light.setGeometry(QtCore.QRect(510, 320, 421, 41))
        self.Left_Light.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Left_Light.setObjectName("Left_Light")
        self.Browse_btn_1 = QtWidgets.QPushButton(self.widget)
        self.Browse_btn_1.setGeometry(QtCore.QRect(950, 250, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Browse_btn_1.setFont(font)
        self.Browse_btn_1.setObjectName("Browse_btn_1")
        self.Browse_btn_2 = QtWidgets.QPushButton(self.widget)
        self.Browse_btn_2.setGeometry(QtCore.QRect(950, 320, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Browse_btn_2.setFont(font)
        self.Browse_btn_2.setObjectName("Browse_btn_2")
        self.Detection_Objects = QtWidgets.QLabel(self.widget)
        self.Detection_Objects.setGeometry(QtCore.QRect(510, 400, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Detection_Objects.setFont(font)
        self.Detection_Objects.setStyleSheet("color:#000000;")
        self.Detection_Objects.setObjectName("Detection_Objects")
        self.Assets_Folder = QtWidgets.QLineEdit(self.widget)
        self.Assets_Folder.setGeometry(QtCore.QRect(510, 460, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Assets_Folder.setFont(font)
        self.Assets_Folder.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Assets_Folder.setObjectName("Assets_Folder")
        self.Substring_Detection = QtWidgets.QLineEdit(self.widget)
        self.Substring_Detection.setGeometry(QtCore.QRect(510, 520, 551, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.Substring_Detection.setFont(font)
        self.Substring_Detection.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Substring_Detection.setObjectName("Substring_Detection")
        self.Render_Settings = QtWidgets.QLabel(self.widget)
        self.Render_Settings.setGeometry(QtCore.QRect(510, 600, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Render_Settings.setFont(font)
        self.Render_Settings.setStyleSheet("color:#000000;")
        self.Render_Settings.setObjectName("Render_Settings")
        self.Resolution_X = QtWidgets.QLineEdit(self.widget)
        self.Resolution_X.setGeometry(QtCore.QRect(510, 660, 271, 31))
        self.Resolution_X.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Resolution_X.setObjectName("Resolution_X")
        self.Resolution_Y = QtWidgets.QLineEdit(self.widget)
        self.Resolution_Y.setGeometry(QtCore.QRect(790, 660, 271, 31))
        self.Resolution_Y.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid #000000;\n"
"color:#000000;\n"
"font: 25 12pt \"Roboto\";\n"
"padding-bottom:7px;\n"
"\n"
"")
        self.Resolution_Y.setObjectName("Resolution_Y")
        self.SetSettings_btn = QtWidgets.QPushButton(self.widget)
        self.SetSettings_btn.setGeometry(QtCore.QRect(510, 740, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.SetSettings_btn.setFont(font)
        self.SetSettings_btn.setObjectName("SetSettings_btn")
        self.Background_Left = QtWidgets.QLabel(self.widget)
        self.Background_Left.setGeometry(QtCore.QRect(0, 0, 451, 850))
        self.Background_Left.setStyleSheet("background-image: url(:/image/Background.png);")
        self.Background_Left.setText("")
        self.Background_Left.setPixmap(QtGui.QPixmap(":/image/Background.png"))
        self.Background_Left.setScaledContents(True)
        self.Background_Left.setObjectName("Background_Left")
        self.iPeG_logo = QtWidgets.QLabel(self.widget)
        self.iPeG_logo.setGeometry(QtCore.QRect(110, 750, 231, 51))
        self.iPeG_logo.setStyleSheet("")
        self.iPeG_logo.setText("")
        self.iPeG_logo.setPixmap(QtGui.QPixmap(":/image/IPeG_Logo.png"))
        self.iPeG_logo.setScaledContents(True)
        self.iPeG_logo.setObjectName("iPeG_logo")
        self.Start_RL_btn = QtWidgets.QPushButton(self.widget)
        self.Start_RL_btn.setGeometry(QtCore.QRect(800, 740, 281, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Start_RL_btn.setFont(font)
        self.Start_RL_btn.setObjectName("Start_RL_btn")
        self.Background_Rechts.raise_()
        self.Background_Left.raise_()
        self.SetSettings_btn.raise_()
        self.iPeG_logo.raise_()
        self.Min_Distance.raise_()
        self.Meshes_Distances.raise_()
        self.Step_Distance.raise_()
        self.Max_Distance.raise_()
        self.Light_Distributions.raise_()
        self.Browse_btn_2.raise_()
        self.Left_Light.raise_()
        self.Browse_btn_1.raise_()
        self.Right_Light.raise_()
        self.Detection_Objects.raise_()
        self.Assets_Folder.raise_()
        self.Substring_Detection.raise_()
        self.Resolution_Y.raise_()
        self.Resolution_X.raise_()
        self.Render_Settings.raise_()
        self.Start_RL_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Meshes_Distances.setText(_translate("MainWindow", "Meshes distances:"))
        self.Min_Distance.setPlaceholderText(_translate("MainWindow", "Min Distance"))
        self.Max_Distance.setPlaceholderText(_translate("MainWindow", "Max Distance"))
        self.Step_Distance.setPlaceholderText(_translate("MainWindow", "Step Distance"))
        self.Light_Distributions.setText(_translate("MainWindow", "Light distributions:"))
        self.Right_Light.setPlaceholderText(_translate("MainWindow", "Choose the right light distribution..."))
        self.Left_Light.setPlaceholderText(_translate("MainWindow", "Choose the left light distribution..."))
        self.Browse_btn_1.setText(_translate("MainWindow", "Browse"))
        self.Browse_btn_2.setText(_translate("MainWindow", "Browse"))
        self.Detection_Objects.setText(_translate("MainWindow", "Object detection:"))
        self.Assets_Folder.setPlaceholderText(_translate("MainWindow", "Choose the assets folder... (/Game/Detektionsobjekte)"))
        self.Substring_Detection.setPlaceholderText(_translate("MainWindow", "Choose the substring of the detection objects (Puppe)"))
        self.Render_Settings.setText(_translate("MainWindow", "Render settings:"))
        self.Resolution_X.setPlaceholderText(_translate("MainWindow", "Output Resolution X..."))
        self.Resolution_Y.setPlaceholderText(_translate("MainWindow", "Output Resolution Y..."))
        self.SetSettings_btn.setText(_translate("MainWindow", "SET SETTINGS"))
        self.Start_RL_btn.setText(_translate("MainWindow", "START RL"))
import res
