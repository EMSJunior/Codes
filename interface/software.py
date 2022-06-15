# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'software.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functions import *
from cep import *
from datetime import datetime
import contratos
import recibos
import os
from criarEvento import Ui_CriarEvento

from unicodedata import normalize
import imgFundo

class MyLineEdit(QtWidgets.QLineEdit):

    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        super(MyLineEdit, self).mousePressEvent(event)
        self.clicked.emit()

class Ui_MainWindow(object):
    def openWindow(self,escolha,dados):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CriarEvento()
        self.ui.setupUi(self.window,escolha,dados)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 980)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
        "background-image: url(:/newPrefix/fundo.png);\n"
        "background-repeat:no-repeat;\n"
        "}\n"
        "QTextCodec::setCodecForCStrings(QTextCodec::codecForName(\"UTF-8\"));")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QtWidgets.QFrame(self.frame)
        self.frame_content.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setStyleSheet("background: transparent;\n"
        "color:black;")
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pg_home = QtWidgets.QWidget()
        self.pg_home.setObjectName("pg_home")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.pg_home)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_27 = QtWidgets.QFrame(self.pg_home)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame_27)
        self.widget.setStyleSheet("background: transparent;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_28 = QtWidgets.QFrame(self.widget)
        self.frame_28.setStyleSheet("background: transparent;")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_29 = QtWidgets.QFrame(self.frame_28)
        self.frame_29.setStyleSheet("QFrame{\n"
        "background: transparent;}")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_29)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setMinimumSize(QtCore.QSize(0, 600))
        self.frame_30.setStyleSheet("background-image:url(:/newPrefix/Logo.png);\n"
        "background-repeat:no-repeat;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_3.addWidget(self.frame_30)
        self.verticalLayout_3.addWidget(self.frame_29)
        self.frame_31 = QtWidgets.QFrame(self.frame_28)
        self.frame_31.setStyleSheet("background: transparent;")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bttCadastro = QtWidgets.QPushButton(self.frame_31)
        self.bttCadastro.setMinimumSize(QtCore.QSize(150, 100))
        self.bttCadastro.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bttCadastro.setStyleSheet("QPushButton{\n"
        "    font: 16pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:50px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttCadastro.setObjectName("bttCadastro")
        self.horizontalLayout_4.addWidget(self.bttCadastro)
        self.bttAgendamento = QtWidgets.QPushButton(self.frame_31)
        self.bttAgendamento.setMinimumSize(QtCore.QSize(150, 100))
        self.bttAgendamento.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bttAgendamento.setStyleSheet("QPushButton{\n"
        "    font: 16pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:50px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttAgendamento.setObjectName("bttAgendamento")
        self.horizontalLayout_4.addWidget(self.bttAgendamento)
        self.bttSemanal = QtWidgets.QPushButton(self.frame_31)
        self.bttSemanal.setMinimumSize(QtCore.QSize(150, 100))
        self.bttSemanal.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bttSemanal.setStyleSheet("QPushButton{\n"
        "    font: 16pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:50px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttSemanal.setObjectName("bttSemanal")
        self.horizontalLayout_4.addWidget(self.bttSemanal)
        self.bttDevolucoes = QtWidgets.QPushButton(self.frame_31)
        self.bttDevolucoes.setMinimumSize(QtCore.QSize(150, 100))
        self.bttDevolucoes.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bttDevolucoes.setStyleSheet("QPushButton{\n"
        "    font: 16pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:50px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttDevolucoes.setObjectName("bttDevolucoes")
        self.horizontalLayout_4.addWidget(self.bttDevolucoes)
        self.bttContrato = QtWidgets.QPushButton(self.frame_31)
        self.bttContrato.setMinimumSize(QtCore.QSize(150, 100))
        self.bttContrato.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bttContrato.setStyleSheet("QPushButton{\n"
        "    font: 16pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:50px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttContrato.setObjectName("bttContrato")
        self.horizontalLayout_4.addWidget(self.bttContrato)
        self.verticalLayout_3.addWidget(self.frame_31)
        self.verticalLayout_2.addWidget(self.frame_28)
        self.horizontalLayout_2.addWidget(self.widget)
        self.verticalLayout_15.addWidget(self.frame_27)
        self.stackedWidget.addWidget(self.pg_home)
        self.pg_cadastro = QtWidgets.QWidget()
        self.pg_cadastro.setMinimumSize(QtCore.QSize(0, 0))
        self.pg_cadastro.setObjectName("pg_cadastro")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.pg_cadastro)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_50 = QtWidgets.QFrame(self.pg_cadastro)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_50)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_51 = QtWidgets.QFrame(self.frame_50)
        self.frame_51.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_52 = QtWidgets.QFrame(self.frame_51)
        self.frame_52.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelCadastroC_2 = QtWidgets.QLabel(self.frame_52)
        self.labelCadastroC_2.setMinimumSize(QtCore.QSize(50, 0))
        self.labelCadastroC_2.setStyleSheet("font: 20pt \"Sofia\";")
        self.labelCadastroC_2.setLineWidth(0)
        self.labelCadastroC_2.setObjectName("labelCadastroC_2")
        self.horizontalLayout_10.addWidget(self.labelCadastroC_2)
        self.bttInicioCC = QtWidgets.QPushButton(self.frame_52)
        self.bttInicioCC.setMinimumSize(QtCore.QSize(50, 50))
        self.bttInicioCC.setMaximumSize(QtCore.QSize(60, 50))
        self.bttInicioCC.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttInicioCC.setObjectName("bttInicioCC")
        self.horizontalLayout_10.addWidget(self.bttInicioCC)
        self.verticalLayout_9.addWidget(self.frame_52)
        self.frame_53 = QtWidgets.QFrame(self.frame_51)
        self.frame_53.setMinimumSize(QtCore.QSize(500, 500))
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setLineWidth(0)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_11.setHorizontalSpacing(10)
        self.gridLayout_11.setVerticalSpacing(15)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.lineEditEnderecoCC = MyLineEdit(self.frame_53)
        self.lineEditEnderecoCC.setMinimumSize(QtCore.QSize(450, 20))
        self.lineEditEnderecoCC.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEditEnderecoCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditEnderecoCC.setObjectName("lineEditEnderecoCC")
        self.gridLayout_17.addWidget(self.lineEditEnderecoCC, 0, 0, 1, 1)
        self.lineEditComplementoCC = MyLineEdit(self.frame_53)
        self.lineEditComplementoCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditComplementoCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditComplementoCC.setText("")
        self.lineEditComplementoCC.setObjectName("lineEditComplementoCC")
        self.gridLayout_17.addWidget(self.lineEditComplementoCC, 0, 4, 1, 1)
        self.lineEditNumeroCC = MyLineEdit(self.frame_53)
        self.lineEditNumeroCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNumeroCC.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditNumeroCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditNumeroCC.setObjectName("lineEditNumeroCC")
        self.gridLayout_17.addWidget(self.lineEditNumeroCC, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_53)
        self.label_17.setMinimumSize(QtCore.QSize(180, 30))
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_17.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_17.addWidget(self.label_17, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame_53)
        self.label_19.setMinimumSize(QtCore.QSize(120, 30))
        self.label_19.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_19.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.gridLayout_17.addWidget(self.label_19, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem, 0, 5, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_17, 4, 1, 1, 1)
        self.gridLayout_19 = QtWidgets.QGridLayout()
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.lineEditCidadeCC = MyLineEdit(self.frame_53)
        self.lineEditCidadeCC.setMinimumSize(QtCore.QSize(140, 20))
        self.lineEditCidadeCC.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lineEditCidadeCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditCidadeCC.setObjectName("lineEditCidadeCC")
        self.gridLayout_19.addWidget(self.lineEditCidadeCC, 0, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.frame_53)
        self.label_29.setMinimumSize(QtCore.QSize(100, 30))
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_29.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_29.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_19.addWidget(self.label_29, 0, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.frame_53)
        self.label_30.setMinimumSize(QtCore.QSize(120, 30))
        self.label_30.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_30.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_30.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_19.addWidget(self.label_30, 0, 1, 1, 1)
        self.lineEditBairroCC = MyLineEdit(self.frame_53)
        self.lineEditBairroCC.setMinimumSize(QtCore.QSize(200, 20))
        self.lineEditBairroCC.setMaximumSize(QtCore.QSize(200, 16777215))
        self.lineEditBairroCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditBairroCC.setObjectName("lineEditBairroCC")
        self.gridLayout_19.addWidget(self.lineEditBairroCC, 0, 0, 1, 1)
        self.lineEditEstadoCC = MyLineEdit(self.frame_53)
        self.lineEditEstadoCC.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditEstadoCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditEstadoCC.setObjectName("lineEditEstadoCC")
        self.gridLayout_19.addWidget(self.lineEditEstadoCC, 0, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem1, 0, 5, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_19, 5, 1, 1, 1)
        self.gridLayout_23 = QtWidgets.QGridLayout()
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.lineEditTelefone2CC = MyLineEdit(self.frame_53)
        self.lineEditTelefone2CC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditTelefone2CC.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditTelefone2CC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditTelefone2CC.setObjectName("lineEditTelefone2CC")
        self.gridLayout_23.addWidget(self.lineEditTelefone2CC, 0, 9, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.frame_53)
        self.label_31.setMinimumSize(QtCore.QSize(0, 30))
        self.label_31.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_31.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_31.setObjectName("label_31")
        self.gridLayout_23.addWidget(self.label_31, 0, 5, 1, 1)
        self.lineEditTelefone1CC = MyLineEdit(self.frame_53)
        self.lineEditTelefone1CC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditTelefone1CC.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditTelefone1CC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditTelefone1CC.setObjectName("lineEditTelefone1CC")
        self.gridLayout_23.addWidget(self.lineEditTelefone1CC, 0, 3, 1, 1)
        self.lineEditDDD2CC = MyLineEdit(self.frame_53)
        self.lineEditDDD2CC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDD2CC.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditDDD2CC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDD2CC.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDDD2CC.setObjectName("lineEditDDD2CC")
        self.gridLayout_23.addWidget(self.lineEditDDD2CC, 0, 7, 1, 1)
        self.lineEditDDD1CC = MyLineEdit(self.frame_53)
        self.lineEditDDD1CC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDD1CC.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditDDD1CC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDD1CC.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDDD1CC.setObjectName("lineEditDDD1CC")
        self.gridLayout_23.addWidget(self.lineEditDDD1CC, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem2, 0, 4, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.frame_53)
        self.label_32.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_32.setObjectName("label_32")
        self.gridLayout_23.addWidget(self.label_32, 0, 8, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.frame_53)
        self.label_33.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_33.setObjectName("label_33")
        self.gridLayout_23.addWidget(self.label_33, 0, 6, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.frame_53)
        self.label_37.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_37.setObjectName("label_37")
        self.gridLayout_23.addWidget(self.label_37, 0, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.frame_53)
        self.label_38.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_38.setObjectName("label_38")
        self.gridLayout_23.addWidget(self.label_38, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem3, 0, 10, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_23, 6, 1, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.frame_53)
        self.label_47.setMinimumSize(QtCore.QSize(0, 30))
        self.label_47.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_47.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_47.setObjectName("label_47")
        self.gridLayout_11.addWidget(self.label_47, 2, 0, 1, 1)
        self.gridLayout_29 = QtWidgets.QGridLayout()
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.lineEditDiaNCC = MyLineEdit(self.frame_53)
        self.lineEditDiaNCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDiaNCC.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEditDiaNCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDiaNCC.setObjectName("lineEditDiaNCC")
        self.gridLayout_29.addWidget(self.lineEditDiaNCC, 0, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.frame_53)
        self.label_42.setObjectName("label_42")
        self.gridLayout_29.addWidget(self.label_42, 0, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.frame_53)
        self.label_45.setObjectName("label_45")
        self.gridLayout_29.addWidget(self.label_45, 0, 3, 1, 1)
        self.lineEditMesNCC = MyLineEdit(self.frame_53)
        self.lineEditMesNCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditMesNCC.setMaximumSize(QtCore.QSize(50, 50))
        self.lineEditMesNCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditMesNCC.setObjectName("lineEditMesNCC")
        self.gridLayout_29.addWidget(self.lineEditMesNCC, 0, 2, 1, 1)
        self.lineEditAnoNCC = MyLineEdit(self.frame_53)
        self.lineEditAnoNCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditAnoNCC.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditAnoNCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditAnoNCC.setText("")
        self.lineEditAnoNCC.setObjectName("lineEditAnoNCC")
        self.gridLayout_29.addWidget(self.lineEditAnoNCC, 0, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem4, 0, 5, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_29, 1, 1, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.frame_53)
        self.label_59.setMinimumSize(QtCore.QSize(0, 30))
        self.label_59.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_59.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_59.setObjectName("label_59")
        self.gridLayout_11.addWidget(self.label_59, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_53)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.frame_53)
        self.label_69.setMinimumSize(QtCore.QSize(0, 30))
        self.label_69.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_69.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_69.setObjectName("label_69")
        self.gridLayout_11.addWidget(self.label_69, 3, 0, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.frame_53)
        self.label_67.setMinimumSize(QtCore.QSize(0, 30))
        self.label_67.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_67.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_67.setObjectName("label_67")
        self.gridLayout_11.addWidget(self.label_67, 4, 0, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.frame_53)
        self.label_66.setMinimumSize(QtCore.QSize(0, 30))
        self.label_66.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_66.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_66.setObjectName("label_66")
        self.gridLayout_11.addWidget(self.label_66, 6, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.frame_53)
        self.label_68.setMinimumSize(QtCore.QSize(0, 30))
        self.label_68.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_68.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_68.setObjectName("label_68")
        self.gridLayout_11.addWidget(self.label_68, 5, 0, 1, 1)
        self.gridLayout_35 = QtWidgets.QGridLayout()
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.bttBuscarCEPCC = QtWidgets.QPushButton(self.frame_53)
        self.bttBuscarCEPCC.setMinimumSize(QtCore.QSize(80, 0))
        self.bttBuscarCEPCC.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttBuscarCEPCC.setObjectName("bttBuscarCEPCC")
        self.gridLayout_35.addWidget(self.bttBuscarCEPCC, 0, 1, 1, 1)
        self.lineEditCEPCC = MyLineEdit(self.frame_53)
        self.lineEditCEPCC.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditCEPCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditCEPCC.setObjectName("lineEditCEPCC")
        self.gridLayout_35.addWidget(self.lineEditCEPCC, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem5, 0, 2, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_35, 3, 1, 1, 1)
        self.gridLayout_43 = QtWidgets.QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.lineEditCPFCC = MyLineEdit(self.frame_53)
        self.lineEditCPFCC.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditCPFCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditCPFCC.setObjectName("lineEditCPFCC")
        self.gridLayout_43.addWidget(self.lineEditCPFCC, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_43.addItem(spacerItem6, 0, 2, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.frame_53)
        self.label_70.setMinimumSize(QtCore.QSize(0, 30))
        self.label_70.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_70.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_70.setObjectName("label_70")
        self.gridLayout_43.addWidget(self.label_70, 0, 3, 1, 1)
        self.lineEditRGCC = MyLineEdit(self.frame_53)
        self.lineEditRGCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditRGCC.setMaximumSize(QtCore.QSize(150, 30))
        self.lineEditRGCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditRGCC.setObjectName("lineEditRGCC")
        self.gridLayout_43.addWidget(self.lineEditRGCC, 0, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_43.addItem(spacerItem7, 0, 5, 1, 1)
        self.bttBuscarCPFCC = QtWidgets.QPushButton(self.frame_53)
        self.bttBuscarCPFCC.setMinimumSize(QtCore.QSize(80, 0))
        self.bttBuscarCPFCC.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttBuscarCPFCC.setObjectName("bttBuscarCPFCC")
        self.gridLayout_43.addWidget(self.bttBuscarCPFCC, 0, 1, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_43, 2, 1, 1, 1)
        self.lineEditNomeCC = MyLineEdit(self.frame_53)
        self.lineEditNomeCC.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNomeCC.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEditNomeCC.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditNomeCC.setObjectName("lineEditNomeCC")
        self.gridLayout_11.addWidget(self.lineEditNomeCC, 0, 1, 1, 1)
        self.verticalLayout_17.addLayout(self.gridLayout_11)
        self.frame_54 = QtWidgets.QFrame(self.frame_53)
        self.frame_54.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.bttCadastarCC = QtWidgets.QPushButton(self.frame_54)
        self.bttCadastarCC.setGeometry(QtCore.QRect(60, 50, 141, 71))
        self.bttCadastarCC.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttCadastarCC.setObjectName("bttCadastarCC")
        self.bttAtualizarCC = QtWidgets.QPushButton(self.frame_54)
        self.bttAtualizarCC.setGeometry(QtCore.QRect(290, 50, 141, 71))
        self.bttAtualizarCC.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttAtualizarCC.setObjectName("bttAtualizarCC")
        self.verticalLayout_17.addWidget(self.frame_54)
        self.verticalLayout_9.addWidget(self.frame_53)
        self.verticalLayout_16.addWidget(self.frame_51)
        self.horizontalLayout_8.addWidget(self.frame_50)
        self.stackedWidget.addWidget(self.pg_cadastro)
        self.pg_agendamento = QtWidgets.QWidget()
        self.pg_agendamento.setObjectName("pg_agendamento")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.pg_agendamento)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_55 = QtWidgets.QFrame(self.pg_agendamento)
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_55)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_56 = QtWidgets.QFrame(self.frame_55)
        self.frame_56.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_56)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_71 = QtWidgets.QLabel(self.frame_56)
        self.label_71.setStyleSheet("font: 20pt \"Sofia\";")
        self.label_71.setObjectName("label_71")
        self.horizontalLayout_22.addWidget(self.label_71)
        self.bttInicioA = QtWidgets.QPushButton(self.frame_56)
        self.bttInicioA.setMinimumSize(QtCore.QSize(50, 50))
        self.bttInicioA.setMaximumSize(QtCore.QSize(60, 50))
        self.bttInicioA.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttInicioA.setObjectName("bttInicioA")
        self.horizontalLayout_22.addWidget(self.bttInicioA)
        self.verticalLayout_19.addWidget(self.frame_56)
        self.frame_57 = QtWidgets.QFrame(self.frame_55)
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_57)
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.gridLayout_44 = QtWidgets.QGridLayout()
        self.gridLayout_44.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_44.setHorizontalSpacing(10)
        self.gridLayout_44.setVerticalSpacing(15)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.lineEditNomeA = MyLineEdit(self.frame_57)
        self.lineEditNomeA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNomeA.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEditNomeA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditNomeA.setObjectName("lineEditNomeA")
        self.gridLayout_44.addWidget(self.lineEditNomeA, 0, 1, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.frame_57)
        self.label_74.setMinimumSize(QtCore.QSize(0, 30))
        self.label_74.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_74.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_74.setObjectName("label_74")
        self.gridLayout_44.addWidget(self.label_74, 2, 0, 1, 1)
        self.gridLayout_46 = QtWidgets.QGridLayout()
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.lineEditCPFA = MyLineEdit(self.frame_57)
        self.lineEditCPFA.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditCPFA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditCPFA.setObjectName("lineEditCPFA")
        self.gridLayout_46.addWidget(self.lineEditCPFA, 0, 0, 1, 1)
        self.bttBuscarCPFA = QtWidgets.QPushButton(self.frame_57)
        self.bttBuscarCPFA.setMinimumSize(QtCore.QSize(80, 0))
        self.bttBuscarCPFA.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttBuscarCPFA.setObjectName("bttBuscarCPFA")
        self.gridLayout_46.addWidget(self.bttBuscarCPFA, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_46.addItem(spacerItem8, 0, 2, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_46, 1, 1, 1, 1)
        self.gridLayout_45 = QtWidgets.QGridLayout()
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.lineEditEnderecoA = MyLineEdit(self.frame_57)
        self.lineEditEnderecoA.setMinimumSize(QtCore.QSize(450, 20))
        self.lineEditEnderecoA.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEditEnderecoA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditEnderecoA.setObjectName("lineEditEnderecoA")
        self.gridLayout_45.addWidget(self.lineEditEnderecoA, 0, 0, 1, 1)
        self.lineEditComplementoA = MyLineEdit(self.frame_57)
        self.lineEditComplementoA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditComplementoA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditComplementoA.setText("")
        self.lineEditComplementoA.setObjectName("lineEditComplementoA")
        self.gridLayout_45.addWidget(self.lineEditComplementoA, 0, 4, 1, 1)
        self.lineEditNumeroA = MyLineEdit(self.frame_57)
        self.lineEditNumeroA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNumeroA.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditNumeroA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditNumeroA.setObjectName("lineEditNumeroA")
        self.gridLayout_45.addWidget(self.lineEditNumeroA, 0, 2, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.frame_57)
        self.label_72.setMinimumSize(QtCore.QSize(180, 30))
        self.label_72.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_72.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_72.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_72.setObjectName("label_72")
        self.gridLayout_45.addWidget(self.label_72, 0, 3, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.frame_57)
        self.label_73.setMinimumSize(QtCore.QSize(120, 30))
        self.label_73.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_73.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_73.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_73.setObjectName("label_73")
        self.gridLayout_45.addWidget(self.label_73, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_45.addItem(spacerItem9, 0, 5, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_45, 2, 1, 1, 1)
        self.gridLayout_47 = QtWidgets.QGridLayout()
        self.gridLayout_47.setObjectName("gridLayout_47")
        self.label_75 = QtWidgets.QLabel(self.frame_57)
        self.label_75.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_75.setObjectName("label_75")
        self.gridLayout_47.addWidget(self.label_75, 0, 0, 1, 1)
        self.lineEditDDD1A = MyLineEdit(self.frame_57)
        self.lineEditDDD1A.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDD1A.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditDDD1A.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDD1A.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDDD1A.setObjectName("lineEditDDD1A")
        self.gridLayout_47.addWidget(self.lineEditDDD1A, 0, 1, 1, 1)
        self.lineEditTelefone1A = MyLineEdit(self.frame_57)
        self.lineEditTelefone1A.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditTelefone1A.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditTelefone1A.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditTelefone1A.setObjectName("lineEditTelefone1A")
        self.gridLayout_47.addWidget(self.lineEditTelefone1A, 0, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_47.addItem(spacerItem10, 0, 4, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.frame_57)
        self.label_76.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_76.setObjectName("label_76")
        self.gridLayout_47.addWidget(self.label_76, 0, 2, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_47, 3, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.frame_57)
        self.label_77.setMinimumSize(QtCore.QSize(0, 30))
        self.label_77.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_77.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_77.setObjectName("label_77")
        self.gridLayout_44.addWidget(self.label_77, 0, 0, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.frame_57)
        self.label_78.setMinimumSize(QtCore.QSize(0, 30))
        self.label_78.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_78.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_78.setObjectName("label_78")
        self.gridLayout_44.addWidget(self.label_78, 1, 0, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.frame_57)
        self.label_83.setMinimumSize(QtCore.QSize(0, 30))
        self.label_83.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_83.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_83.setObjectName("label_83")
        self.gridLayout_44.addWidget(self.label_83, 4, 0, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.frame_57)
        self.label_82.setMinimumSize(QtCore.QSize(0, 30))
        self.label_82.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_82.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_82.setObjectName("label_82")
        self.gridLayout_44.addWidget(self.label_82, 3, 0, 1, 1)
        self.gridLayout_49 = QtWidgets.QGridLayout()
        self.gridLayout_49.setObjectName("gridLayout_49")
        self.comboBoxEventoA = QtWidgets.QComboBox(self.frame_57)
        self.comboBoxEventoA.setMinimumSize(QtCore.QSize(250, 30))
        self.comboBoxEventoA.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "")
        self.comboBoxEventoA.setCurrentText("")
        self.comboBoxEventoA.setObjectName("comboBoxEventoA")
        self.gridLayout_49.addWidget(self.comboBoxEventoA, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_49.addItem(spacerItem11, 0, 5, 1, 1)
        self.bttBuscarEventoA = QtWidgets.QPushButton(self.frame_57)
        self.bttBuscarEventoA.setMinimumSize(QtCore.QSize(80, 0))
        self.bttBuscarEventoA.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "    margin-left:10px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttBuscarEventoA.setObjectName("bttBuscarEventoA")
        self.gridLayout_49.addWidget(self.bttBuscarEventoA, 0, 2, 1, 1)
        self.lineEditEventoA = MyLineEdit(self.frame_57)
        self.lineEditEventoA.setStyleSheet("font: 12pt \"Century Gothic\";background:transparent;border:0px;")
        self.lineEditEventoA.setObjectName("lineEditEventoA")
        self.lineEditEventoA.setReadOnly(True)
        self.gridLayout_49.addWidget(self.lineEditEventoA, 0, 4, 1, 1)
        self.bttCriarEventoA = QtWidgets.QPushButton(self.frame_57)
        self.bttCriarEventoA.setMinimumSize(QtCore.QSize(80, 0))
        self.bttCriarEventoA.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "    margin-left:10px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttCriarEventoA.setObjectName("bttCriarEventoA")
        self.gridLayout_49.addWidget(self.bttCriarEventoA, 0, 3, 1, 1)
        self.gridLayout_44.addLayout(self.gridLayout_49, 4, 1, 1, 1)
        self.horizontalLayout_23.addLayout(self.gridLayout_44)
        self.verticalLayout_19.addWidget(self.frame_57)
        self.frame_58 = QtWidgets.QFrame(self.frame_55)
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_58)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.frame_59 = QtWidgets.QFrame(self.frame_58)
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_59)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_85 = QtWidgets.QLabel(self.frame_59)
        self.label_85.setMinimumSize(QtCore.QSize(0, 30))
        self.label_85.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_85.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_85.setObjectName("label_85")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_85)
        self.textEditDescricaoA = QtWidgets.QTextEdit(self.frame_59)
        self.textEditDescricaoA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.textEditDescricaoA.setObjectName("textEditDescricaoA")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEditDescricaoA)
        self.label_88 = QtWidgets.QLabel(self.frame_59)
        self.label_88.setMinimumSize(QtCore.QSize(0, 30))
        self.label_88.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_88.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_88.setObjectName("label_88")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_88)
        self.textEditAcessoriosA = QtWidgets.QTextEdit(self.frame_59)
        self.textEditAcessoriosA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.textEditAcessoriosA.setObjectName("textEditAcessoriosA")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditAcessoriosA)
        self.label_89 = QtWidgets.QLabel(self.frame_59)
        self.label_89.setMinimumSize(QtCore.QSize(0, 30))
        self.label_89.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_89.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_89.setObjectName("label_89")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_89)
        self.textEditAjustesA = QtWidgets.QTextEdit(self.frame_59)
        self.textEditAjustesA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.textEditAjustesA.setObjectName("textEditAjustesA")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEditAjustesA)
        self.horizontalLayout_25.addLayout(self.formLayout_3)
        self.horizontalLayout_24.addWidget(self.frame_59)
        self.frame_60 = QtWidgets.QFrame(self.frame_58)
        self.frame_60.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_60)
        self.verticalLayout_20.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_61 = QtWidgets.QFrame(self.frame_60)
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_61)
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_92 = QtWidgets.QLabel(self.frame_61)
        self.label_92.setMinimumSize(QtCore.QSize(135, 30))
        self.label_92.setMaximumSize(QtCore.QSize(135, 30))
        self.label_92.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_92.setObjectName("label_92")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_92)
        self.gridLayout_50 = QtWidgets.QGridLayout()
        self.gridLayout_50.setObjectName("gridLayout_50")
        self.label_95 = QtWidgets.QLabel(self.frame_61)
        self.label_95.setMinimumSize(QtCore.QSize(30, 30))
        self.label_95.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_95.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_95.setAlignment(QtCore.Qt.AlignCenter)
        self.label_95.setObjectName("label_95")
        self.gridLayout_50.addWidget(self.label_95, 0, 0, 1, 1)
        self.lineEditValorA = MyLineEdit(self.frame_61)
        self.lineEditValorA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditValorA.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditValorA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditValorA.setObjectName("lineEditValorA")
        self.gridLayout_50.addWidget(self.lineEditValorA, 0, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_50.addItem(spacerItem12, 0, 2, 1, 1)
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_50)
        self.label_113 = QtWidgets.QLabel(self.frame_61)
        self.label_113.setMinimumSize(QtCore.QSize(135, 30))
        self.label_113.setMaximumSize(QtCore.QSize(135, 30))
        self.label_113.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_113.setObjectName("label_113")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_113)
        self.gridLayout_52 = QtWidgets.QGridLayout()
        self.gridLayout_52.setObjectName("gridLayout_52")
        spacerItem13 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_52.addItem(spacerItem13, 0, 0, 1, 1)
        self.lineEditDescontoA = MyLineEdit(self.frame_61)
        self.lineEditDescontoA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDescontoA.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDescontoA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDescontoA.setObjectName("lineEditDescontoA")
        self.gridLayout_52.addWidget(self.lineEditDescontoA, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_52.addItem(spacerItem14, 0, 2, 1, 1)
        self.formLayout_6.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_52)
        self.label_114 = QtWidgets.QLabel(self.frame_61)
        self.label_114.setMinimumSize(QtCore.QSize(135, 30))
        self.label_114.setMaximumSize(QtCore.QSize(135, 30))
        self.label_114.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_114.setObjectName("label_114")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_114)
        self.gridLayout_53 = QtWidgets.QGridLayout()
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.label_115 = QtWidgets.QLabel(self.frame_61)
        self.label_115.setMinimumSize(QtCore.QSize(30, 30))
        self.label_115.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_115.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_115.setAlignment(QtCore.Qt.AlignCenter)
        self.label_115.setObjectName("label_115")
        self.gridLayout_53.addWidget(self.label_115, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_53.addItem(spacerItem15, 0, 2, 1, 1)
        self.lineEditSinalA = MyLineEdit(self.frame_61)
        self.lineEditSinalA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditSinalA.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditSinalA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditSinalA.setObjectName("lineEditSinalA")
        self.gridLayout_53.addWidget(self.lineEditSinalA, 0, 1, 1, 1)
        self.formLayout_6.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.gridLayout_53)
        self.label_116 = QtWidgets.QLabel(self.frame_61)
        self.label_116.setMinimumSize(QtCore.QSize(135, 30))
        self.label_116.setMaximumSize(QtCore.QSize(135, 30))
        self.label_116.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_116.setObjectName("label_116")
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_116)
        self.gridLayout_54 = QtWidgets.QGridLayout()
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.label_117 = QtWidgets.QLabel(self.frame_61)
        self.label_117.setMinimumSize(QtCore.QSize(0, 30))
        self.label_117.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_117.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_117.setAlignment(QtCore.Qt.AlignCenter)
        self.label_117.setObjectName("label_117")
        self.gridLayout_54.addWidget(self.label_117, 0, 2, 1, 1)
        self.label_118 = QtWidgets.QLabel(self.frame_61)
        self.label_118.setMinimumSize(QtCore.QSize(0, 30))
        self.label_118.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_118.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_118.setAlignment(QtCore.Qt.AlignCenter)
        self.label_118.setObjectName("label_118")
        self.gridLayout_54.addWidget(self.label_118, 0, 4, 1, 1)
        self.lineEditDEDiaA = MyLineEdit(self.frame_61)
        self.lineEditDEDiaA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDEDiaA.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditDEDiaA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDEDiaA.setObjectName("lineEditDEDiaA")
        self.gridLayout_54.addWidget(self.lineEditDEDiaA, 0, 1, 1, 1)
        self.lineEditDEAnoA = MyLineEdit(self.frame_61)
        self.lineEditDEAnoA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDEAnoA.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDEAnoA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDEAnoA.setObjectName("lineEditDEAnoA")
        self.gridLayout_54.addWidget(self.lineEditDEAnoA, 0, 5, 1, 1)
        self.lineEditDEMesA = MyLineEdit(self.frame_61)
        self.lineEditDEMesA.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDEMesA.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditDEMesA.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDEMesA.setObjectName("lineEditDEMesA")
        self.gridLayout_54.addWidget(self.lineEditDEMesA, 0, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem16, 0, 6, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem17, 0, 0, 1, 1)
        self.formLayout_6.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.gridLayout_54)
        self.verticalLayout_30.addLayout(self.formLayout_6)
        self.frame_62 = QtWidgets.QFrame(self.frame_61)
        self.frame_62.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_62)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.verticalLayout_30.addWidget(self.frame_62)
        self.verticalLayout_20.addWidget(self.frame_61)
        self.frame_63 = QtWidgets.QFrame(self.frame_60)
        self.frame_63.setMinimumSize(QtCore.QSize(200, 50))
        self.frame_63.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_63.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.bttGerarReciboA_2 = QtWidgets.QPushButton(self.frame_63)
        self.bttGerarReciboA_2.setGeometry(QtCore.QRect(179, 10, 120, 40))
        self.bttGerarReciboA_2.setMinimumSize(QtCore.QSize(120, 30))
        self.bttGerarReciboA_2.setMaximumSize(QtCore.QSize(120, 40))
        self.bttGerarReciboA_2.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttGerarReciboA_2.setObjectName("bttGerarReciboA_2")
        self.bttConcluirA_2 = QtWidgets.QPushButton(self.frame_63)
        self.bttConcluirA_2.setGeometry(QtCore.QRect(330, 10, 120, 40))
        self.bttConcluirA_2.setMinimumSize(QtCore.QSize(120, 30))
        self.bttConcluirA_2.setMaximumSize(QtCore.QSize(120, 40))
        self.bttConcluirA_2.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttConcluirA_2.setObjectName("bttConcluirA_2")

        self.bttAtualizarA_2 = QtWidgets.QPushButton(self.frame_63)
        self.bttAtualizarA_2.setGeometry(QtCore.QRect(481, 10, 120, 40))
        self.bttAtualizarA_2.setMinimumSize(QtCore.QSize(120, 30))
        self.bttAtualizarA_2.setMaximumSize(QtCore.QSize(120, 40))
        self.bttAtualizarA_2.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttAtualizarA_2.setObjectName("bttAtualizarA_2")

        self.verticalLayout_20.addWidget(self.frame_63)
        self.horizontalLayout_24.addWidget(self.frame_60)
        self.verticalLayout_19.addWidget(self.frame_58)
        self.verticalLayout_18.addWidget(self.frame_55)
        self.stackedWidget.addWidget(self.pg_agendamento)
        self.pg_entregas = QtWidgets.QWidget()
        self.pg_entregas.setObjectName("pg_entregas")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.pg_entregas)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_64 = QtWidgets.QFrame(self.pg_entregas)
        self.frame_64.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_64.setObjectName("frame_64")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_64)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.frame_65 = QtWidgets.QFrame(self.frame_64)
        self.frame_65.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_65)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.gridLayout_55 = QtWidgets.QGridLayout()
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.label_119 = QtWidgets.QLabel(self.frame_65)
        self.label_119.setStyleSheet("font: 20pt \"Sofia\";")
        self.label_119.setObjectName("label_119")
        self.gridLayout_55.addWidget(self.label_119, 0, 0, 1, 1)
        self.horizontalLayout_26.addLayout(self.gridLayout_55)
        self.bttInicioSE = QtWidgets.QPushButton(self.frame_65)
        self.bttInicioSE.setMinimumSize(QtCore.QSize(50, 50))
        self.bttInicioSE.setMaximumSize(QtCore.QSize(60, 50))
        self.bttInicioSE.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttInicioSE.setObjectName("bttInicioSE")
        self.horizontalLayout_26.addWidget(self.bttInicioSE)
        self.verticalLayout_35.addWidget(self.frame_65)
        self.frame_66 = QtWidgets.QFrame(self.frame_64)
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.frame_66)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.labelSegundaSE_2 = QtWidgets.QLabel(self.frame_66)
        self.labelSegundaSE_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelSegundaSE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSegundaSE_2.setObjectName("labelSegundaSE_2")
        self.gridLayout_56.addWidget(self.labelSegundaSE_2, 0, 0, 1, 1)
        self.labelTercaSE_2 = QtWidgets.QLabel(self.frame_66)
        self.labelTercaSE_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelTercaSE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTercaSE_2.setObjectName("labelTercaSE_2")
        self.gridLayout_56.addWidget(self.labelTercaSE_2, 0, 1, 1, 1)
        self.labelQuartaSE_2 = QtWidgets.QLabel(self.frame_66)
        self.labelQuartaSE_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelQuartaSE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuartaSE_2.setObjectName("labelQuartaSE_2")
        self.gridLayout_56.addWidget(self.labelQuartaSE_2, 0, 2, 1, 1)
        self.labelQuintaSE_2 = QtWidgets.QLabel(self.frame_66)
        self.labelQuintaSE_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelQuintaSE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuintaSE_2.setObjectName("labelQuintaSE_2")
        self.gridLayout_56.addWidget(self.labelQuintaSE_2, 0, 3, 1, 1)
        self.labelSextaSE_2 = QtWidgets.QLabel(self.frame_66)
        self.labelSextaSE_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelSextaSE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSextaSE_2.setObjectName("labelSextaSE_2")
        self.gridLayout_56.addWidget(self.labelSextaSE_2, 0, 4, 1, 1)
        self.labelSabadoSE_2 = QtWidgets.QLabel(self.frame_66)
        self.labelSabadoSE_2.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelSabadoSE_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSabadoSE_2.setObjectName("labelSabadoSE_2")
        self.gridLayout_56.addWidget(self.labelSabadoSE_2, 0, 5, 1, 1)
        self.frame_67 = QtWidgets.QFrame(self.frame_66)
        self.frame_67.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_67)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.entregas_segunda = QtWidgets.QListWidget(self.frame_67)
        self.entregas_segunda.setObjectName("entregas_segunda")
        self.horizontalLayout_27.addWidget(self.entregas_segunda)
        self.gridLayout_56.addWidget(self.frame_67, 1, 0, 1, 1)
        self.frame_68 = QtWidgets.QFrame(self.frame_66)
        self.frame_68.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_68.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_68.setObjectName("frame_68")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_68)
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.entregas_terca = QtWidgets.QListWidget(self.frame_68)
        self.entregas_terca.setObjectName("entregas_terca")
        self.horizontalLayout_28.addWidget(self.entregas_terca)
        self.gridLayout_56.addWidget(self.frame_68, 1, 1, 1, 1)
        self.frame_69 = QtWidgets.QFrame(self.frame_66)
        self.frame_69.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_69.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_69.setObjectName("frame_69")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_69)
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.entregas_quarta = QtWidgets.QListWidget(self.frame_69)
        self.entregas_quarta.setObjectName("entregas_quarta")
        self.horizontalLayout_29.addWidget(self.entregas_quarta)
        self.gridLayout_56.addWidget(self.frame_69, 1, 2, 1, 1)
        self.frame_70 = QtWidgets.QFrame(self.frame_66)
        self.frame_70.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_70.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_70.setObjectName("frame_70")
        self.horizontalLayout_43 = QtWidgets.QHBoxLayout(self.frame_70)
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName("horizontalLayout_43")
        self.entregas_quinta = QtWidgets.QListWidget(self.frame_70)
        self.entregas_quinta.setObjectName("entregas_quinta")
        self.horizontalLayout_43.addWidget(self.entregas_quinta)
        self.gridLayout_56.addWidget(self.frame_70, 1, 3, 1, 1)
        self.frame_71 = QtWidgets.QFrame(self.frame_66)
        self.frame_71.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_71.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_71.setObjectName("frame_71")
        self.horizontalLayout_44 = QtWidgets.QHBoxLayout(self.frame_71)
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName("horizontalLayout_44")
        self.entregas_sexta = QtWidgets.QListWidget(self.frame_71)
        self.entregas_sexta.setObjectName("entregas_sexta")
        self.horizontalLayout_44.addWidget(self.entregas_sexta)
        self.gridLayout_56.addWidget(self.frame_71, 1, 4, 1, 1)
        self.frame_72 = QtWidgets.QFrame(self.frame_66)
        self.frame_72.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_72.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_72.setObjectName("frame_72")
        self.horizontalLayout_45 = QtWidgets.QHBoxLayout(self.frame_72)
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName("horizontalLayout_45")
        self.entregas_sabado = QtWidgets.QListWidget(self.frame_72)
        self.entregas_sabado.setObjectName("entregas_sabado")
        self.horizontalLayout_45.addWidget(self.entregas_sabado)
        self.gridLayout_56.addWidget(self.frame_72, 1, 5, 1, 1)
        self.verticalLayout_35.addWidget(self.frame_66)
        self.frame_73 = QtWidgets.QFrame(self.frame_64)
        self.frame_73.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.horizontalLayout_46 = QtWidgets.QHBoxLayout(self.frame_73)
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.bttGerarContratoSE = QtWidgets.QPushButton(self.frame_73)
        self.bttGerarContratoSE.setMinimumSize(QtCore.QSize(150, 30))
        self.bttGerarContratoSE.setMaximumSize(QtCore.QSize(150, 45))
        self.bttGerarContratoSE.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttGerarContratoSE.setObjectName("bttGerarContratoSE")
        self.horizontalLayout_46.addWidget(self.bttGerarContratoSE)
        self.bttApagarAgendamentoSE = QtWidgets.QPushButton(self.frame_73)
        self.bttApagarAgendamentoSE.setMinimumSize(QtCore.QSize(150, 30))
        self.bttApagarAgendamentoSE.setMaximumSize(QtCore.QSize(150, 45))
        self.bttApagarAgendamentoSE.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttApagarAgendamentoSE.setObjectName("bttApagarAgendamentoSE")
        self.horizontalLayout_46.addWidget(self.bttApagarAgendamentoSE)
        self.bttEditarAgendamentoSE = QtWidgets.QPushButton(self.frame_73)
        self.bttEditarAgendamentoSE.setMinimumSize(QtCore.QSize(150, 30))
        self.bttEditarAgendamentoSE.setMaximumSize(QtCore.QSize(150, 45))
        self.bttEditarAgendamentoSE.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttEditarAgendamentoSE.setObjectName("bttEditarAgendamentoSE")
        self.horizontalLayout_46.addWidget(self.bttEditarAgendamentoSE)
        self.verticalLayout_35.addWidget(self.frame_73)
        self.verticalLayout_34.addWidget(self.frame_64)
        self.stackedWidget.addWidget(self.pg_entregas)
        self.pg_devolucoes = QtWidgets.QWidget()
        self.pg_devolucoes.setObjectName("pg_devolucoes")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.pg_devolucoes)
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.frame_74 = QtWidgets.QFrame(self.pg_devolucoes)
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.frame_74)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.frame_75 = QtWidgets.QFrame(self.frame_74)
        self.frame_75.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout(self.frame_75)
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.label_120 = QtWidgets.QLabel(self.frame_75)
        self.label_120.setStyleSheet("font: 20pt \"Sofia\";")
        self.label_120.setObjectName("label_120")
        self.gridLayout_57.addWidget(self.label_120, 0, 0, 1, 1)
        self.horizontalLayout_47.addLayout(self.gridLayout_57)
        self.bttInicioDS = QtWidgets.QPushButton(self.frame_75)
        self.bttInicioDS.setMinimumSize(QtCore.QSize(0, 50))
        self.bttInicioDS.setMaximumSize(QtCore.QSize(60, 50))
        self.bttInicioDS.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttInicioDS.setObjectName("bttInicioDS")
        self.horizontalLayout_47.addWidget(self.bttInicioDS)
        self.verticalLayout_37.addWidget(self.frame_75)
        self.frame_76 = QtWidgets.QFrame(self.frame_74)
        self.frame_76.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_76.setObjectName("frame_76")
        self.gridLayout_58 = QtWidgets.QGridLayout(self.frame_76)
        self.gridLayout_58.setObjectName("gridLayout_58")
        self.frame_77 = QtWidgets.QFrame(self.frame_76)
        self.frame_77.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_77.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_77.setObjectName("frame_77")
        self.horizontalLayout_48 = QtWidgets.QHBoxLayout(self.frame_77)
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.devolucoes_sabado = QtWidgets.QListWidget(self.frame_77)
        self.devolucoes_sabado.setObjectName("devolucoes_sabado")
        self.horizontalLayout_48.addWidget(self.devolucoes_sabado)
        self.gridLayout_58.addWidget(self.frame_77, 1, 5, 1, 1)
        self.frame_78 = QtWidgets.QFrame(self.frame_76)
        self.frame_78.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_78.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_78.setObjectName("frame_78")
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout(self.frame_78)
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.devolucoes_quinta = QtWidgets.QListWidget(self.frame_78)
        self.devolucoes_quinta.setObjectName("devolucoes_quinta")
        self.horizontalLayout_49.addWidget(self.devolucoes_quinta)
        self.gridLayout_58.addWidget(self.frame_78, 1, 3, 1, 1)
        self.frame_79 = QtWidgets.QFrame(self.frame_76)
        self.frame_79.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_79.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_79.setObjectName("frame_79")
        self.horizontalLayout_50 = QtWidgets.QHBoxLayout(self.frame_79)
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName("horizontalLayout_50")
        self.devolucoes_sexta = QtWidgets.QListWidget(self.frame_79)
        self.devolucoes_sexta.setObjectName("devolucoes_sexta")
        self.horizontalLayout_50.addWidget(self.devolucoes_sexta)
        self.gridLayout_58.addWidget(self.frame_79, 1, 4, 1, 1)
        self.frame_80 = QtWidgets.QFrame(self.frame_76)
        self.frame_80.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_80.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_80.setObjectName("frame_80")
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout(self.frame_80)
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.devolucoes_segunda = QtWidgets.QListWidget(self.frame_80)
        self.devolucoes_segunda.setObjectName("devolucoes_segunda")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.devolucoes_segunda.addItem(item)
        self.horizontalLayout_51.addWidget(self.devolucoes_segunda)
        self.gridLayout_58.addWidget(self.frame_80, 1, 0, 1, 1)
        self.frame_81 = QtWidgets.QFrame(self.frame_76)
        self.frame_81.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_81.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_81.setObjectName("frame_81")
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout(self.frame_81)
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.devolucoes_terca = QtWidgets.QListWidget(self.frame_81)
        self.devolucoes_terca.setObjectName("devolucoes_terca")
        self.horizontalLayout_52.addWidget(self.devolucoes_terca)
        self.gridLayout_58.addWidget(self.frame_81, 1, 1, 1, 1)
        self.labelSextaDS_3 = QtWidgets.QLabel(self.frame_76)
        self.labelSextaDS_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelSextaDS_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSextaDS_3.setObjectName("labelSextaDS_3")
        self.gridLayout_58.addWidget(self.labelSextaDS_3, 0, 4, 1, 1)
        self.labelQuartaDS_3 = QtWidgets.QLabel(self.frame_76)
        self.labelQuartaDS_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelQuartaDS_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuartaDS_3.setObjectName("labelQuartaDS_3")
        self.gridLayout_58.addWidget(self.labelQuartaDS_3, 0, 2, 1, 1)
        self.labelQuintaDS_3 = QtWidgets.QLabel(self.frame_76)
        self.labelQuintaDS_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelQuintaDS_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelQuintaDS_3.setObjectName("labelQuintaDS_3")
        self.gridLayout_58.addWidget(self.labelQuintaDS_3, 0, 3, 1, 1)
        self.labelTercaDS_3 = QtWidgets.QLabel(self.frame_76)
        self.labelTercaDS_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelTercaDS_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTercaDS_3.setObjectName("labelTercaDS_3")
        self.gridLayout_58.addWidget(self.labelTercaDS_3, 0, 1, 1, 1)
        self.labelSegundaDS_3 = QtWidgets.QLabel(self.frame_76)
        self.labelSegundaDS_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelSegundaDS_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSegundaDS_3.setObjectName("labelSegundaDS_3")
        self.gridLayout_58.addWidget(self.labelSegundaDS_3, 0, 0, 1, 1)
        self.labelSabadoDS_3 = QtWidgets.QLabel(self.frame_76)
        self.labelSabadoDS_3.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.labelSabadoDS_3.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSabadoDS_3.setObjectName("labelSabadoDS_3")
        self.gridLayout_58.addWidget(self.labelSabadoDS_3, 0, 5, 1, 1)
        self.frame_82 = QtWidgets.QFrame(self.frame_76)
        self.frame_82.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_82.setObjectName("frame_82")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout(self.frame_82)
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.devolucoes_quarta = QtWidgets.QListWidget(self.frame_82)
        self.devolucoes_quarta.setObjectName("devolucoes_quarta")
        self.horizontalLayout_53.addWidget(self.devolucoes_quarta)
        self.gridLayout_58.addWidget(self.frame_82, 1, 2, 1, 1)
        self.verticalLayout_37.addWidget(self.frame_76)
        self.frame_83 = QtWidgets.QFrame(self.frame_74)
        self.frame_83.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_83.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_83.setObjectName("frame_83")
        self.horizontalLayout_54 = QtWidgets.QHBoxLayout(self.frame_83)
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.labelMulta = QtWidgets.QLabel(self.frame_83)
        self.labelMulta.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.labelMulta.setFont(font)
        self.labelMulta.setStyleSheet("\n"
        "font: 75 14pt \"Century Gothic\";")
        self.labelMulta.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelMulta.setObjectName("labelMulta")
        self.horizontalLayout_54.addWidget(self.labelMulta)
        self.bttDevolvidoDS = QtWidgets.QPushButton(self.frame_83)
        self.bttDevolvidoDS.setMinimumSize(QtCore.QSize(150, 30))
        self.bttDevolvidoDS.setMaximumSize(QtCore.QSize(150, 45))
        self.bttDevolvidoDS.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttDevolvidoDS.setObjectName("bttDevolvidoDS")
        self.horizontalLayout_54.addWidget(self.bttDevolvidoDS)
        self.verticalLayout_37.addWidget(self.frame_83)
        self.verticalLayout_36.addWidget(self.frame_74)
        self.stackedWidget.addWidget(self.pg_devolucoes)
        self.pg_contrato = QtWidgets.QWidget()
        self.pg_contrato.setObjectName("pg_contrato")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.pg_contrato)
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.frame_84 = QtWidgets.QFrame(self.pg_contrato)
        self.frame_84.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_84.setObjectName("frame_84")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_84)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.frame_85 = QtWidgets.QFrame(self.frame_84)
        self.frame_85.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_85.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_85.setObjectName("frame_85")
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout(self.frame_85)
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.label_121 = QtWidgets.QLabel(self.frame_85)
        self.label_121.setStyleSheet("font: 20pt \"Sofia\";")
        self.label_121.setObjectName("label_121")
        self.horizontalLayout_55.addWidget(self.label_121)
        self.bttInicioCTT = QtWidgets.QPushButton(self.frame_85)
        self.bttInicioCTT.setMinimumSize(QtCore.QSize(50, 50))
        self.bttInicioCTT.setMaximumSize(QtCore.QSize(60, 50))
        self.bttInicioCTT.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:20px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttInicioCTT.setObjectName("bttInicioCTT")
        self.horizontalLayout_55.addWidget(self.bttInicioCTT)
        self.verticalLayout_39.addWidget(self.frame_85)
        self.frame_86 = QtWidgets.QFrame(self.frame_84)
        self.frame_86.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_86.setObjectName("frame_86")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout(self.frame_86)
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.gridLayout_59 = QtWidgets.QGridLayout()
        self.gridLayout_59.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_59.setHorizontalSpacing(10)
        self.gridLayout_59.setVerticalSpacing(15)
        self.gridLayout_59.setObjectName("gridLayout_59")
        self.label_122 = QtWidgets.QLabel(self.frame_86)
        self.label_122.setMinimumSize(QtCore.QSize(0, 30))
        self.label_122.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_122.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_122.setObjectName("label_122")
        self.gridLayout_59.addWidget(self.label_122, 2, 0, 1, 1)
        self.gridLayout_60 = QtWidgets.QGridLayout()
        self.gridLayout_60.setObjectName("gridLayout_60")
        self.lineEditCPFCTT = MyLineEdit(self.frame_86)
        self.lineEditCPFCTT.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditCPFCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditCPFCTT.setObjectName("lineEditCPFCTT")
        self.gridLayout_60.addWidget(self.lineEditCPFCTT, 0, 0, 1, 1)
        self.bttBuscarCPFCTT = QtWidgets.QPushButton(self.frame_86)
        self.bttBuscarCPFCTT.setMinimumSize(QtCore.QSize(80, 0))
        self.bttBuscarCPFCTT.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttBuscarCPFCTT.setObjectName("bttBuscarCPFCTT")
        self.gridLayout_60.addWidget(self.bttBuscarCPFCTT, 0, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_60.addItem(spacerItem18, 0, 2, 1, 1)
        self.gridLayout_59.addLayout(self.gridLayout_60, 1, 1, 1, 1)
        self.lineEditNomeCTT = MyLineEdit(self.frame_86)
        self.lineEditNomeCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNomeCTT.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lineEditNomeCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditNomeCTT.setObjectName("lineEditNomeCTT")
        self.gridLayout_59.addWidget(self.lineEditNomeCTT, 0, 1, 1, 1)
        self.gridLayout_61 = QtWidgets.QGridLayout()
        self.gridLayout_61.setObjectName("gridLayout_61")
        self.lineEditEnderecoCTT = MyLineEdit(self.frame_86)
        self.lineEditEnderecoCTT.setMinimumSize(QtCore.QSize(450, 20))
        self.lineEditEnderecoCTT.setMaximumSize(QtCore.QSize(500, 16777215))
        self.lineEditEnderecoCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditEnderecoCTT.setObjectName("lineEditEnderecoCTT")
        self.gridLayout_61.addWidget(self.lineEditEnderecoCTT, 0, 0, 1, 1)
        self.lineEditComplementoCTT = MyLineEdit(self.frame_86)
        self.lineEditComplementoCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditComplementoCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditComplementoCTT.setText("")
        self.lineEditComplementoCTT.setObjectName("lineEditComplementoCTT")
        self.gridLayout_61.addWidget(self.lineEditComplementoCTT, 0, 4, 1, 1)
        self.lineEditNumeroCTT = MyLineEdit(self.frame_86)
        self.lineEditNumeroCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditNumeroCTT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditNumeroCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditNumeroCTT.setObjectName("lineEditNumeroCTT")
        self.gridLayout_61.addWidget(self.lineEditNumeroCTT, 0, 2, 1, 1)
        self.label_123 = QtWidgets.QLabel(self.frame_86)
        self.label_123.setMinimumSize(QtCore.QSize(180, 30))
        self.label_123.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_123.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_123.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_123.setObjectName("label_123")
        self.gridLayout_61.addWidget(self.label_123, 0, 3, 1, 1)
        self.label_124 = QtWidgets.QLabel(self.frame_86)
        self.label_124.setMinimumSize(QtCore.QSize(120, 30))
        self.label_124.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_124.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_124.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_124.setObjectName("label_124")
        self.gridLayout_61.addWidget(self.label_124, 0, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_61.addItem(spacerItem19, 0, 5, 1, 1)
        self.gridLayout_59.addLayout(self.gridLayout_61, 2, 1, 1, 1)
        self.gridLayout_62 = QtWidgets.QGridLayout()
        self.gridLayout_62.setObjectName("gridLayout_62")
        self.lineEditTelefone1CTT = MyLineEdit(self.frame_86)
        self.lineEditTelefone1CTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditTelefone1CTT.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEditTelefone1CTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditTelefone1CTT.setObjectName("lineEditTelefone1CTT")
        self.gridLayout_62.addWidget(self.lineEditTelefone1CTT, 0, 3, 1, 1)
        self.lineEditDDD1CTT = MyLineEdit(self.frame_86)
        self.lineEditDDD1CTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDD1CTT.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEditDDD1CTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDD1CTT.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditDDD1CTT.setObjectName("lineEditDDD1CTT")
        self.gridLayout_62.addWidget(self.lineEditDDD1CTT, 0, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_62.addItem(spacerItem20, 0, 4, 1, 1)
        self.label_125 = QtWidgets.QLabel(self.frame_86)
        self.label_125.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_125.setObjectName("label_125")
        self.gridLayout_62.addWidget(self.label_125, 0, 2, 1, 1)
        self.label_126 = QtWidgets.QLabel(self.frame_86)
        self.label_126.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_126.setObjectName("label_126")
        self.gridLayout_62.addWidget(self.label_126, 0, 0, 1, 1)
        self.gridLayout_59.addLayout(self.gridLayout_62, 3, 1, 1, 1)
        self.label_127 = QtWidgets.QLabel(self.frame_86)
        self.label_127.setMinimumSize(QtCore.QSize(0, 30))
        self.label_127.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_127.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_127.setObjectName("label_127")
        self.gridLayout_59.addWidget(self.label_127, 1, 0, 1, 1)
        self.label_128 = QtWidgets.QLabel(self.frame_86)
        self.label_128.setMinimumSize(QtCore.QSize(0, 30))
        self.label_128.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_128.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_128.setObjectName("label_128")
        self.gridLayout_59.addWidget(self.label_128, 0, 0, 1, 1)
        self.label_130 = QtWidgets.QLabel(self.frame_86)
        self.label_130.setMinimumSize(QtCore.QSize(0, 30))
        self.label_130.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_130.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_130.setObjectName("label_130")
        self.gridLayout_59.addWidget(self.label_130, 3, 0, 1, 1)
        self.label_131 = QtWidgets.QLabel(self.frame_86)
        self.label_131.setMinimumSize(QtCore.QSize(0, 30))
        self.label_131.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_131.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_131.setObjectName("label_131")
        self.gridLayout_59.addWidget(self.label_131, 4, 0, 1, 1)
        self.gridLayout_64 = QtWidgets.QGridLayout()
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.comboBoxEventoCTT = QtWidgets.QComboBox(self.frame_86)
        self.comboBoxEventoCTT.setMinimumSize(QtCore.QSize(250, 30))
        self.comboBoxEventoCTT.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";\n"
        "")
        self.comboBoxEventoCTT.setCurrentText("")
        self.comboBoxEventoCTT.setObjectName("comboBoxEventoCTT")
        self.gridLayout_64.addWidget(self.comboBoxEventoCTT, 0, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_64.addItem(spacerItem21, 0, 5, 1, 1)
        self.bttBuscarEventoCTT = QtWidgets.QPushButton(self.frame_86)
        self.bttBuscarEventoCTT.setMinimumSize(QtCore.QSize(80, 0))
        self.bttBuscarEventoCTT.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    border-radius:18px;\n"
        "    margin-left:10px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttBuscarEventoCTT.setObjectName("bttBuscarEventoCTT")
        self.gridLayout_64.addWidget(self.bttBuscarEventoCTT, 0, 2, 1, 1)
        self.lineEditEventoCTT = MyLineEdit(self.frame_86)
        self.lineEditEventoCTT.setStyleSheet("font: 12pt \"Century Gothic\";background:transparent;border:0px;")
        self.lineEditEventoCTT.setObjectName("lineEditEventoCTT")
        self.lineEditEventoCTT.setReadOnly(True)
        self.gridLayout_64.addWidget(self.lineEditEventoCTT, 0, 4, 1, 1)
        self.bttCriarEventoCTT = QtWidgets.QPushButton(self.frame_86)
        self.bttCriarEventoCTT.setMinimumSize(QtCore.QSize(80, 0))
        self.bttCriarEventoCTT.setStyleSheet("QPushButton{\n"
        "    font: 14pt \"Sofia\";\n"
        "    border:4px solid rgb(190,175,138);\n"
        "    margin-left:10px;\n"
        "    border-radius:18px;\n"
        "}\n"
        "\n"
        "QPushButton::hover{\n"
        "border:4px solid rgb(227,214,168);\n"
        "\n"
        "}QPushButton::pressed{\n"
        "border:2px solid rgb(249,238,187);\n"
        "}")
        self.bttCriarEventoCTT.setObjectName("bttCriarEventoCTT")
        self.gridLayout_64.addWidget(self.bttCriarEventoCTT, 0, 3, 1, 1)
        self.gridLayout_59.addLayout(self.gridLayout_64, 4, 1, 1, 1)
        self.horizontalLayout_56.addLayout(self.gridLayout_59)
        self.verticalLayout_39.addWidget(self.frame_86)
        self.frame_87 = QtWidgets.QFrame(self.frame_84)
        self.frame_87.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_87.setObjectName("frame_87")
        self.horizontalLayout_57 = QtWidgets.QHBoxLayout(self.frame_87)
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.frame_88 = QtWidgets.QFrame(self.frame_87)
        self.frame_88.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_88.setObjectName("frame_88")
        self.horizontalLayout_58 = QtWidgets.QHBoxLayout(self.frame_88)
        self.horizontalLayout_58.setObjectName("horizontalLayout_58")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_133 = QtWidgets.QLabel(self.frame_88)
        self.label_133.setMinimumSize(QtCore.QSize(0, 30))
        self.label_133.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_133.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_133.setObjectName("label_133")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_133)
        self.textEditDescricaoCTT = QtWidgets.QTextEdit(self.frame_88)
        self.textEditDescricaoCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.textEditDescricaoCTT.setObjectName("textEditDescricaoCTT")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEditDescricaoCTT)
        self.label_134 = QtWidgets.QLabel(self.frame_88)
        self.label_134.setMinimumSize(QtCore.QSize(0, 30))
        self.label_134.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_134.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_134.setObjectName("label_134")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_134)
        self.textEditAcessoriosCTT = QtWidgets.QTextEdit(self.frame_88)
        self.textEditAcessoriosCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.textEditAcessoriosCTT.setObjectName("textEditAcessoriosCTT")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEditAcessoriosCTT)
        self.horizontalLayout_58.addLayout(self.formLayout_7)
        self.horizontalLayout_57.addWidget(self.frame_88)
        self.frame_89 = QtWidgets.QFrame(self.frame_87)
        self.frame_89.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_89.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_89.setObjectName("frame_89")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_89)
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.frame_90 = QtWidgets.QFrame(self.frame_89)
        self.frame_90.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_90.setObjectName("frame_90")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_90)
        self.verticalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_135 = QtWidgets.QLabel(self.frame_90)
        self.label_135.setMinimumSize(QtCore.QSize(135, 30))
        self.label_135.setMaximumSize(QtCore.QSize(135, 30))
        self.label_135.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_135.setObjectName("label_135")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_135)
        self.gridLayout_65 = QtWidgets.QGridLayout()
        self.gridLayout_65.setObjectName("gridLayout_65")
        self.label_136 = QtWidgets.QLabel(self.frame_90)
        self.label_136.setMinimumSize(QtCore.QSize(0, 30))
        self.label_136.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_136.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_136.setAlignment(QtCore.Qt.AlignCenter)
        self.label_136.setObjectName("label_136")
        self.gridLayout_65.addWidget(self.label_136, 0, 0, 1, 1)
        self.lineEditValorCTT = MyLineEdit(self.frame_90)
        self.lineEditValorCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditValorCTT.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditValorCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditValorCTT.setObjectName("lineEditValorCTT")
        self.gridLayout_65.addWidget(self.lineEditValorCTT, 0, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_65.addItem(spacerItem22, 0, 2, 1, 1)
        self.formLayout_8.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_65)
        self.label_138 = QtWidgets.QLabel(self.frame_90)
        self.label_138.setMinimumSize(QtCore.QSize(135, 30))
        self.label_138.setMaximumSize(QtCore.QSize(135, 30))
        self.label_138.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_138.setObjectName("label_138")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_138)
        self.gridLayout_67 = QtWidgets.QGridLayout()
        self.gridLayout_67.setObjectName("gridLayout_67")
        spacerItem23 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_67.addItem(spacerItem23, 0, 0, 1, 1)
        self.lineEditDescontoCTT = MyLineEdit(self.frame_90)
        self.lineEditDescontoCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDescontoCTT.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDescontoCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDescontoCTT.setObjectName("lineEditDescontoCTT")
        self.gridLayout_67.addWidget(self.lineEditDescontoCTT, 0, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_67.addItem(spacerItem24, 0, 2, 1, 1)
        self.formLayout_8.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout_67)
        self.label_139 = QtWidgets.QLabel(self.frame_90)
        self.label_139.setMinimumSize(QtCore.QSize(135, 30))
        self.label_139.setMaximumSize(QtCore.QSize(135, 30))
        self.label_139.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_139.setObjectName("label_139")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_139)
        self.gridLayout_68 = QtWidgets.QGridLayout()
        self.gridLayout_68.setObjectName("gridLayout_68")
        self.label_140 = QtWidgets.QLabel(self.frame_90)
        self.label_140.setMinimumSize(QtCore.QSize(0, 30))
        self.label_140.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_140.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_140.setAlignment(QtCore.Qt.AlignCenter)
        self.label_140.setObjectName("label_140")
        self.gridLayout_68.addWidget(self.label_140, 0, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_68.addItem(spacerItem25, 0, 2, 1, 1)
        self.lineEditSinalCTT = MyLineEdit(self.frame_90)
        self.lineEditSinalCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditSinalCTT.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditSinalCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditSinalCTT.setObjectName("lineEditSinalCTT")
        self.gridLayout_68.addWidget(self.lineEditSinalCTT, 0, 1, 1, 1)
        self.formLayout_8.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.gridLayout_68)
        self.label_141 = QtWidgets.QLabel(self.frame_90)
        self.label_141.setMinimumSize(QtCore.QSize(135, 30))
        self.label_141.setMaximumSize(QtCore.QSize(135, 30))
        self.label_141.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_141.setObjectName("label_141")
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_141)
        self.gridLayout_69 = QtWidgets.QGridLayout()
        self.gridLayout_69.setObjectName("gridLayout_69")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_69.addItem(spacerItem26, 0, 6, 1, 1)
        self.lineEditDEDiaCTT = MyLineEdit(self.frame_90)
        self.lineEditDEDiaCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDEDiaCTT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditDEDiaCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDEDiaCTT.setObjectName("lineEditDEDiaCTT")
        self.gridLayout_69.addWidget(self.lineEditDEDiaCTT, 0, 1, 1, 1)
        self.lineEditDEMesCTT = MyLineEdit(self.frame_90)
        self.lineEditDEMesCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDEMesCTT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditDEMesCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDEMesCTT.setObjectName("lineEditDEMesCTT")
        self.gridLayout_69.addWidget(self.lineEditDEMesCTT, 0, 3, 1, 1)
        self.lineEditDEAnoCTT = MyLineEdit(self.frame_90)
        self.lineEditDEAnoCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDEAnoCTT.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDEAnoCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDEAnoCTT.setObjectName("lineEditDEAnoCTT")
        self.gridLayout_69.addWidget(self.lineEditDEAnoCTT, 0, 5, 1, 1)
        self.label_142 = QtWidgets.QLabel(self.frame_90)
        self.label_142.setMinimumSize(QtCore.QSize(0, 30))
        self.label_142.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_142.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_142.setAlignment(QtCore.Qt.AlignCenter)
        self.label_142.setObjectName("label_142")
        self.gridLayout_69.addWidget(self.label_142, 0, 4, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_69.addItem(spacerItem27, 0, 0, 1, 1)
        self.label_143 = QtWidgets.QLabel(self.frame_90)
        self.label_143.setMinimumSize(QtCore.QSize(0, 30))
        self.label_143.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_143.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_143.setAlignment(QtCore.Qt.AlignCenter)
        self.label_143.setObjectName("label_143")
        self.gridLayout_69.addWidget(self.label_143, 0, 2, 1, 1)
        self.formLayout_8.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.gridLayout_69)
        self.label_144 = QtWidgets.QLabel(self.frame_90)
        self.label_144.setStyleSheet("font: 75 16pt \"Century Gothic\";\n"
        "\n"
        "\n"
        "")
        self.label_144.setObjectName("label_144")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_144)
        self.gridLayout_70 = QtWidgets.QGridLayout()
        self.gridLayout_70.setObjectName("gridLayout_70")
        self.lineEditDDDiaCTT = MyLineEdit(self.frame_90)
        self.lineEditDDDiaCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDDiaCTT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditDDDiaCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDDiaCTT.setObjectName("lineEditDDDiaCTT")
        self.gridLayout_70.addWidget(self.lineEditDDDiaCTT, 0, 1, 1, 1)
        self.label_145 = QtWidgets.QLabel(self.frame_90)
        self.label_145.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_145.setObjectName("label_145")
        self.gridLayout_70.addWidget(self.label_145, 0, 2, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_70.addItem(spacerItem28, 0, 0, 1, 1)
        self.lineEditDDMesCTT = MyLineEdit(self.frame_90)
        self.lineEditDDMesCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDMesCTT.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEditDDMesCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDMesCTT.setObjectName("lineEditDDMesCTT")
        self.gridLayout_70.addWidget(self.lineEditDDMesCTT, 0, 3, 1, 1)
        self.label_146 = QtWidgets.QLabel(self.frame_90)
        self.label_146.setStyleSheet("\n"
        "\n"
        "    font: 20pt \"Microsoft Uighur\";\n"
        "")
        self.label_146.setObjectName("label_146")
        self.gridLayout_70.addWidget(self.label_146, 0, 4, 1, 1)
        self.lineEditDDAnoCTT = MyLineEdit(self.frame_90)
        self.lineEditDDAnoCTT.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditDDAnoCTT.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEditDDAnoCTT.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.lineEditDDAnoCTT.setObjectName("lineEditDDAnoCTT")
        self.gridLayout_70.addWidget(self.lineEditDDAnoCTT, 0, 5, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_70.addItem(spacerItem29, 0, 6, 1, 1)
        self.formLayout_8.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.gridLayout_70)
        self.verticalLayout_41.addLayout(self.formLayout_8)
        self.frame_91 = QtWidgets.QFrame(self.frame_90)
        self.frame_91.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_91.setObjectName("frame_91")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_91)
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.verticalLayout_41.addWidget(self.frame_91)
        self.verticalLayout_40.addWidget(self.frame_90)
        self.frame_92 = QtWidgets.QFrame(self.frame_89)
        self.frame_92.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_92.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_92.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_92.setObjectName("frame_92")
        self.horizontalLayout_59 = QtWidgets.QHBoxLayout(self.frame_92)
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName("horizontalLayout_59")
        self.bttGerarContratoCTT = QtWidgets.QPushButton(self.frame_92)
        self.bttGerarContratoCTT.setMinimumSize(QtCore.QSize(130, 40))
        self.bttGerarContratoCTT.setMaximumSize(QtCore.QSize(120, 40))
        self.bttGerarContratoCTT.setStyleSheet("QPushButton{\n"
"    font: 14pt \"Sofia\";\n"
"    border:4px solid rgb(190,175,138);\n"
"    border-radius:20px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"border:4px solid rgb(227,214,168);\n"
"\n"
"}QPushButton::pressed{\n"
"border:2px solid rgb(249,238,187);\n"
"}")

#! pronto
        self.bttGerarContratoCTT.setObjectName("bttGerarContratoCTT")
        self.horizontalLayout_59.addWidget(self.bttGerarContratoCTT)
        self.verticalLayout_40.addWidget(self.frame_92)
        self.horizontalLayout_57.addWidget(self.frame_89)
        self.verticalLayout_39.addWidget(self.frame_87)
        self.verticalLayout_38.addWidget(self.frame_84)
        self.stackedWidget.addWidget(self.pg_contrato)
        self.horizontalLayout.addWidget(self.stackedWidget)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.bttCadastro, self.bttAgendamento)
        MainWindow.setTabOrder(self.bttAgendamento, self.bttSemanal)
        MainWindow.setTabOrder(self.bttSemanal, self.bttDevolucoes)
        MainWindow.setTabOrder(self.bttDevolucoes, self.bttContrato)
        MainWindow.setTabOrder(self.bttContrato, self.lineEditNomeCC)
        MainWindow.setTabOrder(self.lineEditNomeCC, self.lineEditDiaNCC)
        MainWindow.setTabOrder(self.lineEditDiaNCC, self.lineEditMesNCC)
        MainWindow.setTabOrder(self.lineEditMesNCC, self.lineEditAnoNCC)
        MainWindow.setTabOrder(self.lineEditAnoNCC, self.lineEditCPFCC)
        MainWindow.setTabOrder(self.lineEditCPFCC, self.lineEditRGCC)
        MainWindow.setTabOrder(self.lineEditRGCC, self.lineEditCEPCC)
        MainWindow.setTabOrder(self.lineEditCEPCC, self.lineEditEnderecoCC)
        MainWindow.setTabOrder(self.lineEditEnderecoCC, self.lineEditNumeroCC)
        MainWindow.setTabOrder(self.lineEditNumeroCC, self.lineEditComplementoCC)
        MainWindow.setTabOrder(self.lineEditComplementoCC, self.lineEditBairroCC)
        MainWindow.setTabOrder(self.lineEditBairroCC, self.lineEditCidadeCC)
        MainWindow.setTabOrder(self.lineEditCidadeCC, self.lineEditEstadoCC)
        MainWindow.setTabOrder(self.lineEditEstadoCC, self.lineEditDDD1CC)
        MainWindow.setTabOrder(self.lineEditDDD1CC, self.lineEditTelefone1CC)
        MainWindow.setTabOrder(self.lineEditTelefone1CC, self.lineEditDDD2CC)
        MainWindow.setTabOrder(self.lineEditDDD2CC, self.lineEditTelefone2CC)
        MainWindow.setTabOrder(self.lineEditTelefone2CC, self.bttCadastarCC)
        MainWindow.setTabOrder(self.bttCadastarCC, self.bttAtualizarCC)
        MainWindow.setTabOrder(self.bttAtualizarCC, self.bttBuscarCPFCC)
        MainWindow.setTabOrder(self.bttBuscarCPFCC, self.bttBuscarCEPCC)
        MainWindow.setTabOrder(self.bttBuscarCEPCC, self.bttInicioCC)
        MainWindow.setTabOrder(self.bttInicioCC, self.lineEditNomeA)
        MainWindow.setTabOrder(self.lineEditNomeA, self.lineEditCPFA)
        MainWindow.setTabOrder(self.lineEditCPFA, self.lineEditEnderecoA)
        MainWindow.setTabOrder(self.lineEditEnderecoA, self.lineEditNumeroA)
        MainWindow.setTabOrder(self.lineEditNumeroA, self.lineEditComplementoA)
        MainWindow.setTabOrder(self.lineEditComplementoA, self.lineEditDDD1A)
        MainWindow.setTabOrder(self.lineEditDDD1A, self.lineEditTelefone1A)
        MainWindow.setTabOrder(self.lineEditTelefone1A, self.comboBoxEventoA)
        MainWindow.setTabOrder(self.comboBoxEventoA, self.textEditDescricaoA)
        MainWindow.setTabOrder(self.textEditDescricaoA, self.textEditAcessoriosA)
        MainWindow.setTabOrder(self.textEditAcessoriosA, self.textEditAjustesA)
        MainWindow.setTabOrder(self.textEditAjustesA, self.lineEditValorA)
        MainWindow.setTabOrder(self.lineEditValorA, self.lineEditDescontoA)
        MainWindow.setTabOrder(self.lineEditDescontoA, self.lineEditSinalA)
        MainWindow.setTabOrder(self.lineEditSinalA, self.lineEditDEDiaA)
        MainWindow.setTabOrder(self.lineEditDEDiaA, self.lineEditDEMesA)
        MainWindow.setTabOrder(self.lineEditDEMesA, self.lineEditDEAnoA)
        MainWindow.setTabOrder(self.lineEditDEAnoA, self.bttGerarReciboA_2)
        MainWindow.setTabOrder(self.bttGerarReciboA_2, self.bttConcluirA_2)
        MainWindow.setTabOrder(self.bttConcluirA_2, self.bttAtualizarA_2)
        MainWindow.setTabOrder(self.bttAtualizarA_2, self.bttBuscarCPFA)
        MainWindow.setTabOrder(self.bttBuscarCPFA, self.bttBuscarEventoA)
        MainWindow.setTabOrder(self.bttBuscarEventoA, self.bttCriarEventoA)
        MainWindow.setTabOrder(self.bttCriarEventoA, self.bttInicioA)
        MainWindow.setTabOrder(self.bttInicioA, self.entregas_segunda)
        MainWindow.setTabOrder(self.entregas_segunda, self.entregas_terca)
        MainWindow.setTabOrder(self.entregas_terca, self.entregas_quarta)
        MainWindow.setTabOrder(self.entregas_quarta, self.entregas_quinta)
        MainWindow.setTabOrder(self.entregas_quinta, self.entregas_sexta)
        MainWindow.setTabOrder(self.entregas_sexta, self.entregas_sabado)
        MainWindow.setTabOrder(self.entregas_sabado, self.bttGerarContratoSE)
        MainWindow.setTabOrder(self.bttGerarContratoSE, self.bttApagarAgendamentoSE)
        MainWindow.setTabOrder(self.bttApagarAgendamentoSE, self.bttEditarAgendamentoSE)
        MainWindow.setTabOrder(self.bttEditarAgendamentoSE, self.bttInicioSE)
        MainWindow.setTabOrder(self.bttInicioSE, self.devolucoes_segunda)
        MainWindow.setTabOrder(self.devolucoes_segunda, self.devolucoes_terca)
        MainWindow.setTabOrder(self.devolucoes_terca, self.devolucoes_quarta)
        MainWindow.setTabOrder(self.devolucoes_quarta, self.devolucoes_quinta)
        MainWindow.setTabOrder(self.devolucoes_quinta, self.devolucoes_sexta)
        MainWindow.setTabOrder(self.devolucoes_sexta, self.devolucoes_sabado)
        MainWindow.setTabOrder(self.devolucoes_sabado, self.bttInicioDS)
        MainWindow.setTabOrder(self.bttInicioDS, self.bttDevolvidoDS)
        MainWindow.setTabOrder(self.bttDevolvidoDS, self.lineEditNomeCTT)
        MainWindow.setTabOrder(self.lineEditNomeCTT, self.lineEditCPFCTT)
        MainWindow.setTabOrder(self.lineEditCPFCTT, self.lineEditEnderecoCTT)
        MainWindow.setTabOrder(self.lineEditEnderecoCTT, self.lineEditNumeroCTT)
        MainWindow.setTabOrder(self.lineEditNumeroCTT, self.lineEditComplementoCTT)
        MainWindow.setTabOrder(self.lineEditComplementoCTT, self.lineEditDDD1CTT)
        MainWindow.setTabOrder(self.lineEditDDD1CTT, self.lineEditTelefone1CTT)
        MainWindow.setTabOrder(self.lineEditTelefone1CTT, self.comboBoxEventoCTT)
        MainWindow.setTabOrder(self.comboBoxEventoCTT, self.textEditDescricaoCTT)
        MainWindow.setTabOrder(self.textEditDescricaoCTT, self.textEditAcessoriosCTT)
        MainWindow.setTabOrder(self.textEditAcessoriosCTT, self.lineEditValorCTT)
        MainWindow.setTabOrder(self.lineEditValorCTT, self.lineEditDescontoCTT)
        MainWindow.setTabOrder(self.lineEditDescontoCTT, self.lineEditSinalCTT)
        MainWindow.setTabOrder(self.lineEditSinalCTT, self.lineEditDEDiaCTT)
        MainWindow.setTabOrder(self.lineEditDEDiaCTT, self.lineEditDEMesCTT)
        MainWindow.setTabOrder(self.lineEditDEMesCTT, self.lineEditDEAnoCTT)
        MainWindow.setTabOrder(self.lineEditDEAnoCTT, self.lineEditDDDiaCTT)
        MainWindow.setTabOrder(self.lineEditDDDiaCTT, self.lineEditDDMesCTT)
        MainWindow.setTabOrder(self.lineEditDDMesCTT, self.lineEditDDAnoCTT)
        MainWindow.setTabOrder(self.lineEditDDAnoCTT, self.bttGerarContratoCTT)
        MainWindow.setTabOrder(self.bttGerarContratoCTT, self.bttBuscarEventoCTT)
        MainWindow.setTabOrder(self.bttBuscarEventoCTT, self.bttCriarEventoCTT)
        MainWindow.setTabOrder(self.bttCriarEventoCTT, self.bttBuscarCPFCTT)
        MainWindow.setTabOrder(self.bttBuscarCPFCTT, self.bttInicioCTT)

        
        self.devolucoes_segunda.itemClicked.connect(self.onListaClickedD)
        self.devolucoes_terca.itemClicked.connect  (self.onListaClickedD)
        self.devolucoes_quarta.itemClicked.connect (self.onListaClickedD)
        self.devolucoes_quinta.itemClicked.connect (self.onListaClickedD)
        self.devolucoes_sexta.itemClicked.connect  (self.onListaClickedD)
        self.entregas_segunda.itemClicked.connect(self.onListaClickedE)
        self.entregas_terca.itemClicked.connect  (self.onListaClickedE)
        self.entregas_quarta.itemClicked.connect (self.onListaClickedE)
        self.entregas_quinta.itemClicked.connect (self.onListaClickedE)
        self.entregas_sexta.itemClicked.connect  (self.onListaClickedE)
        self.w = ''

        ##? Setar Botoes

        #! LETRAS a-Z
        """
        regexL=QtCore.QRegExp("[\w--[\d_]]+")
        validatorL = QtGui.QRegExpValidator(regexL)

        # Pagina CC
        
        self.lineEditNomeCC.setValidator(validatorL)

        # Pagina A
        self.lineEditNomeA.setValidator(validatorL)
        
        # Pagina CTT
        self.lineEditNomeCTT.setValidator(validatorL)
        """

        #! Numeros
        regexN=QtCore.QRegExp("[0-9, ]+")
        validatorN = QtGui.QRegExpValidator(regexN)
        
        # Pagina CC
        self.lineEditDiaNCC.setValidator(validatorN)
        self.lineEditMesNCC.setValidator(validatorN)
        self.lineEditAnoNCC.setValidator(validatorN)
        self.lineEditCPFCC.setValidator(validatorN)
        self.lineEditCEPCC.setValidator(validatorN)
        self.lineEditNumeroCC.setValidator(validatorN)
        self.lineEditDDD1CC.setValidator(validatorN)
        self.lineEditTelefone1CC.setValidator(validatorN)
        self.lineEditDDD2CC.setValidator(validatorN)
        self.lineEditTelefone2CC.setValidator(validatorN)

        # Pagina A
        self.lineEditCPFA.setValidator(validatorN)
        self.lineEditDDD1A.setValidator(validatorN)
        self.lineEditTelefone1A.setValidator(validatorN)
        self.lineEditValorA.setValidator(validatorN)
        self.lineEditDescontoA.setValidator(validatorN)
        self.lineEditSinalA.setValidator(validatorN)
        self.lineEditDEDiaA.setValidator(validatorN)
        self.lineEditDEMesA.setValidator(validatorN)
        self.lineEditDEAnoA.setValidator(validatorN)

        # Pagina CTT 
        self.lineEditCPFCTT.setValidator(validatorN)
        self.lineEditNumeroCTT.setValidator(validatorN)
        self.lineEditDDD1CTT.setValidator(validatorN)
        self.lineEditTelefone1CTT.setValidator(validatorN)
        self.lineEditValorCTT.setValidator(validatorN)
        self.lineEditDescontoCTT.setValidator(validatorN)
        self.lineEditSinalCTT.setValidator(validatorN)
        self.lineEditDEDiaCTT.setValidator(validatorN)
        self.lineEditDEMesCTT.setValidator(validatorN)
        self.lineEditDEMesCTT.setValidator(validatorN)
        self.lineEditDEAnoCTT.setValidator(validatorN)
        





        ##? Criar lista
        self.listaA = [self.lineEditNomeA,self.lineEditCPFA,self.lineEditEnderecoA,self.lineEditNumeroA,self.lineEditDDD1A,self.lineEditTelefone1A,self.lineEditValorA,self.lineEditDEDiaA,self.lineEditDEMesA,self.lineEditDEAnoA,self.lineEditSinalA]

        self.listaCTT = [self.lineEditNomeCTT, self.lineEditCPFCTT, self.lineEditEnderecoCTT,self.lineEditNumeroCTT,self.lineEditDDD1CTT, self.lineEditTelefone1CTT,self.lineEditValorCTT, self.lineEditDescontoCTT,self.lineEditSinalCTT, self.lineEditDEDiaCTT,self.lineEditDEMesCTT, self.lineEditDEAnoCTT,self.lineEditDDDiaCTT, self.lineEditDDMesCTT,self.lineEditDDAnoCTT]

        self.listaCC= [self.lineEditNomeCC,self.lineEditDiaNCC,self.lineEditMesNCC,self.lineEditAnoNCC, self.lineEditCEPCC,self.lineEditEnderecoCC,self.lineEditNumeroCC,self.lineEditBairroCC,self.lineEditCidadeCC,self.lineEditEstadoCC,self.lineEditDDD1CC,self.lineEditTelefone1CC]
        #Lista sem RG e CPF

        ##? Pagina Cliente
        self.bttCadastarCC.clicked.connect(lambda : self.verificarCadastroCC(0))
        self.bttAtualizarCC.clicked.connect(lambda: self.verificarCadastroCC(1))
        self.bttBuscarCEPCC.clicked.connect(self.buscarCepCC)
        self.bttBuscarCPFCC.clicked.connect(self.procurarCliente)
        
        # setar botoes para quando clicar voltar ao normal
        self.lineEditNomeCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditNomeCC))
        self.lineEditDiaNCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDiaNCC))
        self.lineEditMesNCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditMesNCC))
        self.lineEditAnoNCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditAnoNCC))
        self.lineEditCPFCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditCPFCC))
        self.lineEditRGCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditRGCC))
        self.lineEditCEPCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditCEPCC))
        self.lineEditEnderecoCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditEnderecoCC))
        self.lineEditNumeroCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditNumeroCC))
        self.lineEditComplementoCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditComplementoCC))
        self.lineEditBairroCC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditBairroCC))
        self.lineEditCidadeCC.clicked.connect(lambda: self.apagarLineEdit(self.lineEditCidadeCC))
        self.lineEditEstadoCC.clicked.connect(lambda: self.apagarLineEdit(self.lineEditEstadoCC))
        self.lineEditDDD1CC.clicked.connect(lambda: self.apagarLineEdit(self.lineEditDDD1CC))
        self.lineEditDDD2CC.clicked.connect(lambda: self.apagarLineEdit(self.lineEditDDD2CC))
        self.lineEditTelefone1CC.clicked.connect(lambda: self.padraoLineEdit(self.lineEditTelefone1CC))
        

        

        self.bttConcluirA_2.clicked.connect(lambda: self.verificarAgendamentoA(1))
        self.bttAtualizarA_2.clicked.connect(lambda: self.verificarAgendamentoA(2))

        # setar botoes para quando clicar voltar ao normal
        self.lineEditNomeA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditNomeA))
        self.lineEditCPFA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditCPFA))
        self.lineEditEnderecoA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditEnderecoA))
        self.lineEditNumeroA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditNumeroA))
        self.lineEditComplementoA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditComplementoA))
        self.lineEditDDD1A.clicked.connect(lambda: self.apagarLineEdit(self.lineEditDDD1A))
        self.lineEditTelefone1A.clicked.connect(lambda: self.padraoLineEdit(self.lineEditTelefone1A))
        self.lineEditValorA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditValorA))
        self.lineEditDEDiaA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDEDiaA))
        self.lineEditDEMesA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDEMesA))
        self.lineEditDEAnoA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDEAnoA))
        self.lineEditSinalA.clicked.connect(lambda: self.padraoLineEdit(self.lineEditSinalA))


        self.bttCriarEventoA.clicked.connect(lambda: self.criarEvento(1))
        self.bttBuscarEventoA.clicked.connect(lambda: self.buscarEvento(1))

        self.bttGerarReciboA_2.clicked.connect(lambda: self.verificarAgendamentoA(3))
        self.bttBuscarCPFA.clicked.connect(self.procurarClienteA)

        ##? Pagina Entregas
        self.itens = [] #lista de itens para serem entregues
        self.bttApagarAgendamentoSE.clicked.connect(self.apagarAgendamento)
        self.bttGerarContratoSE.clicked.connect(self.gerarContrato)
        self.bttEditarAgendamentoSE.clicked.connect(self.editarAgendamento)

        ##? Pagina de Devoluções
        self.itensD = [] #lista de itens para serem entregues
        self.bttDevolvidoDS.clicked.connect(self.apagarContrato)

        ##? Pagina de Contrato
        self.bttBuscarCPFCTT.clicked.connect(self.buscarContrato)
        self.bttGerarContratoCTT.clicked.connect(self.verificarContrato)
        self.bttCriarEventoCTT.clicked.connect(lambda: self.criarEvento(2))
        self.bttBuscarEventoCTT.clicked.connect(lambda: self.buscarEvento(2))

        # setar botoes para quando clicar voltar ao normal
        self.lineEditNomeCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditNomeCTT))
        self.lineEditCPFCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditCPFCTT))
        self.lineEditEnderecoCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditEnderecoCTT))
        self.lineEditNumeroCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditNumeroCTT))
        self.lineEditComplementoCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditComplementoCTT))
        self.lineEditDDD1CTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDDD1CTT))
        self.lineEditTelefone1CTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditTelefone1CTT))
        self.lineEditValorCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditValorCTT))
        self.lineEditDescontoCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDescontoCTT))
        self.lineEditSinalCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditSinalCTT))
        self.lineEditDEDiaCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDEDiaCTT))
        self.lineEditDEMesCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDEMesCTT))
        self.lineEditDEAnoCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDEAnoCTT))
        self.lineEditDDDiaCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDDDiaCTT))
        self.lineEditDDMesCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDDMesCTT))
        self.lineEditDDAnoCTT.clicked.connect(lambda: self.padraoLineEdit(self.lineEditDDAnoCTT))


        self.comboBoxEventoA.highlighted.connect(lambda: self.atualizarEventos(self.comboBoxEventoA))
        self.comboBoxEventoCTT.highlighted.connect(lambda: self.atualizarEventos(self.comboBoxEventoCTT))
        ##? Pagina Home e Inicios
        self.bttCadastro.clicked.connect(lambda: self.changePage('Cadastro'))
        self.bttAgendamento.clicked.connect(lambda: self.changePage('Agendamento'))
        self.bttSemanal.clicked.connect(lambda: self.changePage('Entregas'))
        self.bttDevolucoes.clicked.connect(lambda: self.changePage('Devo'))
        self.bttContrato.clicked.connect(lambda: self.changePage('Contrato'))
        self.bttInicioCC.clicked.connect(lambda: self.changePage('Home'))
        self.bttInicioA.clicked.connect(lambda: self.changePage('Home'))
        self.bttInicioSE.clicked.connect(lambda: self.changePage('Home'))
        self.bttInicioDS.clicked.connect(lambda: self.changePage('Home'))
        self.bttInicioCTT.clicked.connect(lambda: self.changePage('Home'))
        self.apagarEvento()

        

#! inicio das defs

    


    def criarEvento(self,valor):
        if(valor == 1):
            itens = [self.lineEditNomeA.text(),self.lineEditCPFA.text(),self.textEditDescricaoA.toPlainText()]
            if(itens[0] != '' and itens[1] != '' and itens[2] != '' and self.comboBoxEventoA.currentText()):
                self.openWindow(1,itens)
        else:
            itens = [self.lineEditNomeCTT.text(),self.lineEditCPFCTT.text(),self.textEditDescricaoCTT.toPlainText()]
            if(itens[0] != '' and itens[1] != '' and itens[2] != '' and self.comboBoxEventoCTT.currentText()):
                self.openWindow(1,itens)

    def buscarEvento(self,valor):
        if(valor == 1):
            self.openWindow(str(self.comboBoxEventoA.currentText()),'')
        else:
            
            self.openWindow(str(self.comboBoxEventoCTT.currentText()),'')

    def atualizarEventos(self,aux):
        try:
            self.eventos = getAllEventos()
            if(self.eventos is not None):
                itens = [aux.itemText(i) for i in range(aux.count())]
                for i in self.eventos:
                    if(i[0] not in itens):
                        aux.addItem(i[0])

        except:
            print('erro nos eventos')

    def apagarEvento(self):
        try:
            self.eventos = getAllEventos()
            for i in self.eventos:
                if i is not None:
                    data = datetime(int(i[3][6:]),int(i[3][3:5]), int(str(i[3][0])+str(i[3][1])))
                    if (data < datetime.today()):
                        print('data é menor',i,i[0])
                        removeEvento(i[0])
                        print('removido')
        except:
            print('Erro ao remover o evento')

    def padraoLineEdit(self,lineEdit):
        lineEdit.setStyleSheet("font: 12pt \"Century Gothic\";")

    def apagarLineEdit(self,lineEdit):
        lineEdit.setText('')
        lineEdit.setStyleSheet("font: 12pt \"Century Gothic\";")

##? Pagina HOME
    def changePage(self,page):
        if(page == 'Home'):
                self.stackedWidget.setCurrentIndex(0)
        elif(page == 'Cadastro'):
                self.stackedWidget.setCurrentIndex(1)
        elif(page == 'Agendamento'):
                self.stackedWidget.setCurrentIndex(2)
                self.atualizarEventos(self.comboBoxEventoA)
                self.atualizarEventos(self.comboBoxEventoCTT)
                self.limparTelaAgendamento()
        elif(page == 'Entregas'):
                self.stackedWidget.setCurrentIndex(3)
                self.gerarEntregas()
        elif(page == 'Devo'):
                self.stackedWidget.setCurrentIndex(4)
                self.gerarDevolucoes()
        elif(page == 'Contrato'):
                self.atualizarEventos(self.comboBoxEventoCTT)
                self.stackedWidget.setCurrentIndex(5)


##? Pagina Cliente

    def verificarCadastroCC(self,auxiliar):
        aux = 0
        for i in self.listaCC:
            if(i.text() == ''):
                i.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
                aux +=1
            else:
                i.setStyleSheet("border: 1px solid;border-color: rgb(0, 0, 0);font: 12pt \"Century Gothic\";")

        if(self.lineEditRGCC.text() == '' and self.lineEditCPFCC.text() == ''):
            aux +=1
            self.lineEditRGCC.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
            self.lineEditCPFCC.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
        else:
            self.lineEditRGCC.setStyleSheet("border: 1px solid;border-color: rgb(0, 0, 0);font: 12pt \"Century Gothic\";")
            self.lineEditCPFCC.setStyleSheet("border: 1px solid;border-color: rgb(0, 0, 0);font: 12pt \"Century Gothic\";")

        if(aux == 0 and auxiliar == 0):
            self.cadastrarCliente()
        elif(aux == 0 and auxiliar ==1):
            self.atualizarCliente()

    def cadastrarCliente(self):

        maxId = self.findMaxId()
        while(1):
            if(str(self.lineEditNomeCC.text())[-1] == ' '):
                self.lineEditNomeCC.setText(self.lineEditNomeCC.text()[:-1])
            else:
                break

        insertCliente(maxId,
        str(self.lineEditNomeCC.text()),
        str(self.lineEditDiaNCC.text() + self.lineEditMesNCC.text() + self.lineEditAnoNCC.text()),
        self.lineEditCPFCC.text(),
        self.lineEditRGCC.text(),
        self.lineEditCEPCC.text(),
        self.lineEditEnderecoCC.text(),
        self.lineEditNumeroCC.text(),
        self.lineEditComplementoCC.text(),
        self.lineEditBairroCC.text(),
        self.lineEditCidadeCC.text(),
        self.lineEditEstadoCC.text(),
        str(self.lineEditDDD1CC.text() + self.lineEditTelefone1CC.text()),
        str(self.lineEditDDD2CC.text() + self.lineEditTelefone2CC.text()),'0')
        self.showdialog('Cadastro do cliente','O cliente foi cadastrado com sucesso')
        self.changePage('Agendamento')
        self.lineEditCPFA.setText(self.lineEditCPFCC.text())
        for i in self.listaCC:
            i.setText('')

    def removeCliente(self):
            removeCliente(self.lineEditCPFCC.text())

    def buscarCepCC(self):
        if(str(self.lineEditCEPCC.text() != '')):
            try:
                endereco = getEnderecobyCEP(str(self.lineEditCEPCC.text()))
                if(endereco != ''):
                    self.lineEditEnderecoCC.setText(endereco[0])
                    self.lineEditBairroCC.setText(endereco[1])
                    self.lineEditCidadeCC.setText(endereco[2])
                    self.lineEditEstadoCC.setText(endereco[3])
            except:
                self.lineEditCEPCC.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
                self.showdialog('Buscar Cep','Erro ao buscar Cep')
        else:
            self.lineEditCEPCC.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")

    def procurarCliente(self):
        try:
            cliente = getClientes(self.lineEditCPFCC.text(), self.lineEditNomeCC.text())[0]
            cliente=list(cliente)
            cliente.pop(0)
            if (cliente == ()):
                self.showdialog('Cliente','Não existe um cliente com esse CPF cadastrado')
            else:
                self.lineEditNomeCC.setText(str(cliente[0]))
                self.lineEditDiaNCC.setText(str(cliente[1])[0:2])
                self.lineEditMesNCC.setText(str(cliente[1])[2:4])
                self.lineEditAnoNCC.setText(str(cliente[1])[4::])
                self.lineEditRGCC.setText(str(cliente[3]))
                self.lineEditCEPCC.setText(str(cliente[4]))
                self.lineEditEnderecoCC.setText(str(cliente[5]))
                self.lineEditNumeroCC.setText(str(cliente[6]))
                self.lineEditComplementoCC.setText(str(cliente[7]))
                self.lineEditBairroCC.setText(str(cliente[8]))
                self.lineEditCidadeCC.setText(str(cliente[9]))
                self.lineEditEstadoCC.setText(str(cliente[10]))
                self.lineEditDDD1CC.setText(str(cliente[11][0:2]))
                self.lineEditTelefone1CC.setText(str(cliente[11][2::]))
                self.lineEditDDD2CC.setText(str(cliente[12][0:2]))
                self.lineEditTelefone2CC.setText(str(cliente[12][2::]))
        except:
            self.showdialog('Cliente','Erro no cadastro do Cliente')

    def atualizarCliente(self):
        try:
            cliente = getClientes(self.lineEditCPFCC.text(), self.lineEditNomeCC.text())[0]
            updateCliente(cliente[0],
            str(self.lineEditNomeCC.text()),
            str(self.lineEditDiaNCC.text() + self.lineEditMesNCC.text() + self.lineEditAnoNCC.text()),
            self.lineEditCPFCC.text(),
            self.lineEditRGCC.text(),
            self.lineEditCEPCC.text(),
            self.lineEditEnderecoCC.text(),
            self.lineEditNumeroCC.text(),
            self.lineEditComplementoCC.text(),
            self.lineEditBairroCC.text(),
            self.lineEditCidadeCC.text(),
            self.lineEditEstadoCC.text(),
            str(self.lineEditDDD1CC.text() + self.lineEditTelefone1CC.text()),
            str(self.lineEditDDD2CC.text() + self.lineEditTelefone2CC.text()))

            self.showdialog('Atualização cliente','O cliente foi atualizado com sucesso')
        except:
            self.showdialog('Atualização de cliente','Erro ao atualizar os dados do cliente')



##? Pagina Agendamento
    def limparTelaAgendamento(self):
        self.lineEditCPFA.setText("")
        self.lineEditDDD1A.setText("")
        self.lineEditTelefone1A.setText("")
        self.lineEditValorA.setText("")
        self.lineEditDescontoA.setText("")
        self.lineEditSinalA.setText("")
        self.lineEditDEDiaA.setText("")
        self.lineEditDEMesA.setText("")
        self.lineEditDEAnoA.setText("")

    def verificarAgendamentoA(self,auxiliar):
        aux = 0
        for i in self.listaA:
            if(i.text() == ''):
                i.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
                aux +=1
            else:
                i.setStyleSheet("border: 1px solid;border-color: rgb(0, 0, 0);font: 12pt \"Century Gothic\";")

        if(aux == 0 and auxiliar == 2):
            self.atualizarAgendamento()
        elif(aux == 0 and auxiliar ==1):
            self.cadastrarAgendamento()
        elif(aux == 0 and auxiliar ==3):
            self.gerarReciboA()

    def procurarClienteA(self):
        if(self.lineEditCPFA.text() != '' or self.lineEditNomeA.text() != ''):
            try:
                cliente = getClientes(self.lineEditCPFA.text(), self.lineEditNomeA.text())[0]
                if (cliente != []):
                    cliente=list(cliente)
                    cliente.pop(0)
                    self.lineEditNomeA.setText(str(cliente[0]))
                    self.lineEditEnderecoA.setText(str(cliente[5]))
                    self.lineEditNumeroA.setText(str(cliente[6]))
                    self.lineEditComplementoA.setText(str(cliente[7]))
                    self.lineEditDDD1A.setText(str(cliente[11][0:2]))
                    self.lineEditTelefone1A.setText(str(cliente[11][2::]))
                    agendamentos = getAgendamentos(self.lineEditCPFA.text(),self.lineEditNomeA.text())

                    if(agendamentos != []):
                        agendamentos = agendamentos[0]
                        self.textEditDescricaoA.setPlainText(agendamentos[3])
                        self.textEditAcessoriosA.setPlainText(agendamentos[4])
                        self.textEditAjustesA.setPlainText(agendamentos[5])
                        self.lineEditValorA.setText(agendamentos[6])
                        self.lineEditDescontoA.setText(agendamentos[8])
                        self.lineEditSinalA.setText(agendamentos[9])
                        self.lineEditDEDiaA.setText(str(agendamentos[10])[0:2])
                        self.lineEditDEMesA.setText(str(agendamentos[10])[2:4])
                        self.lineEditDEAnoA.setText(str(agendamentos[10])[4::])
                        itens = [self.comboBoxEventoA.itemText(i) for i in range(self.comboBoxEventoA.count())]
                        aux = 0
                        for i in itens:
                            if(i == agendamentos[2]):
                                break
                            aux +=1
                        self.comboBoxEventoA.setCurrentIndex(aux)
                    
            except:

                self.showdialog('Cliente nao existe','Erro ao buscar cliente no banco de dados')
        else:
            
            self.lineEditCPFA.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
            self.lineEditNomeCC.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")

    def cadastrarAgendamento(self):
        try:
            agendamento = getAgendamentos(self.lineEditCPFA.text(),self.lineEditNomeA.text())[0]
            updateAgendamento(agendamento[0],
            self.lineEditCPFA.text(),
            self.comboBoxEventoA.currentText(),
            self.textEditDescricaoA.toPlainText(),
            self.textEditAcessoriosA.toPlainText(),
            self.textEditAjustesA.toPlainText(),
            self.lineEditValorA.text(),
            '',
            self.lineEditDescontoA.text(),
            self.lineEditSinalA.text(),
            str(self.lineEditDEDiaA.text() + self.lineEditDEMesA.text() + self.lineEditDEAnoA.text()))

            self.showdialog('Atualização do agendamento','O agendamento foi atualizado com sucesso')
        except:
            maxId = self.findMaxIdA()
            insertAgendamento(maxId,
            self.lineEditCPFA.text(),
            self.comboBoxEventoA.currentText(),
            self.textEditDescricaoA.toPlainText(),
            self.textEditAcessoriosA.toPlainText(),
            self.textEditAjustesA.toPlainText(),
            self.lineEditValorA.text(),
            '',
            self.lineEditDescontoA.text(),
            self.lineEditSinalA.text(),
            str(self.lineEditDEDiaA.text() + self.lineEditDEMesA.text() + self.lineEditDEAnoA.text()))

            self.showdialog('Agendamento do cliente','O Agendamento foi feito com sucesso')

    def atualizarAgendamento(self):
        try:
                agendamento = getAgendamentos(self.lineEditCPFA.text(),self.lineEditNomeA.text())[0]
                updateAgendamento(agendamento[0],
                                self.lineEditCPFA.text(),
                                self.comboBoxEventoA.currentText(),
                                self.textEditDescricaoA.toPlainText(),
                                self.textEditAcessoriosA.toPlainText(),
                                self.textEditAjustesA.toPlainText(),
                                self.lineEditValorA.text(),
                                '',
                                self.lineEditDescontoA.text(),
                                self.lineEditSinalA.text(),
                                str(self.lineEditDEDiaA.text() + self.lineEditDEMesA.text() + self.lineEditDEAnoA.text()))

                self.showdialog('Atualização do agendamento','O agendamento foi atualizado com sucesso')
        except:
                print('sem agendamento')

    def gerarReciboA(self):
            try:
                if(getAgendamentos(self.lineEditCPFA.text(),self.lineEditNomeA.text()) != ()):
                    print(getAgendamentos(self.lineEditCPFA.text(),self.lineEditNomeA.text()))
                    recibos.gerarRecibo(getClientes(self.lineEditCPFA.text(),self.lineEditNomeA.text())[0], getAgendamentos(self.lineEditCPFA.text(),self.lineEditNomeA.text()))
                    self.showdialog('Recibo do cliente','O recibo foi criado com sucesso')
                    os.startfile(os.path.dirname(os.path.abspath(__file__))+'\\recibos\\'+self.remover_acentos(getClientes(self.lineEditCPFA.text(),self.lineEditNomeA.text())[0][1])+'.png')
                        
                else:
                    self.showdialog('Agendamentos','Nao existe agendamento com essas informacoes')
            except:
                self.showdialog("Erro","Conclua o agendamento primeiro !")



##? Pagina Entregas da semana
    def gerarEntregas(self):
        self.itens = []
        self.entregas_segunda.clear()
        self.entregas_terca.clear()
        self.entregas_quarta.clear()
        self.entregas_quinta.clear()
        self.entregas_sexta.clear()
        self.entregas_sabado.clear()
        agendamentos = getAllAgendamentos()
        if(agendamentos != []):
            for agendamento in agendamentos:
                item = QtWidgets.QListWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                try:
                        dia = datetime(int(agendamento[10][4::]), int(agendamento[10][2:4]), int(agendamento[10][0:2]))
                except:
                        dia = datetime(2001,1,1)
                if(dia< datetime.today()):
                    item.setForeground(QtGui.QColor("red"))
                if(dia.isoweekday() == 1):
                    self.entregas_segunda.addItem(item)
                elif(dia.isoweekday() == 2):
                    self.entregas_terca.addItem(item)
                elif(dia.isoweekday() == 3):
                    self.entregas_quarta.addItem(item)
                elif(dia.isoweekday() == 4):
                    self.entregas_quinta.addItem(item)
                elif(dia.isoweekday() == 5):
                    self.entregas_sexta.addItem(item)
                elif(dia.isoweekday() == 6):
                    self.entregas_sabado.addItem(item)

                item.setText(agendamento[3])

                self.itens.append(item)

    def apagarAgendamento(self):
        try:
            aux = 0
            agendamentos = getAllAgendamentos()
            for item in self.itens:
                if(item.checkState()):
                    for agendamento in agendamentos:
                        if(item.text() == agendamento[3]):
                            self.entregas_segunda.takeItem(self.entregas_segunda.row(item))
                            self.itens.pop(self.itens.index(item))
                            aux = 1
                            removeAgendamento(agendamento[3],agendamento[0])
                            self.showdialog('Agendamento','O Agendamento foi removido com sucesso')

            if(aux == 1):
                self.gerarEntregas()
            else:
                self.showdialog('Entregas','Contrato nao selecionado')
        except:
            self.showdialog('Entregas','Contrato nao selecionado')

    def gerarContrato(self):
        try:
            agendamentos = getAllAgendamentos()
            for item in self.itens:
                if(item.checkState()):
                    for agendamento in agendamentos:
                        if(item.text() == agendamento[3]):
                            self.stackedWidget.setCurrentIndex(5)
                            self.lineEditCPFCTT.setText(str(agendamento[1]))
            self.buscarContrato()
        except:
            self.showdialog('Entregas','Agendamento nao selecionado')

    def editarAgendamento(self):
        try:
            agendamentos = getAllAgendamentos()
            for item in self.itens:
                if(item.checkState()):
                    for agendamento in agendamentos:
                        if(item.text() == agendamento[3]):
                            self.stackedWidget.setCurrentIndex(2)
                            self.lineEditCPFA.setText(str(agendamento[1]))
            self.procurarClienteA()
        except:
            self.showdialog('Entregas','Agendamento nao selecionado')

    def onListaClickedE(self,item):
        for i in self.itens:
            if(i != item):
                if (i.checkState() == QtCore.Qt.Checked):
                    i.setCheckState(QtCore.Qt.Unchecked)

##? Pagina de Devoluções

    def gerarDevolucoes(self):
        self.itensD = []
        self.devolucoes_segunda.clear()
        self.devolucoes_terca.clear()
        self.devolucoes_quarta.clear()
        self.devolucoes_quinta.clear()
        self.devolucoes_sexta.clear()
        self.devolucoes_sabado.clear()
        contratos = getAllContratos()
        if(contratos != []):
            for contrato in contratos:
                item = QtWidgets.QListWidgetItem()
                item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                item.setCheckState(QtCore.Qt.Unchecked)
                try:
                        dia = datetime(int(contrato[3][4::]), int(contrato[3][2:4]), int(contrato[3][0:2]))
                except:
                        dia = datetime(2001,1,1)
                if(dia< datetime.today()):
                    item.setForeground(QtGui.QColor("red"))
                if(dia.isoweekday() == 1):
                    self.devolucoes_segunda.addItem(item)
                elif(dia.isoweekday() == 2):
                    self.devolucoes_terca.addItem(item)
                elif(dia.isoweekday() == 3):
                    self.devolucoes_quarta.addItem(item)
                elif(dia.isoweekday() == 4):
                    self.devolucoes_quinta.addItem(item)
                elif(dia.isoweekday() == 5):
                    self.devolucoes_sexta.addItem(item)
                elif(dia.isoweekday() == 6):
                    self.devolucoes_sabado.addItem(item)
                else:
                    print('dia = domingo')
                item.setText(contrato[4])
                self.itensD.append(item)

    def onListaClickedD(self,item):
        aux = 0
        print(item.text())
        for i in self.itensD:
            if(i != item):
                if (i.checkState() == QtCore.Qt.Checked):
                    i.setCheckState(QtCore.Qt.Unchecked)

        for i in self.itensD:
            if (i.checkState() == QtCore.Qt.Checked):
                contratos = getAllContratos()
                if(contratos != []):
                    for contrato in contratos:
                        if(contrato[4] == item.text()):
                            dia = datetime(int(contrato[3][4::]), int(contrato[3][2:4]), int(contrato[3][0:2]))
                            if(dia< datetime.today()):
                                print((dia-datetime.today()).days)
                                self.labelMulta.setText("Multa: R$ "+str(-((dia-datetime.today()).days)*0.1*int(contrato[5])))
                            else:
                                self.labelMulta.setText("Multa: ")

    def apagarContrato(self):
        try:
            contratos = getAllContratos()
            for item in self.itensD:
                print('entrei')
                print(item,item.checkState())
                if(item.checkState()):
                    for contrato in contratos:
                        print(item.text(),contrato[4])
                        if(item.text() == contrato[4]):
                            self.itensD.pop(self.itensD.index(item))

                            removeContrato(contrato[1])
                            self.showdialog('Devolução','Iten Devolvido com sucesso')


            self.gerarDevolucoes()
        except:
            self.showdialog('Devolução','Erro ao atualizar devolução, reabra a janela')



##? Pagina Contratos

    def verificarContrato(self):
        aux = 0
        for i in self.listaCTT:
            if(i.text() == ''):
                i.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
                aux +=1
            else:
                i.setStyleSheet("border: 1px solid;border-color: rgb(0, 0, 0);font: 12pt \"Century Gothic\";")

        if(aux == 0):
            self.gerarContratoCTT()

    def buscarContrato(self):
        if(self.lineEditCPFCTT.text() != ''):
            try:
                cliente = getClientes(self.lineEditCPFCTT.text(),self.lineEditNomeCTT.text())[0]
                cliente=list(cliente)
                cliente.pop(0)
                if (cliente != ()):
                    self.lineEditNomeCTT.setText(str(cliente[0]))
                    self.lineEditEnderecoCTT.setText(str(cliente[5]))
                    self.lineEditNumeroCTT.setText(str(cliente[6]))
                    self.lineEditComplementoCTT.setText(str(cliente[7]))
                    self.lineEditDDD1CTT.setText(str(cliente[11][0:2]))
                    self.lineEditTelefone1CTT.setText(str(cliente[11][2::]))

                agendamentos = getAgendamentos(self.lineEditCPFCTT.text(),self.lineEditNomeCTT.text())
                if(agendamentos != []):
                    agendamentos = agendamentos[0]
                    self.textEditDescricaoCTT.setPlainText(agendamentos[3])
                    self.textEditAcessoriosCTT.setPlainText(agendamentos[4])
                    self.lineEditValorCTT.setText(agendamentos[6])
                    self.lineEditDescontoCTT.setText(agendamentos[8])
                    self.lineEditSinalCTT.setText(agendamentos[9])
                    self.lineEditDEDiaCTT.setText(str(agendamentos[10])[0:2])
                    self.lineEditDEMesCTT.setText(str(agendamentos[10])[2:4])
                    self.lineEditDEAnoCTT.setText(str(agendamentos[10])[4::])
                    itens = [self.comboBoxEventoCTT.itemText(i) for i in range(self.comboBoxEventoCTT.count())]
                    aux = 0
                    for i in itens:
                        if(i == agendamentos[2]):
                            break;
                        aux +=1
                    self.comboBoxEventoCTT.setCurrentIndex(aux)
            except:
                self.showdialog('ERRO- Contrato do cliente','Erro ao buscar cliente ou agendamento')
        else:
            self.lineEditCPFCTT.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")

    def remover_acentos(self,txt):
        return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

    def gerarContratoCTT(self):
        diad = datetime(int(self.lineEditDDAnoCTT.text()), int(self.lineEditDDMesCTT.text()), int(self.lineEditDDDiaCTT.text()))
        diae = datetime(int(self.lineEditDEAnoCTT.text()), int(self.lineEditDEMesCTT.text()), int(self.lineEditDEDiaCTT.text()))
        if((diad-diae).days > 0 and diad > datetime.today()):
            if(diad.isoweekday() != 7):
                try:
                    DDE = self.lineEditDDDiaCTT.text() + self.lineEditDDMesCTT.text() + self.lineEditDDAnoCTT.text()
                    contratos.gerarContrato(getClientes(self.lineEditCPFCTT.text(),self.lineEditNomeCTT.text())[0], getAgendamentos(self.lineEditCPFCTT.text(),self.lineEditNomeCTT.text())[0], DDE)
                    os.startfile(os.path.dirname(os.path.abspath(__file__))+'\\contratos\\'+self.remover_acentos(getClientes(self.lineEditCPFCTT.text(),self.lineEditNomeCTT.text())[0][1])+'.png')
                    agd = getAgendamentos(self.lineEditCPFCTT.text(),self.lineEditNomeCTT.text())[0]
                    maxId = self.findMaxIdCTT()
                    insertContrato(maxId,
                    self.lineEditCPFCTT.text(),
                    agd[0],
                    self.lineEditDDDiaCTT.text()+
                    self.lineEditDDMesCTT.text()+
                    self.lineEditDDAnoCTT.text(),agd[3],agd[6])
                    self.showdialog('Contrato do cliente','O Contrato foi agendado com sucesso')
                except:
                    self.showdialog('ERRO- Contrato do cliente','Erro Inesperado ao gerar contrato')
            else:
                self.showdialog('ERRO- Contrato do cliente','O Contrato nao pode ser gerado, pois a data de devolucao cai em um domingo ')
                self.lineEditDDDiaCTT.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
                self.lineEditDDMesCTT.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
                self.lineEditDDAnoCTT.setStyleSheet("border: 1px solid;border-color: rgb(255, 20, 35);font: 12pt \"Century Gothic\";")
        else:
            self.showdialog('Data', 'Erro nas datas de entrega ou devolucao')

    def closeEvent(self, event):
        print ("Closing the app")
        self.deleteLater()


##? Todas as páginas
    def showdialog(self,title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def findMaxId(self):
        conn = sqlite3.connect('BancoDeDados.db')
        cur = conn.cursor()

        cur.execute("SELECT ID FROM CLIENTES")
        ids = cur.fetchall()
        maxId = 0
        for id in ids:
            if(id[int(len(id)-1)]>=maxId):
                maxId = int(id[int(len(id)-1)])+1

        conn.commit()
        conn.close()
        return maxId

    def findMaxIdA(self):
        conn = sqlite3.connect('BancoDeDados.db')
        cur = conn.cursor()

        cur.execute("SELECT ID FROM AGENDAMENTOS")
        ids = cur.fetchall()
        maxId = 0
        for id in ids:
            if(id[int(len(id)-1)]>=maxId):
                maxId = int(id[int(len(id)-1)])+1

        conn.commit()
        conn.close()
        return maxId

    def findMaxIdCTT(self):
        conn = sqlite3.connect('BancoDeDados.db')
        cur = conn.cursor()

        cur.execute("SELECT ID FROM CONTRATOS")
        ids = cur.fetchall()
        maxId = 0
        for id in ids:
            if(id[int(len(id)-1)]>=maxId):
                maxId = int(id[int(len(id)-1)])+1

        conn.commit()
        conn.close()
        return maxId



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bttCadastro.setText(_translate("MainWindow", "Cadastro"))
        self.bttAgendamento.setText(_translate("MainWindow", "Agendamento"))
        self.bttSemanal.setText(_translate("MainWindow", "Semanal"))
        self.bttDevolucoes.setText(_translate("MainWindow", "Devoluções"))
        self.bttContrato.setText(_translate("MainWindow", "Contrato"))
        self.labelCadastroC_2.setText(_translate("MainWindow", "Cadastro do Cliente"))
        self.bttInicioCC.setText(_translate("MainWindow", "Início"))
        self.label_17.setText(_translate("MainWindow", "Complemento  "))
        self.label_19.setText(_translate("MainWindow", "Número  "))
        self.lineEditCidadeCC.setText(_translate("MainWindow", "Montes Claros"))
        self.label_29.setText(_translate("MainWindow", "Estado  "))
        self.label_30.setText(_translate("MainWindow", "Cidade  "))
        self.lineEditEstadoCC.setText(_translate("MainWindow", "MG"))
        self.label_31.setText(_translate("MainWindow", "Telefone 2       "))
        self.lineEditDDD2CC.setText(_translate("MainWindow", "38"))
        self.lineEditDDD1CC.setText(_translate("MainWindow", "38"))
        self.label_32.setText(_translate("MainWindow", ")  "))
        self.label_33.setText(_translate("MainWindow", "("))
        self.label_37.setText(_translate("MainWindow", "("))
        self.label_38.setText(_translate("MainWindow", ")  "))
        self.label_47.setText(_translate("MainWindow", "CPF"))
        self.label_42.setText(_translate("MainWindow", " / "))
        self.label_45.setText(_translate("MainWindow", " / "))
        self.label_59.setText(_translate("MainWindow", "Data de Nascimento"))
        self.label_3.setText(_translate("MainWindow", "Nome"))
        self.label_69.setText(_translate("MainWindow", "CEP"))
        self.label_67.setText(_translate("MainWindow", "Endereço"))
        self.label_66.setText(_translate("MainWindow", "Telefone 1"))
        self.label_68.setText(_translate("MainWindow", "Bairro"))
        self.bttBuscarCEPCC.setText(_translate("MainWindow", "Buscar"))
        self.label_70.setText(_translate("MainWindow", "RG  "))
        self.bttBuscarCPFCC.setText(_translate("MainWindow", "Buscar"))
        self.bttCadastarCC.setText(_translate("MainWindow", "Cadastrar"))
        self.bttAtualizarCC.setText(_translate("MainWindow", "Atualizar"))
        self.label_71.setText(_translate("MainWindow", "Agendamento"))
        self.bttInicioA.setText(_translate("MainWindow", "Início"))
        self.label_74.setText(_translate("MainWindow", "Endereço"))
        self.bttBuscarCPFA.setText(_translate("MainWindow", "Buscar"))
        self.label_72.setText(_translate("MainWindow", "Complemento  "))
        self.label_73.setText(_translate("MainWindow", "Número  "))
        self.label_75.setText(_translate("MainWindow", "("))
        self.lineEditDDD1A.setText(_translate("MainWindow", "38"))
        self.label_76.setText(_translate("MainWindow", ")  "))
        self.label_77.setText(_translate("MainWindow", "Nome"))
        self.label_78.setText(_translate("MainWindow", "CPF"))
        self.label_83.setText(_translate("MainWindow", "Evento"))
        self.label_82.setText(_translate("MainWindow", "Telefone 1"))
        self.bttBuscarEventoA.setText(_translate("MainWindow", "Buscar"))
        self.bttCriarEventoA.setText(_translate("MainWindow", "Criar"))
        self.label_85.setText(_translate("MainWindow", "Descrição"))
        self.label_88.setText(_translate("MainWindow", "Acessórios"))
        self.label_89.setText(_translate("MainWindow", "Ajustes"))
        self.label_92.setText(_translate("MainWindow", "Valor"))
        self.label_95.setText(_translate("MainWindow", "R$:"))
        self.label_113.setText(_translate("MainWindow", "Desconto"))
        self.label_114.setText(_translate("MainWindow", "Sinal"))
        self.label_115.setText(_translate("MainWindow", "Rs:"))
        self.label_116.setText(_translate("MainWindow", "Data Entrega"))
        self.label_117.setText(_translate("MainWindow", "/"))
        self.label_118.setText(_translate("MainWindow", "/"))
        self.bttGerarReciboA_2.setText(_translate("MainWindow", "Gerar recibo"))
        self.bttConcluirA_2.setText(_translate("MainWindow", "Concluir"))
        self.bttAtualizarA_2.setText(_translate("MainWindow", "Atualizar"))
        self.label_119.setText(_translate("MainWindow", "Entregas da Semana"))
        self.bttInicioSE.setText(_translate("MainWindow", "Iní­cio"))
        self.labelSegundaSE_2.setText(_translate("MainWindow", "Segunda"))
        self.labelTercaSE_2.setText(_translate("MainWindow", "Terça"))
        self.labelQuartaSE_2.setText(_translate("MainWindow", "Quarta"))
        self.labelQuintaSE_2.setText(_translate("MainWindow", "Quinta"))
        self.labelSextaSE_2.setText(_translate("MainWindow", "Sexta"))
        self.labelSabadoSE_2.setText(_translate("MainWindow", "Sábado"))
        __sortingEnabled = self.entregas_segunda.isSortingEnabled()
        self.entregas_segunda.setSortingEnabled(False)
        self.entregas_segunda.setSortingEnabled(__sortingEnabled)
        self.bttGerarContratoSE.setText(_translate("MainWindow", "Gerar Contrato"))
        self.bttApagarAgendamentoSE.setText(_translate("MainWindow", "Apagar"))
        self.bttEditarAgendamentoSE.setText(_translate("MainWindow", "Editar"))
        self.label_120.setText(_translate("MainWindow", "Devoluções da Semana"))
        self.bttInicioDS.setText(_translate("MainWindow", "Início"))
        __sortingEnabled = self.devolucoes_segunda.isSortingEnabled()
        self.devolucoes_segunda.setSortingEnabled(False)
        self.devolucoes_segunda.setSortingEnabled(__sortingEnabled)
        self.labelSextaDS_3.setText(_translate("MainWindow", "Sexta"))
        self.labelQuartaDS_3.setText(_translate("MainWindow", "Quarta"))
        self.labelQuintaDS_3.setText(_translate("MainWindow", "Quinta"))
        self.labelTercaDS_3.setText(_translate("MainWindow", "Terça"))
        self.labelSegundaDS_3.setText(_translate("MainWindow", "Segunda"))
        self.labelSabadoDS_3.setText(_translate("MainWindow", "Sábado"))
        self.labelMulta.setText(_translate("MainWindow", "Multa: "))
        self.bttDevolvidoDS.setText(_translate("MainWindow", "Devolvido"))
        self.label_121.setText(_translate("MainWindow", "Contrato"))
        self.bttInicioCTT.setText(_translate("MainWindow", "Iní­cio"))
        self.label_122.setText(_translate("MainWindow", "Endereço"))
        self.bttBuscarCPFCTT.setText(_translate("MainWindow", "Buscar"))
        self.label_123.setText(_translate("MainWindow", "Complemento  "))
        self.label_124.setText(_translate("MainWindow", "Número  "))
        self.lineEditDDD1CTT.setText(_translate("MainWindow", "38"))
        self.label_125.setText(_translate("MainWindow", ")  "))
        self.label_126.setText(_translate("MainWindow", "("))
        self.label_127.setText(_translate("MainWindow", "CPF"))
        self.label_128.setText(_translate("MainWindow", "Nome"))
        self.label_130.setText(_translate("MainWindow", "Telefone 1"))
        self.label_131.setText(_translate("MainWindow", "Evento"))
        self.bttBuscarEventoCTT.setText(_translate("MainWindow", "Buscar"))
        self.bttCriarEventoCTT.setText(_translate("MainWindow", "Criar"))
        self.label_133.setText(_translate("MainWindow", "Descrição"))
        self.label_134.setText(_translate("MainWindow", "Acessórios"))
        self.label_135.setText(_translate("MainWindow", "Valor"))
        self.label_136.setText(_translate("MainWindow", "R$:"))
        self.label_138.setText(_translate("MainWindow", "Desconto"))
        self.label_139.setText(_translate("MainWindow", "Sinal"))
        self.label_140.setText(_translate("MainWindow", "Rs:"))
        self.label_141.setText(_translate("MainWindow", "Data Entrega"))
        self.label_142.setText(_translate("MainWindow", "/"))
        self.label_143.setText(_translate("MainWindow", "/"))
        self.label_144.setText(_translate("MainWindow", "Data de Devolução"))
        self.label_145.setText(_translate("MainWindow", "/"))
        self.label_146.setText(_translate("MainWindow", "/"))
        self.bttGerarContratoCTT.setText(_translate("MainWindow", "Gerar contrato"))


import imgs

import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
"""
A
















































"""