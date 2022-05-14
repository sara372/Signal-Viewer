# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5 import QtCore
import sys
import numpy as np
import pandas as pd
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene
from pyqtgraph import PlotWidget, PlotItem
import pyqtgraph as pg
import os
import img_rc
from scipy import signal
import matplotlib.pyplot as plt
from reportlab.pdfgen import canvas
import pyqtgraph.exporters
from PyQt5 import QtCore, QtGui, QtWidgets
import statistics
from fpdf import FPDF
from matplotlib.ticker import ScalarFormatter


class Ui_MainWindow(QtWidgets.QMainWindow):
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from matplotlib.ticker import ScalarFormatter
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1408, 843)
        MainWindow.setStyleSheet("QPushButton { background-color: black; }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(11, 721, 1371, 60))
        self.groupBox.setStyleSheet(" QGroupBox {\n"
"    background-color: white;\n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slow_button = QtWidgets.QPushButton(self.groupBox)
        self.slow_button.setStyleSheet("QPushButton { background-color: white; }")
        self.slow_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/64488.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slow_button.setIcon(icon)
        self.slow_button.setIconSize(QtCore.QSize(30, 30))
        self.slow_button.setObjectName("slow_button")
        self.horizontalLayout.addWidget(self.slow_button)
        self.begin_button = QtWidgets.QPushButton(self.groupBox)
        self.begin_button.setStyleSheet("QPushButton { background-color: white; }")
        self.begin_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.begin_button.setIcon(icon1)
        self.begin_button.setIconSize(QtCore.QSize(30, 30))
        self.begin_button.setObjectName("begin_button")
        self.horizontalLayout.addWidget(self.begin_button)
        self.play_button = QtWidgets.QPushButton(self.groupBox)
        self.play_button.setStyleSheet("QPushButton { background-color: white; }")
        self.play_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/play.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon2)
        self.play_button.setIconSize(QtCore.QSize(25, 25))
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        self.stop_button = QtWidgets.QPushButton(self.groupBox)
        self.stop_button.setStyleSheet("QPushButton { background-color: white; }")
        self.stop_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/تdزnT.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop_button.setIcon(icon3)
        self.stop_button.setIconSize(QtCore.QSize(30, 30))
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout.addWidget(self.stop_button)
        self.speed_button = QtWidgets.QPushButton(self.groupBox)
        self.speed_button.setStyleSheet("QPushButton { background-color: white; }")
        self.speed_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/media_fast_forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speed_button.setIcon(icon4)
        self.speed_button.setIconSize(QtCore.QSize(30, 30))
        self.speed_button.setObjectName("speed_button")
        self.horizontalLayout.addWidget(self.speed_button)
        self.up_button = QtWidgets.QPushButton(self.groupBox)
        self.up_button.setStyleSheet("QPushButton { background-color: white; }")
        self.up_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/uparrw-Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_button.setIcon(icon5)
        self.up_button.setIconSize(QtCore.QSize(25, 25))
        self.up_button.setObjectName("up_button")
        self.horizontalLayout.addWidget(self.up_button)
        self.down_button = QtWidgets.QPushButton(self.groupBox)
        self.down_button.setStyleSheet("QPushButton { background-color: white; }")
        self.down_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/dwnarrw.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_button.setIcon(icon6)
        self.down_button.setIconSize(QtCore.QSize(25, 25))
        self.down_button.setObjectName("down_button")
        self.horizontalLayout.addWidget(self.down_button)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.right_slider = QtWidgets.QSlider(self.groupBox)
        self.right_slider.setOrientation(QtCore.Qt.Horizontal)
        self.right_slider.setObjectName("right_slider")
        self.verticalLayout_2.addWidget(self.right_slider)
        self.left_slider = QtWidgets.QSlider(self.groupBox)
        self.left_slider.setOrientation(QtCore.Qt.Horizontal)
        self.left_slider.setObjectName("left_slider")
        self.verticalLayout_2.addWidget(self.left_slider)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.zoom_out = QtWidgets.QPushButton(self.groupBox)
        self.zoom_out.setStyleSheet("QPushButton { background-color: white; }")
        self.zoom_out.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/zoomout.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out.setIcon(icon7)
        self.zoom_out.setIconSize(QtCore.QSize(25, 25))
        self.zoom_out.setObjectName("zoom_out")
        self.horizontalLayout.addWidget(self.zoom_out)
        self.zoom_in = QtWidgets.QPushButton(self.groupBox)
        self.zoom_in.setStyleSheet("QPushButton { background-color: white; }")
        self.zoom_in.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/zoomin.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in.setIcon(icon8)
        self.zoom_in.setIconSize(QtCore.QSize(25, 25))
        self.zoom_in.setObjectName("zoom_in")
        self.horizontalLayout.addWidget(self.zoom_in)
        self.color_box_signals = QtWidgets.QComboBox(self.groupBox)
        self.color_box_signals.setObjectName("color_box_signals")
        self.color_box_signals.addItem("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/red.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("img/red.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.color_box_signals.addItem(icon9, "")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/ColorSwatch_RoyalBlue_8532a670-01e9-4af4-95d5-49c2df05afe7_700x700.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("img/ColorSwatch_RoyalBlue_8532a670-01e9-4af4-95d5-49c2df05afe7_700x700.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.color_box_signals.addItem(icon10, "")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("img/color-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap("img/color-image.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.color_box_signals.addItem(icon11, "")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("img/FFF305.png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap("img/FFF305.png.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.color_box_signals.addItem(icon12, "")
        self.horizontalLayout.addWidget(self.color_box_signals)
        self.color_palette_spectro = QtWidgets.QComboBox(self.groupBox)
        self.color_palette_spectro.setObjectName("color_palette_spectro")
        self.color_palette_spectro.addItem("")
        self.color_palette_spectro.addItem("")
        self.color_palette_spectro.addItem("")
        self.color_palette_spectro.addItem("")
        self.color_palette_spectro.addItem("")
        self.horizontalLayout.addWidget(self.color_palette_spectro)
        self.hide_signal1 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.hide_signal1.setFont(font)
        self.hide_signal1.setObjectName("hide_signal1")
        self.horizontalLayout.addWidget(self.hide_signal1)
        self.hide_signal2 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.hide_signal2.setFont(font)
        self.hide_signal2.setObjectName("hide_signal2")
        self.horizontalLayout.addWidget(self.hide_signal2)
        self.hide_signal3 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.hide_signal3.setFont(font)
        self.hide_signal3.setObjectName("hide_signal3")
        self.horizontalLayout.addWidget(self.hide_signal3)
        self.hide_signal4 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.hide_signal4.setFont(font)
        self.hide_signal4.setObjectName("hide_signal4")
        self.horizontalLayout.addWidget(self.hide_signal4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(90, 30, 1111, 691))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.graphicsView_1 = PlotWidget(self.splitter)
        self.graphicsView_1.setMouseTracking(True)
        self.graphicsView_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.graphicsView_1.setAutoFillBackground(True)
        self.graphicsView_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_1.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.spectrogram = QtWidgets.QLabel(self.splitter)
        self.spectrogram.setText("")
        self.spectrogram.setScaledContents(True)
        self.spectrogram.setObjectName("spectrogram")
        self.max_contrast = QtWidgets.QSlider(self.centralwidget)
        self.max_contrast.setGeometry(QtCore.QRect(1320, 340, 22, 371))
        self.max_contrast.setMinimum(22)
        self.max_contrast.setMaximum(22)
        self.max_contrast.setSliderPosition(22)
        self.max_contrast.setOrientation(QtCore.Qt.Vertical)
        self.max_contrast.setObjectName("max_contrast")
        self.min_contrast = QtWidgets.QSlider(self.centralwidget)
        self.min_contrast.setGeometry(QtCore.QRect(1250, 340, 22, 371))
        self.min_contrast.setOrientation(QtCore.Qt.Vertical)
        self.min_contrast.setObjectName("min_contrast")
        self.name_signal2 = QtWidgets.QLabel(self.centralwidget)
        self.name_signal2.setGeometry(QtCore.QRect(290, 0, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name_signal2.setFont(font)
        self.name_signal2.setText("")
        self.name_signal2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_signal2.setObjectName("name_signal2")
        self.name_signal1 = QtWidgets.QLabel(self.centralwidget)
        self.name_signal1.setGeometry(QtCore.QRect(90, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name_signal1.setFont(font)
        self.name_signal1.setText("")
        self.name_signal1.setAlignment(QtCore.Qt.AlignCenter)
        self.name_signal1.setObjectName("name_signal1")
        self.name_signal3 = QtWidgets.QLabel(self.centralwidget)
        self.name_signal3.setGeometry(QtCore.QRect(520, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name_signal3.setFont(font)
        self.name_signal3.setText("")
        self.name_signal3.setAlignment(QtCore.Qt.AlignCenter)
        self.name_signal3.setObjectName("name_signal3")
        self.name_signal4 = QtWidgets.QLabel(self.centralwidget)
        self.name_signal4.setGeometry(QtCore.QRect(750, 0, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.name_signal4.setFont(font)
        self.name_signal4.setText("")
        self.name_signal4.setAlignment(QtCore.Qt.AlignCenter)
        self.name_signal4.setObjectName("name_signal4")
        self.max_label = QtWidgets.QLabel(self.centralwidget)
        self.max_label.setGeometry(QtCore.QRect(1310, 310, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.max_label.setFont(font)
        self.max_label.setObjectName("max_label")
        self.min_label = QtWidgets.QLabel(self.centralwidget)
        self.min_label.setGeometry(QtCore.QRect(1240, 310, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.min_label.setFont(font)
        self.min_label.setObjectName("min_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1408, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd_Signals = QtWidgets.QMenu(self.menuFile)
        self.menuAdd_Signals.setObjectName("menuAdd_Signals")
        self.menuChannels = QtWidgets.QMenu(self.menubar)
        self.menuChannels.setObjectName("menuChannels")
        self.menuspectrogram = QtWidgets.QMenu(self.menubar)
        self.menuspectrogram.setObjectName("menuspectrogram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPrint_to_PDF = QtWidgets.QAction(MainWindow)
        self.actionPrint_to_PDF.setObjectName("actionPrint_to_PDF")
        self.actionCloseAll = QtWidgets.QAction(MainWindow)
        self.actionCloseAll.setObjectName("actionCloseAll")
        self.actionchannel_1 = QtWidgets.QAction(MainWindow)
        self.actionchannel_1.setObjectName("actionchannel_1")
        self.actionChannel_2 = QtWidgets.QAction(MainWindow)
        self.actionChannel_2.setObjectName("actionChannel_2")
        self.actionChannel_3 = QtWidgets.QAction(MainWindow)
        self.actionChannel_3.setObjectName("actionChannel_3")
        self.actionChannel_1 = QtWidgets.QAction(MainWindow)
        self.actionChannel_1.setCheckable(True)
        self.actionChannel_1.setChecked(False)
        self.actionChannel_1.setObjectName("actionChannel_1")
        self.actionChannel_4 = QtWidgets.QAction(MainWindow)
        self.actionChannel_4.setCheckable(True)
        self.actionChannel_4.setObjectName("actionChannel_4")
        self.actionChannel_5 = QtWidgets.QAction(MainWindow)
        self.actionChannel_5.setCheckable(True)
        self.actionChannel_5.setObjectName("actionChannel_5")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionsignal1 = QtWidgets.QAction(MainWindow)
        self.actionsignal1.setObjectName("actionsignal1")
        self.actionsignal2 = QtWidgets.QAction(MainWindow)
        self.actionsignal2.setObjectName("actionsignal2")
        self.actionsignal3 = QtWidgets.QAction(MainWindow)
        self.actionsignal3.setObjectName("actionsignal3")
        self.actionsignal_1 = QtWidgets.QAction(MainWindow)
        self.actionsignal_1.setObjectName("actionsignal_1")
        self.actionsignal_2 = QtWidgets.QAction(MainWindow)
        self.actionsignal_2.setObjectName("actionsignal_2")
        self.actionsignal_3 = QtWidgets.QAction(MainWindow)
        self.actionsignal_3.setObjectName("actionsignal_3")
        self.actionabnormal_signal = QtWidgets.QAction(MainWindow)
        self.actionabnormal_signal.setObjectName("actionabnormal_signal")
        self.actionviridis = QtWidgets.QAction(MainWindow)
        self.actionviridis.setObjectName("actionviridis")
        self.actionplasma = QtWidgets.QAction(MainWindow)
        self.actionplasma.setObjectName("actionplasma")
        self.actioninferno = QtWidgets.QAction(MainWindow)
        self.actioninferno.setObjectName("actioninferno")
        self.actionmagma = QtWidgets.QAction(MainWindow)
        self.actionmagma.setObjectName("actionmagma")
        self.actioncividis = QtWidgets.QAction(MainWindow)
        self.actioncividis.setObjectName("actioncividis")
        self.actionsignal_4 = QtWidgets.QAction(MainWindow)
        self.actionsignal_4.setObjectName("actionsignal_4")
        self.menuAdd_Signals.addAction(self.actionsignal1)
        self.menuAdd_Signals.addAction(self.actionsignal2)
        self.menuAdd_Signals.addAction(self.actionsignal3)
        self.menuAdd_Signals.addAction(self.actionabnormal_signal)
        self.menuFile.addAction(self.menuAdd_Signals.menuAction())
        self.menuFile.addAction(self.actionPrint_to_PDF)
        self.menuFile.addAction(self.actionCloseAll)
        self.menuFile.addAction(self.actionExit)
        self.menuspectrogram.addAction(self.actionsignal_1)
        self.menuspectrogram.addAction(self.actionsignal_2)
        self.menuspectrogram.addAction(self.actionsignal_3)
        self.menuspectrogram.addAction(self.actionsignal_4)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuChannels.menuAction())
        self.menubar.addAction(self.menuspectrogram.menuAction())

        self.retranslateUi(MainWindow)
        self.color_palette_spectro.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Signal Viewer"))
        self.begin_button.setShortcut(_translate("MainWindow", "Alt+S"))
        self.play_button.setShortcut(_translate("MainWindow", "Alt+P"))
        self.up_button.setShortcut(_translate("MainWindow", "Up"))
        self.down_button.setShortcut(_translate("MainWindow", "Down"))
        self.zoom_out.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.zoom_in.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.color_box_signals.setItemText(0, _translate("MainWindow", "default"))
        self.color_box_signals.setItemText(1, _translate("MainWindow", "Red"))
        self.color_box_signals.setItemText(2, _translate("MainWindow", "Blue"))
        self.color_box_signals.setItemText(3, _translate("MainWindow", "Green"))
        self.color_box_signals.setItemText(4, _translate("MainWindow", "Yellow"))
        self.color_palette_spectro.setItemText(0, _translate("MainWindow", "viridis"))
        self.color_palette_spectro.setItemText(1, _translate("MainWindow", "plasma"))
        self.color_palette_spectro.setItemText(2, _translate("MainWindow", "inferno"))
        self.color_palette_spectro.setItemText(3, _translate("MainWindow", "magma"))
        self.color_palette_spectro.setItemText(4, _translate("MainWindow", "cividis"))
        self.hide_signal1.setText(_translate("MainWindow", "Hide signal _1"))
        self.hide_signal2.setText(_translate("MainWindow", "Hide signal_2"))
        self.hide_signal3.setText(_translate("MainWindow", "Hide signal_3"))
        self.hide_signal4.setText(_translate("MainWindow", "Hide abnormal "))
        self.max_label.setText(_translate("MainWindow", "Max"))
        self.min_label.setText(_translate("MainWindow", "Min"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdd_Signals.setTitle(_translate("MainWindow", "Add Signals"))
        self.menuChannels.setTitle(_translate("MainWindow", "Signals"))
        self.menuspectrogram.setTitle(_translate("MainWindow", "spectrogram"))
        self.actionPrint_to_PDF.setText(_translate("MainWindow", "Print to PDF"))
        self.actionPrint_to_PDF.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionCloseAll.setText(_translate("MainWindow", "Close all"))
        self.actionCloseAll.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionchannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.actionChannel_2.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_3.setText(_translate("MainWindow", "Channel 3"))
        self.actionChannel_1.setText(_translate("MainWindow", "Channel 1"))
        self.actionChannel_1.setShortcut(_translate("MainWindow", "Alt+1"))
        self.actionChannel_4.setText(_translate("MainWindow", "Channel 2"))
        self.actionChannel_4.setShortcut(_translate("MainWindow", "Alt+2"))
        self.actionChannel_5.setText(_translate("MainWindow", "Channel 3"))
        self.actionChannel_5.setShortcut(_translate("MainWindow", "Alt+3"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Alt+X"))
        self.actionsignal1.setText(_translate("MainWindow", "signal1"))
        self.actionsignal2.setText(_translate("MainWindow", "signal2"))
        self.actionsignal3.setText(_translate("MainWindow", "signal3"))
        self.actionsignal_1.setText(_translate("MainWindow", "ECG signal"))
        self.actionsignal_2.setText(_translate("MainWindow", "EOG signal"))
        self.actionsignal_3.setText(_translate("MainWindow", "EMG signal"))
        self.actionabnormal_signal.setText(_translate("MainWindow", "abnormal signal"))
        self.actionviridis.setText(_translate("MainWindow", "viridis"))
        self.actionplasma.setText(_translate("MainWindow", "plasma"))
        self.actioninferno.setText(_translate("MainWindow", "inferno"))
        self.actionmagma.setText(_translate("MainWindow", "magma"))
        self.actioncividis.setText(_translate("MainWindow", "cividis"))
        self.actionsignal_4.setText(_translate("MainWindow", "abnormal ECG"))

    
    # creating timers
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()
        self.graphicsView_1.setXRange(min=0, max=10)
        self.pens = [pg.mkPen('r'), pg.mkPen('b'), pg.mkPen('g'), pg.mkPen('y')]


        # Connecting Buttons
        #File Menu
        self.actionsignal1.triggered.connect(lambda: self.open_file1()) 
        self.actionsignal2.triggered.connect(lambda: self.open_file2())
        self.actionsignal3.triggered.connect(lambda: self.open_file3())
        self.actionabnormal_signal.triggered.connect(lambda: self.open_file4()) 
        self.actionCloseAll.triggered.connect(lambda: self.clear_all())  
        self.actionExit.triggered.connect(lambda: self.close())
        self.actionsignal_1.triggered.connect(lambda: self.spectrogram1())
        self.actionsignal_2.triggered.connect(lambda: self.spectrogram2())
        self.actionsignal_3.triggered.connect(lambda: self.spectrogram3())
        self.actionsignal_4.triggered.connect(lambda: self.spectrogram4())
        self.actionPrint_to_PDF.triggered.connect(lambda: self.pdf()) 


        #Toolbar
        self.play_button.clicked.connect(lambda: self.play())
        self.stop_button.clicked.connect(lambda: self.stop())
        self.begin_button.clicked.connect(lambda: self.begin())
        self.speed_button.clicked.connect(lambda: self.speed())
        self.slow_button.clicked.connect(lambda: self.slow())
        
        self.hide_signal1.stateChanged.connect(self.hide_ch1)
        self.hide_signal2.stateChanged.connect(self.hide_ch2)
        self.hide_signal3.stateChanged.connect(self.hide_ch3)
        self.hide_signal4.stateChanged.connect(self.hide_ch4)
        
        self.color_box_signals.currentIndexChanged.connect(self.choose_color)
        
        self.zoom_in.clicked.connect(lambda: self.zoomin())
        self.zoom_out.clicked.connect(lambda: self.zoomout())
        
        
        self.right_slider.setMinimum(0) # set min limit
        self.right_slider.setMaximum(100) # set max limit
        self.right_slider.setValue(0) 
        self.right_slider.setTickInterval(15)
        self.right_slider.valueChanged.connect(self.right)
        
        self.left_slider.setMinimum(0) # set min limit
        self.left_slider.setMaximum(100) # set max limit
        self.left_slider.setValue(100) 
        self.left_slider.setTickInterval(1)
        self.left_slider.valueChanged.connect(self.left)
        
        
        self.up_button.clicked.connect(lambda: self.up())
        self.down_button.clicked.connect(lambda: self.down())
        
        self.max_contrast.setMinimum(-60) # set min limit
        self.max_contrast.setMaximum(-40) # set max limit
        self.max_contrast.setValue(-40) 
        self.max_contrast.setTickInterval(1)
        # self.max_contrast.valueChanged.connect(self.right)
        
        self.min_contrast.setMinimum(-100) # set min limit
        self.min_contrast.setMaximum(-80) # set max limit
        self.min_contrast.setValue(-100) 
        self.min_contrast.setTickInterval(1)


 #-----------------------------------------------------------------------------#
    # functions:
    def get_extention(self, s):
        for i in range(1, len(s)):
            if s[-i] == '.':
                return s[-(i - 1):]    
   # single view :

    def open_file1(self):
        self.file_name1 = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open only txt or CSV or xls', os.getenv('HOME'))

        #pass the elements of list in the tuple to the read_file function
        self.read_file1(self.file_name1[0][0]) 
        
    def open_file2(self):
        self.file_name2 = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open only txt or CSV or xls', os.getenv('HOME'))

        #pass the elements of list in the tuple to the read_file function
        self.read_file2(self.file_name2[0][0])  
        
    def open_file3(self):
        self.file_name3 = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open only txt or CSV or xls', os.getenv('HOME'))

        #pass the elements of list in the tuple to the read_file function
        self.read_file3(self.file_name3[0][0])  
    
    def open_file4(self):
        self.file_name4 = QtWidgets.QFileDialog.getOpenFileNames(
            self, 'Open only txt or CSV or xls', os.getenv('HOME'))

        #pass the elements of list in the tuple to the read_file function
        self.read_file4(self.file_name4[0][0])
        
    path1=''
    def read_file1(self, file_path):
        self.path1 = file_path
        self.file_ex = self.get_extention(self.path1)
        if self.file_ex == 'txt':
            data1 = pd.read_csv(self.path1)
            self.y_signal1 = data1.values[:, 0]
            self.x_signal1 = np.linspace(0, 0.001 * len(self.y_signal1), len(self.y_signal1)) #generates time values corresponding to amplitudes in y
        if self.file_ex == 'csv':
            data1 = pd.read_csv(self.path1)
            #contain the amplitudes
            self.y_signal1 = data1.values[:, 1]
            #containe the time values
            self.x_signal1 = data1.values[:, 0]
        self.data_line1 = self.graphicsView_1.plot(self.x_signal1, self.y_signal1, pen=self.pens[0])
        self.name_signal1.setText('ECG signal ')
        self.name_signal1.setStyleSheet("background-color: red")
        self.idx1 = 0
        self.timer1.setInterval(80)
        self.timer1.timeout.connect(self.update_plot_data1)
        self.timer1.start()
    path2=''
    def read_file2(self, file_path):
        self.path2 = file_path
        self.file_ex = self.get_extention(self.path2)
        if self.file_ex == 'txt':
            data2 = pd.read_csv(self.path2)
            self.y_signal2 = data2.values[:, 0]
            self.x_signal2 = np.linspace(0, 0.001 * len(self.y_signal2), len(self.y_signal2))
        if self.file_ex == 'csv':
            data2 = pd.read_csv(self.path2)
            self.y_signal2 = data2.values[:, 1]
            self.x_signal2 = data2.values[:, 0]
        self.data_line2 = self.graphicsView_1.plot(
            self.x_signal2, self.y_signal2, pen=self.pens[1])
        self.name_signal2.setText('EOG signal ')
        self.name_signal2.setStyleSheet("background-color: blue")
        self.idx2 = 0
        self.timer1.setInterval(30)
        self.timer1.timeout.connect(self.update_plot_data2)
        self.timer1.start()

    path3=''
    def read_file3(self, file_path):
        self.path3 = file_path
        self.file_ex = self.get_extention(self.path3)
        if self.file_ex == 'txt':
            data3 = pd.read_csv(self.path3)
            self.y_signal3 = data3.values[:, 0]
            self.x_signal3 = np.linspace(0, 0.001 * len(self.y_signal3), len(self.y_signal3))
        if self.file_ex == 'csv':
            data3 = pd.read_csv(self.path3)
            self.y_signal3 = data3.values[:, 1]
            self.x_signal3 = data3.values[:, 0]
        self.data_line3 = self.graphicsView_1.plot(
            self.x_signal3, self.y_signal3, pen=self.pens[2])
        self.name_signal3.setText('EMG signal ')
        self.name_signal3.setStyleSheet("background-color: green")
        self.idx3 = 0
        self.timer1.setInterval(30)
        self.timer1.timeout.connect(self.update_plot_data3)
        self.timer1.start()
    
    path4=''
    def read_file4(self, file_path):
        self.path4 = file_path
        self.file_ex = self.get_extention(self.path4)
        if self.file_ex == 'txt':
            data4 = pd.read_csv(self.path4)
            self.y_signal4 = data4.values[:, 0]
            self.x_signal4 = np.linspace(0, 0.001 * len(self.y_signal4), len(self.y_signal4))
        if self.file_ex == 'csv':
            data4 = pd.read_csv(self.path4)
            self.y_signal4 = data4.values[:, 1]
            self.x_signal4 = data4.values[:, 0]
        self.data_line4 = self.graphicsView_1.plot(
            self.x_signal4, self.y_signal4, pen=self.pens[3])
        self.name_signal4.setText('abnormal ECG ')
        self.name_signal4.setStyleSheet("background-color: yellow")
        self.idx4 = 0
        self.timer1.setInterval(30)
        self.timer1.timeout.connect(self.update_plot_data4)
        self.timer1.start()

    x_limit=[]
    def update_plot_data1(self):
        x_next = self.x_signal1[:self.idx1]
        y_next= self.y_signal1[:self.idx1]
        self.idx1 += 50
        self.x_limit.append(self.idx1)
        # shrink range of x-axis
        self.graphicsView_1.plotItem.setXRange(
            max(x_next, default=0)-9, max(x_next, default=0))
        # Plot the new data
        self.data_line1.setData(x_next, y_next)    
        
    def update_plot_data2(self):
        x_next = self.x_signal2[:self.idx2]
        y_next = self.y_signal2[:self.idx2]
        self.idx2 += 50
        self.x_limit.append(self.idx2)
        self.graphicsView_1.plotItem.setXRange(
            max(x_next, default=0)-18, max(x_next, default=0))  # shrink range of x-axis
        self.data_line2.setData(x_next, y_next)    
    
    def update_plot_data3(self):
        x_next = self.x_signal3[:self.idx3]
        y_next = self.y_signal3[:self.idx3]
        self.idx3 += 20
        self.x_limit.append(self.idx3)
        self.graphicsView_1.plotItem.setXRange(
            max(x_next, default=0)-4, max(x_next, default=0))
        self.data_line3.setData(x_next, y_next)
        
    def update_plot_data4(self):
        x_next = self.x_signal4[:self.idx4]
        y_next = self.y_signal4[:self.idx4]
        self.idx4 += 3
        self.x_limit.append(self.idx4)
        self.graphicsView_1.plotItem.setXRange(
            max(x_next, default=0)-4, max(x_next, default=0))
        self.data_line4.setData(x_next, y_next) 
        
    def clear_all(self): 
        self.graphicsView_1.clear()  
        self.idx1 = 0
        self.idx2 = 0
        self.idx3 = 0
        self.idx4 = 0
        
    # edit the signal :
     
    def begin(self):
            self.idx1 = 0
            self.timer1.setInterval(80)
            self.timer1.timeout.connect(self.update_plot_data1)
            self.timer1.start()
            self.idx2 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.update_plot_data2)
            self.timer1.start()
            self.idx3 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.update_plot_data3)
            self.timer1.start()
            self.idx4 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.update_plot_data4)
            self.timer1.start()

    def play(self): 
        self.timer1.start()
        
    def stop(self):
            self.timer1.stop() 
            
    def speed(self):
          
            # self.idx1 = 0
            self.timer1.setInterval(80)
            self.timer1.timeout.connect(self.update_plot_data1)
            self.timer1.start()
            # # self.idx2 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.update_plot_data2)
            self.timer1.start()
            #self.idx3 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.update_plot_data3)
            self.timer1.start()
            #self.idx4 = 0
            self.timer1.setInterval(80)
            self.timer1.timeout.connect(self.update_plot_data4)
            self.timer1.start()
    

    def slow(self):
            
            self.timer1.setInterval(80)
            self.timer1.timeout.connect(self.slow_plot_data1)
            self.timer1.start()
            # self.idx2 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.slow_plot_data2)
            self.timer1.start()
            #self.idx3 = 0
            self.timer1.setInterval(30)
            self.timer1.timeout.connect(self.slow_plot_data3)
            self.timer1.start()
            #self.idx4 = 0
            self.timer1.setInterval(80)
            self.timer1.timeout.connect(self.slow_plot_data4)
            self.timer1.start()

    def slow_plot_data1(self):
         if self.idx1 > 0 :
              x_next = self.x_signal1[:self.idx1]
              y_next = self.y_signal1[:self.idx1]
              self.idx1 -= 50
        # shrink range of x-axis
              self.graphicsView_1.plotItem.setXRange(
              max(x_next, default=0)-9, max(x_next, default=0))
        # Plot the new data
              self.data_line1.setData(x_next, y_next)
   
    def slow_plot_data2(self):
          if self.idx2 > 0 :
              x_next = self.x_signal2[:self.idx2]
              y_next = self.y_signal2[:self.idx2]
              self.idx2 -= 50
              self.graphicsView_1.plotItem.setXRange(
              max(x_next, default=0)-18, max(x_next, default=0))  # shrink range of x-axis
              self.data_line2.setData(x_next, y_next)        
             
    def slow_plot_data3(self):
        if self.idx3>0 :
            x_next = self.x_signal3[:self.idx3]
            y_next = self.y_signal3[:self.idx3]
            self.idx3 -= 20
            self.graphicsView_1.plotItem.setXRange(
              max(x_next, default=0)-4, max(x_next, default=0))
            self.data_line3.setData(x_next, y_next)
            
    def slow_plot_data4(self):
        if self.idx4>0 :
            x_next = self.x_signal4[:self.idx4]
            y_next = self.y_signal4[:self.idx4]
            self.idx4 -= 5
            self.graphicsView_1.plotItem.setXRange(
              max(x_next, default=0)-4, max(x_next, default=0))
            self.data_line4.setData(x_next, y_next)
        

    def hide_ch1(self):
      
        if self.hide_signal1.isChecked():
            self.data_line1.hide()
            self.name_signal1.setText(' ')
            self.name_signal1.setStyleSheet("background-color: white")
            
        else :

            if self.color_box_signals.currentText() == 'Blue':
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[1])
                self.name_signal1.setText(' ECG signal ')
                self.name_signal1.setStyleSheet("background-color: blue")
                
            if self.color_box_signals.currentText() == 'Red':    
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[0])
                self.name_signal1.setText(' ECG signal ')
                self.name_signal1.setStyleSheet("background-color: red")
            
            if self.color_box_signals.currentText() == 'Green':    
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[2])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: green")
                
            if self.color_box_signals.currentText() == 'Yellow':
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[3])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: yellow")
            if self.color_box_signals.currentText() == 'default':
                self.data_line1 = self.graphicsView_1.plot(
                   self.x_signal1, self.y_signal1, pen= self.pens[0])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: red")
                
        
    def hide_ch2(self):  
        
       if self.hide_signal2.isChecked():
            self.data_line2.hide()
            self.name_signal2.setText(' ')
            self.name_signal2.setStyleSheet("background-color: white")
            
       else : 
            if self.color_box_signals.currentText() == 'Blue':
                self.data_line2 = self.graphicsView_1.plot(
                   self.x_signal2, self.y_signal2, pen= self.pens[1])
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: blue")
                
            if self.color_box_signals.currentText() == 'Red':    
                self.data_line2 = self.graphicsView_1.plot(
                   self.x_signal2, self.y_signal2, pen= self.pens[0])
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: red")
                
            if self.color_box_signals.currentText() == 'Green':    
                self.data_line2 = self.graphicsView_1.plot(
                   self.x_signal2, self.y_signal2, pen= self.pens[2])
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: green")
                
            if self.color_box_signals.currentText() == 'Yellow':
                self.data_line2 = self.graphicsView_1.plot(
                   self.x_signal2, self.y_signal2, pen= self.pens[3]) 
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: yellow")
            if self.color_box_signals.currentText() == 'default':
                self.data_line2 = self.graphicsView_1.plot(
                   self.x_signal2, self.y_signal2, pen= self.pens[1])
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: blue")
    
    def hide_ch3(self): 
        
       if self.hide_signal3.isChecked():
            self.data_line3.hide()
            self.name_signal3.setText(' ')
            self.name_signal3.setStyleSheet("background-color: white")
       else :
            if self.color_box_signals.currentText() == 'Blue':
                self.data_line3 = self.graphicsView_1.plot(
                   self.x_signal3, self.y_signal3, pen= self.pens[1])
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: blue")
                
            if self.color_box_signals.currentText() == 'Red':    
                self.data_line3 = self.graphicsView_1.plot(
                   self.x_signal3, self.y_signal3, pen= self.pens[0])
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: red")
                
            if self.color_box_signals.currentText() == 'Green':    
                self.data_line3 = self.graphicsView_1.plot(
                   self.x_signal3, self.y_signal3, pen= self.pens[2])
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: green")
                
            if self.color_box_signals.currentText() == 'Yellow':
                self.data_line3 = self.graphicsView_1.plot(
                   self.x_signal3, self.y_signal3, pen= self.pens[3])    
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: yellow")
                
            if self.color_box_signals.currentText() == 'default':
                self.data_line3 = self.graphicsView_1.plot(
                   self.x_signal3, self.y_signal3, pen= self.pens[2])             
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: green")
                
    def hide_ch4(self):
        if self.hide_signal4.isChecked():
            self.data_line4.hide()
            self.name_signal4.setText(' ')
            self.name_signal4.setStyleSheet("background-color: white")
        else :
            if self.color_box_signals.currentText() == 'Blue':
                self.data_line4 = self.graphicsView_1.plot(
                   self.x_signal4, self.y_signal4, pen= self.pens[1])
                self.name_signal4.setText(' abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: blue")
                
            if self.color_box_signals.currentText() == 'Red':    
                self.data_line4 = self.graphicsView_1.plot(
                   self.x_signal4, self.y_signal4, pen= self.pens[0])
                self.name_signal4.setText(' abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: red")
                
            if self.color_box_signals.currentText() == 'Green':    
                self.data_line4 = self.graphicsView_1.plot(
                   self.x_signal4, self.y_signal4, pen= self.pens[2])
                self.name_signal4.setText(' abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: green")
                
            if self.color_box_signals.currentText() == 'Yellow':
                self.data_line4 = self.graphicsView_1.plot(
                   self.x_signal4, self.y_signal4, pen= self.pens[3])    
                self.name_signal4.setText(' abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: yellow")
            if self.color_box_signals.currentText() == 'default':
                self.data_line4 = self.graphicsView_1.plot(
                   self.x_signal4, self.y_signal4, pen= self.pens[3])
                self.name_signal4.setText('abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: yellow")

    def choose_color(self):
        if self.color_box_signals.currentText() == 'Blue':
            
            if not self.hide_signal1.isChecked():
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[1])
                self.name_signal1.setText('ECG signal')
                self.name_signal1.setStyleSheet("background-color: blue")
                
            if not self.hide_signal2.isChecked():
                
                self.data_line2 = self.graphicsView_1.plot(
                    self.x_signal2, self.y_signal2, pen= self.pens[1])  
                self.name_signal2.setText('EOG signal')
                self.name_signal2.setStyleSheet("background-color: blue")
                
            if not self.hide_signal3.isChecked():
                self.data_line3 = self.graphicsView_1.plot(
                    self.x_signal3, self.y_signal3, pen=self.pens[1])
                self.name_signal3.setText('EMG signal')
                self.name_signal3.setStyleSheet("background-color: blue")
                
            if not self.hide_signal4.isChecked(): 
                self.data_line4 = self.graphicsView_1.plot(
                    self.x_signal4, self.y_signal4, pen=self.pens[1])
                self.name_signal4.setText('abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: blue")
                
            
        if self.color_box_signals.currentText() == 'Red':
            
            if not self.hide_signal1.isChecked():
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[0])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: red")
                
            if not self.hide_signal2.isChecked():
                self.data_line2 = self.graphicsView_1.plot(
                    self.x_signal2, self.y_signal2, pen= self.pens[0]) 
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: red")
                
            if not self.hide_signal3.isChecked():
                self.data_line3 = self.graphicsView_1.plot(
                    self.x_signal3, self.y_signal3, pen=self.pens[0])
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: red")
                
            if not self.hide_signal4.isChecked(): 
                self.data_line4 = self.graphicsView_1.plot(
                    self.x_signal4, self.y_signal4, pen=self.pens[0])
                self.name_signal4.setText('abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: red")    
            
        
        if self.color_box_signals.currentText() == 'Green':
            
            if not self.hide_signal1.isChecked():
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[2])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: green")
                
            if not self.hide_signal2.isChecked():
                self.data_line2 = self.graphicsView_1.plot(
                    self.x_signal2, self.y_signal2, pen= self.pens[2]) 
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: green")
                
            if not self.hide_signal3.isChecked():
                self.data_line3 = self.graphicsView_1.plot(
                    self.x_signal3, self.y_signal3, pen=self.pens[2])
                self.name_signal3.setText(' EMG signal')
                self.name_signal3.setStyleSheet("background-color: green")
                
            if not self.hide_signal4.isChecked(): 
                self.data_line4 = self.graphicsView_1.plot(
                    self.x_signal4, self.y_signal4, pen=self.pens[2])
                self.name_signal4.setText('abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: green")    
                 
        if self.color_box_signals.currentText() == 'Yellow':  
            
              if not self.hide_signal1.isChecked():
                self.data_line1 = self.graphicsView_1.plot(
                    self.x_signal1, self.y_signal1, pen= self.pens[3])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: yellow")
                
              if not self.hide_signal2.isChecked():
                self.data_line2 = self.graphicsView_1.plot(
                    self.x_signal2, self.y_signal2, pen= self.pens[3])  
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: yellow")
                
              if not self.hide_signal3.isChecked():
                self.data_line3 = self.graphicsView_1.plot(
                    self.x_signal3, self.y_signal3, pen=self.pens[3])
                self.name_signal3.setText(' EMG signal ')
                self.name_signal3.setStyleSheet("background-color: yellow")
                
              if not self.hide_signal4.isChecked(): 
                self.data_line4 = self.graphicsView_1.plot(
                    self.x_signal4, self.y_signal4, pen=self.pens[3])
                self.name_signal4.setText('abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: yellow") 
                
        if self.color_box_signals.currentText()=='default':        
                self.data_line1 = self.graphicsView_1.plot(
                   self.x_signal1, self.y_signal1, pen= self.pens[0])
                self.name_signal1.setText(' ECG signal')
                self.name_signal1.setStyleSheet("background-color: red")  
                
                self.data_line2 = self.graphicsView_1.plot(
                    self.x_signal2, self.y_signal2, pen= self.pens[1])  
                self.name_signal2.setText(' EOG signal')
                self.name_signal2.setStyleSheet("background-color: blue")
                
                self.data_line3 = self.graphicsView_1.plot(
                    self.x_signal3, self.y_signal3, pen=self.pens[2])
                self.name_signal3.setText(' EMG signal ')
                self.name_signal3.setStyleSheet("background-color: green")
                
                self.data_line4 = self.graphicsView_1.plot(
                    self.x_signal4, self.y_signal4, pen=self.pens[3])
                self.name_signal4.setText('abnormal ECG')
                self.name_signal4.setStyleSheet("background-color: yellow") 
                
    def zoomin(self):
        
            self.graphicsView_1.plotItem.getViewBox().scaleBy((0.5, 0.5))

    # Zoomout function connected to zoomout button based on which channel is controlled
    def zoomout(self):
        
            self.graphicsView_1.plotItem.getViewBox().scaleBy((1.5, 1.5))
            
    def right(self):
        if self.right_slider.value()>0 :
            self.range = self.graphicsView_1.getViewBox().viewRange()
            # max_limit=0
            # for limit in self.x_limit:
            #     if self.limit>=self.max_limit:
            #         self.max_limit=self.limit
            self.max_limit=max(self.x_limit)
            if self.range[0][1] < self.x_signal1[self.max_limit] :
                self.graphicsView_1.getViewBox().translateBy(x=+5, y=0)
            # elif self.range[0][1] < max(self.x2) :    
            #      self.graphicsView_1.getViewBox().translateBy(x=+10, y=0)
            # elif self.range[0][1] < max(self.x3) :  
            #     self.graphicsView_1.getViewBox().translateBy(x=+10, y=0)
                
    def left(self):
        if self.left_slider.value()>0 :
            self.range = self.graphicsView_1.getViewBox().viewRange()
            if self.range[0][0] > min(self.x_signal1) :
                self.graphicsView_1.getViewBox().translateBy(x=-5, y=0)
                
    def up(self):
        
       self.range = self.graphicsView_1.getViewBox().viewRange()
       if self.range[1][1] < max(self.y_signal1) :
           self.graphicsView_1.getViewBox().translateBy(x=0, y=+0.2)

    def down(self):
        
        self.range = self.graphicsView_1.getViewBox().viewRange()
        if self.range[1][0] > min(self.y_signal1) :
            self.graphicsView_1.getViewBox().translateBy(x=0, y=-0.2)

    def spectrogram1(self):
        if self.path1 !='':    
       #get data
            self.file_ex = self.get_extention(self.path1)
            if self.file_ex == 'txt':
                
               data = pd.read_csv(self.path1)
               self.signal = data.values[:, 0]
               self.time = np.linspace(0, 0.001 * len(self.signal), len(self.signal)) #generates time values corresponding to amplitudes in y

            if self.file_ex == 'csv':
               data = pd.read_csv(self.path1)
               #contain the amplitudes
               self.signal = data.values[:, 1]
               #containe the time values
               self.time = data.values[:, 0]

        #plot Spectrogram
            camp = self.color_palette_spectro.currentText()
            if self.min_contrast.value() == self.min_contrast.minimum():
                
                VMIN = None
            else:
                VMIN = self.min_contrast.value()

            if self.max_contrast.value() == self.max_contrast.minimum():
                VMAX = None
            else:
                VMAX = self.max_contrast.value()
                
            dt = np.mean(np.diff(self.time))
            fs = int(1/dt)
            amp = self.signal
            plt.clf()
            spectro = plt.specgram(amp, NFFT=1024,Fs=fs, noverlap=900,cmap=camp,vmin=VMIN,vmax=VMAX)
            plt.colorbar()
            plt.savefig('signal.png')
            plt.close()
            spectro_img = QPixmap('signal.png')
            self.spectrogram.setPixmap(spectro_img)
        else:
            plt.clf()
            plt.close()
            self.spectrogram.setText('this signal does not exist')
            
           

    def spectrogram2(self):
        if self.path2 !='':   
            
            self.file_ex = self.get_extention(self.path2)
            if self.file_ex == 'txt':
                data = pd.read_csv(self.path2)
                self.signal = data.values[:, 0]
                self.time = np.linspace(0, 0.001 * len(self.signal), len(self.signal)) #generates time values corresponding to amplitudes in signal

            if self.file_ex == 'csv':
                data = pd.read_csv(self.path2)
            #contain the amplitudes
                self.signal = data.values[:, 1]
            #containe the time values
                self.time = data.values[:, 0]
            camp = self.color_palette_spectro.currentText()
            if self.min_contrast.value() == self.min_contrast.minimum():
                VMIN = None
            else:
                VMIN = self.min_contrast.value()

            if self.max_contrast.value() == self.max_contrast.minimum():
                VMAX = None
            else:
                VMAX = self.max_contrast.value()

            dt = np.mean(np.diff(self.time))
            fs = int(1/dt)
            amp = self.signal
            plt.clf()
            spectro = plt.specgram(amp, NFFT=1024,Fs=fs, noverlap=900,cmap=camp,vmin=VMIN,vmax=VMAX)
            plt.colorbar()
            plt.savefig('signal.png')
            plt.close()
            spectro_img = QPixmap('signal.png')
            self.spectrogram.setPixmap(spectro_img)
        else:
            plt.clf()
            plt.close()
            self.spectrogram.setText('this signal does not exist')
            

    def spectrogram3(self):
        if self.path3 !='':   
            self.file_ex = self.get_extention(self.path3)
            if self.file_ex == 'txt':
                data = pd.read_csv(self.path3)
                self.signal = data.values[:, 0]
                self.time = np.linspace(0, 0.001 * len(self.signal), len(self.signal)) #generates time values corresponding to amplitudes in y

            if self.file_ex == 'csv':
                data = pd.read_csv(self.path3)
            #contain the amplitudes
                self.signal = data.values[:, 1]
            #containe the time values
                self.time = data.values[:, 0]

            camp = self.color_palette_spectro.currentText()
            if self.min_contrast.value() == self.min_contrast.minimum():
                VMIN = None
            else:
                VMIN = self.min_contrast.value()

            if self.max_contrast.value() == self.max_contrast.minimum():
                VMAX = None
            else:
                VMAX = self.max_contrast.value()

            dt = np.mean(np.diff(self.time))
            fs = int(1/dt)
            amp = self.signal
            plt.clf()
            spectro = plt.specgram(amp, NFFT=1024,Fs=fs, noverlap=900,cmap=camp,vmin=VMIN,vmax=VMAX)
            plt.colorbar()
            plt.savefig('signal.png')
            plt.close()
            spectro_img = QPixmap('signal.png')
            self.spectrogram.setPixmap(spectro_img)
        else:
            plt.clf()
            plt.close()
            self.spectrogram.setText('this signal does not exist')
    
    def spectrogram4(self):
        if self.path4 !='':   
            self.file_ex = self.get_extention(path4)
            if self.file_ex == 'txt':
                data = pd.read_csv(path4)
                self.signal = data.values[:, 0]
                self.time = np.linspace(0, 0.001 * len(self.signal), len(self.signal)) #generates time values corresponding to amplitudes in y

            if self.file_ex == 'csv':
                data = pd.read_csv(path4)
            #contain the amplitudes
                self.signal = data.values[:, 1]
            #containe the time values
                self.time = data.values[:, 0]

            camp = self.color_palette_spectro.currentText()
            if self.min_contrast.value() == self.min_contrast.minimum():
                VMIN = None
            else:
                VMIN = self.min_contrast.value()

            if self.max_contrast.value() == self.max_contrast.minimum():
                VMAX = None
            else:
                VMAX = self.max_contrast.value()

            dt = np.mean(np.diff(self.time))
            fs = int(1/dt)
            amp = self.signal
            plt.clf()
            spectro = plt.specgram(amp, NFFT=1024,Fs=fs, noverlap=900,cmap=camp,vmin=VMIN,vmax=VMAX)
            plt.colorbar()
            plt.savefig('signal.png')
            plt.close()
            spectro_img = QPixmap('signal.png')
            self.spectrogram.setPixmap(spectro_img)
        else:
            plt.clf()
            plt.close()
            self.spectrogram.setText('this signal does not exist')
     
    
    
    def pdf(self):
        global path3
        self.file_ex = self.get_extention(path3)
        if self.file_ex == 'txt':
            data = pd.read_csv(path3)
            self.signal3 = data.values[:, 0]
            self.time3= np.linspace(0, 0.001 * len(self.signal3), len(self.signal3) )#generates time values corresponding to amplitudes in y

        if self.file_ex == 'csv':
            data = pd.read_csv(path3)
            #contain the amplitudes
            self.signal3 = data.values[:, 1]
            #containe the time values
            self.time3= data.values[:, 0]
            
        global path2
        self.file_ex = self.get_extention(path2)
        if self.file_ex == 'txt':
            data = pd.read_csv(path2)
            self.signal2= data.values[:, 0]
            self.time2= np.linspace(0, 0.001 * len(self.signal2), len(self.signal2)) #generates time values corresponding to amplitudes in y

        if self.file_ex == 'csv':
            data = pd.read_csv(path2)
            #contain the amplitudes
            self.signal2= data.values[:, 1]
            #containe the time values
            self.time2= data.values[:, 0]
            
        global path1
        self.file_ex = self.get_extention(path1)
        if self.file_ex == 'txt':
            data = pd.read_csv(path3)
            self.signal1= data.values[:, 0]
            self.time1= np.linspace(0, 0.001 * len(self.signal1), len(self.signal1)) #generates time values corresponding to amplitudes in y

        if self.file_ex == 'csv':
            data = pd.read_csv(path1)
            #contain the amplitudes
            self.signal1= data.values[:, 1]
            #containe the time values
            self.time1= data.values[:, 0]
            
        global path4
        self.file_ex = self.get_extention(path4)
        if self.file_ex == 'txt':
            data = pd.read_csv(path4)
            self.signal4= data.values[:, 0]
            self.time4= np.linspace(0, 0.001 * len(self.signal4), len(self.signal4)) #generates time values corresponding to amplitudes in y

        if self.file_ex == 'csv':
            data = pd.read_csv(path4)
            #contain the amplitudes
            self.signal4= data.values[:, 1]
            #containe the time values
            self.time4= data.values[:, 0]




        
        self.min1=min(self.signal1)
        self.min2=min(self.signal2)
        self.min3=min(self.signal3)
        self.min4=min(self.signal4)
        self.max1=max(self.signal1)
        self.max2=max(self.signal2)
        self.max3=max(self.signal3)
        self.max4=max(self.signal4)
        self.mean1=statistics.mean(self.signal1)
        self.mean2=statistics.mean(self.signal2)
        self.mean3=statistics.mean(self.signal3)
        self.mean4=statistics.mean(self.signal4)
        
        self.std1=statistics.stdev(self.signal1)
        self.std2=statistics.stdev(self.signal2)
        self.std3=statistics.stdev(self.signal3)
        self.std4=statistics.stdev(self.signal4)
        
        self.duration1=self.time1[len(self.time1)-1]-self.time1[0]
        self.duration2=self.time2[len(self.time2)-1]-self.time2[0]
        self.duration3=self.time3[len(self.time3)-1]-self.time3[0]
        self.duration4=self.time4[len(self.time4)-1]-self.time4[0]        
       #add font
        
        self.pdf = FPDF(orientation = 'P', unit = 'mm', format = 'A4')
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 24)
        self.pdf.set_text_color(0,0,0)
        #pdf.set_auto_page_break(auto='True',margin=15)
        self.pdf.set_xy(105,5)
        self.pdf.cell(150,10, 'Report', 'B',1,'C', False) 
        
        
        #add image
        self.pdf.image('signal.png', x =10, y = 20, w = 150, h =100)
        self.pdf.set_xy(50,130)
        self.pdf.cell(100,10, 'spectrogram', '',1,'C', False)
       
        im_export=pyqtgraph.exporters.ImageExporter(self.graphicsView_1.scene())
        im_export.export('graph.png')
     
        self.pdf.image('graph.png', x =10, y = 150, w = 150, h =100)
       
        self.pdf.set_xy(50,260)
        self.pdf.cell(100,10, 'signals', '',1,'C', False)
        
        # Effective page width, or just epw
        epw = self.pdf.w - 2*self.pdf.l_margin
        
        # Set column width to 1/4 of effective page width to distribute content 
        # evenly across table and page
        # col_width = epw/5
        col_width = epw/6
        
        
        table=[["signal",'min','max','mean','std','time'],
               ["ECG",self.min1,self.max1,self.mean1,self.std1,self.duration1],
               ["EOG",self.min2,self.max2,self.mean2,self.std2,self.duration2],
               ["EMG",self.min3,self.max3,self.mean3,self.std3,self.duration3],
               ["abnormal",self.min4,self.max4,self.mean4,self.std4,self.duration4]
              
        ]
      
        th = self.pdf.font_size
        self.pdf.add_page()
        self.pdf.set_xy(epw/2,0)
        self.pdf.cell(col_width,10, 'statistics', '',1,'C', False)
        for row in table:
            for datum in row:
                # Enter data in colums
                # Notice the use of the function str to coerce any input to the 
                # string type. This is needed
                # since pyFPDF expects a string, not a number.
                self.pdf.cell(col_width,th, str(datum)[0:5], border=1,ln=0,align='C',link=False)
         
            self.pdf.ln(th)
        self.pdf.output('report2.pdf')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
