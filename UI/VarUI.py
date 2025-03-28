# Form implementation generated from reading ui file 'VarUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1694, 930)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.start_pushButton.setGeometry(QtCore.QRect(50, 30, 75, 23))
        self.start_pushButton.setObjectName("start_pushButton")
        self.stop_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.stop_pushButton.setGeometry(QtCore.QRect(50, 60, 75, 23))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.fps_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.fps_textEdit.setGeometry(QtCore.QRect(290, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fps_textEdit.setFont(font)
        self.fps_textEdit.setObjectName("fps_textEdit")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(210, 120, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.fps_repetition_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.fps_repetition_textEdit.setGeometry(QtCore.QRect(290, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fps_repetition_textEdit.setFont(font)
        self.fps_repetition_textEdit.setObjectName("fps_repetition_textEdit")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(210, 140, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.initFrame_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.initFrame_label.setGeometry(QtCore.QRect(40, 180, 721, 701))
        self.initFrame_label.setAutoFillBackground(True)
        self.initFrame_label.setText("")
        self.initFrame_label.setObjectName("initFrame_label")
        self.checkBox_plot_video = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_plot_video.setGeometry(QtCore.QRect(210, 20, 131, 23))
        self.checkBox_plot_video.setObjectName("checkBox_plot_video")
        self.brightness_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.brightness_pushButton.setGeometry(QtCore.QRect(620, 70, 121, 23))
        self.brightness_pushButton.setObjectName("brightness_pushButton")
        self.brightness_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.brightness_textEdit.setGeometry(QtCore.QRect(760, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brightness_textEdit.setFont(font)
        self.brightness_textEdit.setObjectName("brightness_textEdit")
        self.contrast_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.contrast_pushButton.setGeometry(QtCore.QRect(620, 100, 121, 23))
        self.contrast_pushButton.setObjectName("contrast_pushButton")
        self.contrast_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.contrast_textEdit.setGeometry(QtCore.QRect(760, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrast_textEdit.setFont(font)
        self.contrast_textEdit.setObjectName("contrast_textEdit")
        self.initFrame2_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.initFrame2_label.setGeometry(QtCore.QRect(800, 190, 721, 691))
        self.initFrame2_label.setAutoFillBackground(True)
        self.initFrame2_label.setText("")
        self.initFrame2_label.setObjectName("initFrame2_label")
        self.folder_name_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.folder_name_textEdit.setGeometry(QtCore.QRect(500, 20, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.folder_name_textEdit.setFont(font)
        self.folder_name_textEdit.setObjectName("folder_name_textEdit")
        self.checkBox_visualise_raw = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_visualise_raw.setGeometry(QtCore.QRect(210, 60, 131, 23))
        self.checkBox_visualise_raw.setObjectName("checkBox_visualise_raw")
        self.checkBox_from_file = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_from_file.setGeometry(QtCore.QRect(400, 20, 131, 23))
        self.checkBox_from_file.setObjectName("checkBox_from_file")
        self.exp_name_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.exp_name_textEdit.setGeometry(QtCore.QRect(30, 130, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exp_name_textEdit.setFont(font)
        self.exp_name_textEdit.setObjectName("exp_name_textEdit")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 100, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.create_images_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_images_pushButton.setGeometry(QtCore.QRect(1050, 30, 121, 23))
        self.create_images_pushButton.setObjectName("create_images_pushButton")
        self.saturation_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.saturation_textEdit.setGeometry(QtCore.QRect(1040, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saturation_textEdit.setFont(font)
        self.saturation_textEdit.setObjectName("saturation_textEdit")
        self.saturation_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saturation_pushButton.setGeometry(QtCore.QRect(900, 70, 121, 23))
        self.saturation_pushButton.setObjectName("saturation_pushButton")
        self.contrast_textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.contrast_textEdit_3.setGeometry(QtCore.QRect(1100, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrast_textEdit_3.setFont(font)
        self.contrast_textEdit_3.setObjectName("contrast_textEdit_3")
        self.contrast_textEdit_4 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.contrast_textEdit_4.setGeometry(QtCore.QRect(1100, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrast_textEdit_4.setFont(font)
        self.contrast_textEdit_4.setObjectName("contrast_textEdit_4")
        self.gamma_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.gamma_textEdit.setGeometry(QtCore.QRect(1040, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gamma_textEdit.setFont(font)
        self.gamma_textEdit.setObjectName("gamma_textEdit")
        self.gamma_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.gamma_pushButton.setGeometry(QtCore.QRect(900, 110, 121, 23))
        self.gamma_pushButton.setObjectName("gamma_pushButton")
        self.white_balance_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.white_balance_pushButton.setGeometry(QtCore.QRect(900, 150, 121, 23))
        self.white_balance_pushButton.setObjectName("white_balance_pushButton")
        self.white_balance_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.white_balance_textEdit.setGeometry(QtCore.QRect(1040, 150, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.white_balance_textEdit.setFont(font)
        self.white_balance_textEdit.setObjectName("white_balance_textEdit")
        self.gamma_textEdit_3 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.gamma_textEdit_3.setGeometry(QtCore.QRect(1100, 150, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gamma_textEdit_3.setFont(font)
        self.gamma_textEdit_3.setObjectName("gamma_textEdit_3")
        self.contrast_textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.contrast_textEdit_2.setGeometry(QtCore.QRect(820, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contrast_textEdit_2.setFont(font)
        self.contrast_textEdit_2.setObjectName("contrast_textEdit_2")
        self.brightness_textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.brightness_textEdit_2.setGeometry(QtCore.QRect(820, 70, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.brightness_textEdit_2.setFont(font)
        self.brightness_textEdit_2.setObjectName("brightness_textEdit_2")
        self.file_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.file_pushButton.setGeometry(QtCore.QRect(400, 50, 81, 23))
        self.file_pushButton.setObjectName("file_pushButton")
        self.court_points_L_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.court_points_L_pushButton.setGeometry(QtCore.QRect(400, 80, 161, 23))
        self.court_points_L_pushButton.setObjectName("court_points_L_pushButton")
        self.save_points_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_points_pushButton.setGeometry(QtCore.QRect(400, 140, 161, 23))
        self.save_points_pushButton.setObjectName("save_points_pushButton")
        self.court_points_R_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.court_points_R_pushButton.setGeometry(QtCore.QRect(400, 110, 161, 23))
        self.court_points_R_pushButton.setObjectName("court_points_R_pushButton")
        self.img_size_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.img_size_comboBox.setGeometry(QtCore.QRect(720, 140, 151, 25))
        self.img_size_comboBox.setObjectName("img_size_comboBox")
        self.cut_comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.cut_comboBox.setGeometry(QtCore.QRect(1170, 150, 151, 25))
        self.cut_comboBox.setObjectName("cut_comboBox")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1170, 120, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(580, 140, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.jumps_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.jumps_textEdit.setGeometry(QtCore.QRect(1320, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.jumps_textEdit.setFont(font)
        self.jumps_textEdit.setObjectName("jumps_textEdit")
        self.label_16 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1250, 20, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.time_sleep_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.time_sleep_textEdit.setGeometry(QtCore.QRect(1320, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_sleep_textEdit.setFont(font)
        self.time_sleep_textEdit.setObjectName("time_sleep_textEdit")
        self.label_17 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1160, 70, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.qdetR_size_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.qdetR_size_textEdit.setEnabled(False)
        self.qdetR_size_textEdit.setGeometry(QtCore.QRect(1490, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qdetR_size_textEdit.setFont(font)
        self.qdetR_size_textEdit.setObjectName("qdetR_size_textEdit")
        self.label_18 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1400, 20, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.qdetL_size_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.qdetL_size_textEdit.setEnabled(False)
        self.qdetL_size_textEdit.setGeometry(QtCore.QRect(1490, 50, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qdetL_size_textEdit.setFont(font)
        self.qdetL_size_textEdit.setObjectName("qdetL_size_textEdit")
        self.label_19 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1400, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.qsaveR_size_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.qsaveR_size_textEdit.setEnabled(False)
        self.qsaveR_size_textEdit.setGeometry(QtCore.QRect(1490, 110, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qsaveR_size_textEdit.setFont(font)
        self.qsaveR_size_textEdit.setObjectName("qsaveR_size_textEdit")
        self.label_20 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1400, 140, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.qsaveL_size_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.qsaveL_size_textEdit.setEnabled(False)
        self.qsaveL_size_textEdit.setGeometry(QtCore.QRect(1490, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qsaveL_size_textEdit.setFont(font)
        self.qsaveL_size_textEdit.setObjectName("qsaveL_size_textEdit")
        self.label_21 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1400, 110, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.qstad_size_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.qstad_size_textEdit.setEnabled(False)
        self.qstad_size_textEdit.setGeometry(QtCore.QRect(1490, 80, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.qstad_size_textEdit.setFont(font)
        self.qstad_size_textEdit.setObjectName("qstad_size_textEdit")
        self.label_22 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(1400, 80, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.velR_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.velR_textEdit.setEnabled(False)
        self.velR_textEdit.setGeometry(QtCore.QRect(1600, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.velR_textEdit.setFont(font)
        self.velR_textEdit.setObjectName("velR_textEdit")
        self.label_23 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(1550, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.velL_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.velL_textEdit.setEnabled(False)
        self.velL_textEdit.setGeometry(QtCore.QRect(1600, 60, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.velL_textEdit.setFont(font)
        self.velL_textEdit.setObjectName("velL_textEdit")
        self.label_24 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(1550, 60, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.checkBox_record_video = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_record_video.setGeometry(QtCore.QRect(210, 0, 131, 23))
        self.checkBox_record_video.setObjectName("checkBox_record_video")
        self.checkBox_visualise_processed = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_visualise_processed.setGeometry(QtCore.QRect(210, 40, 151, 23))
        self.checkBox_visualise_processed.setObjectName("checkBox_visualise_processed")
        self.label_25 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(1220, 100, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.batch_size_textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.batch_size_textEdit.setGeometry(QtCore.QRect(1320, 100, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batch_size_textEdit.setFont(font)
        self.batch_size_textEdit.setObjectName("batch_size_textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1694, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_pushButton.setText(_translate("MainWindow", "Start"))
        self.stop_pushButton.setText(_translate("MainWindow", "Stop"))
        self.fps_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">60</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "fps input"))
        self.fps_repetition_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">60</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "fps output"))
        self.checkBox_plot_video.setText(_translate("MainWindow", "plot video"))
        self.brightness_pushButton.setText(_translate("MainWindow", "Brightness"))
        self.brightness_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">50</span></p></body></html>"))
        self.contrast_pushButton.setText(_translate("MainWindow", "Contrast"))
        self.contrast_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">50</span></p></body></html>"))
        self.folder_name_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.checkBox_visualise_raw.setText(_translate("MainWindow", "visualise raw"))
        self.checkBox_from_file.setText(_translate("MainWindow", "from file"))
        self.exp_name_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">video1</p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Exp Name"))
        self.create_images_pushButton.setText(_translate("MainWindow", "Create Images"))
        self.saturation_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">50</span></p></body></html>"))
        self.saturation_pushButton.setText(_translate("MainWindow", "Saturation"))
        self.contrast_textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">70</span></p></body></html>"))
        self.contrast_textEdit_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">110</span></p></body></html>"))
        self.gamma_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">50</span></p></body></html>"))
        self.gamma_pushButton.setText(_translate("MainWindow", "Gamma"))
        self.white_balance_pushButton.setText(_translate("MainWindow", "White Balance"))
        self.white_balance_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">50</span></p></body></html>"))
        self.gamma_textEdit_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">5000</span></p></body></html>"))
        self.contrast_textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.brightness_textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.file_pushButton.setText(_translate("MainWindow", "file"))
        self.court_points_L_pushButton.setText(_translate("MainWindow", "court points L"))
        self.save_points_pushButton.setText(_translate("MainWindow", "save points"))
        self.court_points_R_pushButton.setText(_translate("MainWindow", "court points R"))
        self.label_14.setText(_translate("MainWindow", "cut size"))
        self.label_15.setText(_translate("MainWindow", "Output camera"))
        self.jumps_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">4</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "jump 1/"))
        self.time_sleep_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0.015</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "sleep(s)-processed video"))
        self.qdetR_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "q_detL.size"))
        self.qdetL_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "q_detR.size"))
        self.qsaveR_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "q_saveR.size"))
        self.qsaveL_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "q_saveL.size"))
        self.qstad_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "q_stad.size"))
        self.velR_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "velR"))
        self.velL_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">0</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "velL"))
        self.checkBox_record_video.setText(_translate("MainWindow", "record video"))
        self.checkBox_visualise_processed.setText(_translate("MainWindow", "visualise processed"))
        self.label_25.setText(_translate("MainWindow", "batch size"))
        self.batch_size_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">4</span></p></body></html>"))
