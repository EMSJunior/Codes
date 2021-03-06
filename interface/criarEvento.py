# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'criarEvento.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import functions
from datetime import datetime

class Ui_CriarEvento(object):
    def setupUi(self, CriarEvento,escolha,dados):
        CriarEvento.setObjectName("CriarEvento")
        CriarEvento.resize(550, 538)
        CriarEvento.setMaximumSize(QtCore.QSize(550, 16777215))
        CriarEvento.setStyleSheet("background-image: url(:/fundo/fundo.png);")
        self.centralwidgetCE = QtWidgets.QWidget(CriarEvento)
        self.centralwidgetCE.setObjectName("centralwidgetCE")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidgetCE)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3CE = QtWidgets.QFrame(self.centralwidgetCE)
        self.frame_3CE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3CE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3CE.setObjectName("frame_3CE")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3CE)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelNomeCE = QtWidgets.QLabel(self.frame_3CE)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.labelNomeCE.setFont(font)
        self.labelNomeCE.setObjectName("labelNomeCE")
        self.horizontalLayout.addWidget(self.labelNomeCE)
        self.lineEditNomeCE = QtWidgets.QLineEdit(self.frame_3CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.lineEditNomeCE.sizePolicy().hasHeightForWidth())
        self.lineEditNomeCE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEditNomeCE.setFont(font)
        self.lineEditNomeCE.setStyleSheet("background-color: transparent;")
        self.lineEditNomeCE.setObjectName("lineEditNomeCE")
        self.horizontalLayout.addWidget(self.lineEditNomeCE)
        spacerItem = QtWidgets.QSpacerItem(50, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_3CE)
        self.frameCE = QtWidgets.QFrame(self.centralwidgetCE)
        self.frameCE.setStyleSheet("background:transparent;")
        self.frameCE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCE.setObjectName("frameCE")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frameCE)
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5CE = QtWidgets.QFrame(self.frameCE)
        self.frame_5CE.setStyleSheet("background:transparent;")
        self.frame_5CE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5CE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5CE.setObjectName("frame_5CE")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5CE)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelDataCE = QtWidgets.QLabel(self.frame_5CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDataCE.sizePolicy().hasHeightForWidth())
        self.labelDataCE.setSizePolicy(sizePolicy)
        self.labelDataCE.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.labelDataCE.setFont(font)
        self.labelDataCE.setObjectName("labelDataCE")
        self.horizontalLayout_2.addWidget(self.labelDataCE, 0, QtCore.Qt.AlignLeft)
        self.frame_6CE = QtWidgets.QFrame(self.frame_5CE)
        self.frame_6CE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6CE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6CE.setObjectName("frame_6CE")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6CE)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEditDiaNCE = QtWidgets.QLineEdit(self.frame_6CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditDiaNCE.sizePolicy().hasHeightForWidth())
        self.lineEditDiaNCE.setSizePolicy(sizePolicy)
        self.lineEditDiaNCE.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEditDiaNCE.setFont(font)
        self.lineEditDiaNCE.setStyleSheet("background-color: transparent;")
        self.lineEditDiaNCE.setObjectName("lineEditDiaNCE")
        self.horizontalLayout_5.addWidget(self.lineEditDiaNCE)
        self.label_5 = QtWidgets.QLabel(self.frame_6CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEditMesNCE = QtWidgets.QLineEdit(self.frame_6CE)
        self.lineEditMesNCE.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEditMesNCE.setFont(font)
        self.lineEditMesNCE.setStyleSheet("background-color: transparent;")
        self.lineEditMesNCE.setObjectName("lineEditMesNCE")
        self.horizontalLayout_5.addWidget(self.lineEditMesNCE)
        self.label_6 = QtWidgets.QLabel(self.frame_6CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.lineEditAnoNCE = QtWidgets.QLineEdit(self.frame_6CE)
        self.lineEditAnoNCE.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEditAnoNCE.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lineEditAnoNCE.setFont(font)
        self.lineEditAnoNCE.setStyleSheet("background-color: transparent;")
        self.lineEditAnoNCE.setObjectName("lineEditAnoNCE")
        self.horizontalLayout_5.addWidget(self.lineEditAnoNCE)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.frame_6CE)
        self.horizontalLayout_4.addWidget(self.frame_5CE)
        self.verticalLayout.addWidget(self.frameCE)
        self.frame_4CE = QtWidgets.QFrame(self.centralwidgetCE)
        self.frame_4CE.setStyleSheet("background:transparent;")
        self.frame_4CE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4CE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4CE.setObjectName("frame_4CE")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4CE)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bttCriarCE = QtWidgets.QPushButton(self.frame_4CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bttCriarCE.sizePolicy().hasHeightForWidth())
        self.bttCriarCE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Sofia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bttCriarCE.setFont(font)
        self.bttCriarCE.setStyleSheet("QPushButton{\n"
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
        self.bttCriarCE.setIconSize(QtCore.QSize(16, 16))
        self.bttCriarCE.setObjectName("bttCriarCE")
        self.horizontalLayout_3.addWidget(self.bttCriarCE, 0, QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_4CE)
        self.frame_2CE = QtWidgets.QFrame(self.centralwidgetCE)
        self.frame_2CE.setAutoFillBackground(False)
        self.frame_2CE.setStyleSheet("background:transparent;")
        self.frame_2CE.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2CE.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2CE.setObjectName("frame_2CE")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2CE)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidgetCE = QtWidgets.QTableWidget(self.frame_2CE)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableWidgetCE.sizePolicy().hasHeightForWidth())
        self.tableWidgetCE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidgetCE.setFont(font)
        self.tableWidgetCE.setAutoFillBackground(False)
        self.tableWidgetCE.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetCE.setLineWidth(1)
        self.tableWidgetCE.setMidLineWidth(0)
        self.tableWidgetCE.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetCE.setIconSize(QtCore.QSize(0, 0))
        self.tableWidgetCE.setShowGrid(True)
        self.tableWidgetCE.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetCE.setWordWrap(True)
        self.tableWidgetCE.setObjectName("tableWidgetCE")
        self.tableWidgetCE.setColumnCount(2)
        self.tableWidgetCE.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidgetCE.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sofia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCE.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Sofia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidgetCE.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCE.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetCE.setItem(0, 1, item)
        self.tableWidgetCE.horizontalHeader().setDefaultSectionSize(251)
        self.tableWidgetCE.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidgetCE.verticalHeader().setDefaultSectionSize(25)
        self.tableWidgetCE.verticalHeader().setMinimumSectionSize(20)
        self.gridLayout.addWidget(self.tableWidgetCE, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_2CE)
        CriarEvento.setCentralWidget(self.centralwidgetCE)
        self.eventos = ''
        self.escolha = escolha
        self.dados = dados

        if(self.escolha != 1 and escolha != ''):
            self.bttCriarCE.setEnabled(False)
            self.getEventos()
            self.lineEditNomeCE.setText(self.escolha)
            self.lineEditNomeCE.setReadOnly(True)
            self.lineEditDiaNCE.setReadOnly(True)
            self.lineEditMesNCE.setReadOnly(True)
            self.lineEditAnoNCE.setReadOnly(True)
        else:
            self.eventos = functions.getAllEventos()




        self.bttCriarCE.clicked.connect(self.createEvento)

        self.retranslateUi(CriarEvento)
        QtCore.QMetaObject.connectSlotsByName(CriarEvento)

    def getEventos(self):
        self.eventos = functions.getAllEventos()
        if(self.eventos is not None):

            for i in self.eventos:
                if(i[0] == self.escolha):
                    item = self.tableWidgetCE.item(0, 0)
                    item.setText(i[1])
                    item = self.tableWidgetCE.item(0, 1)
                    item.setText(i[2])
                    print(i[3])
                    self.lineEditDiaNCE.setText(i[3][0]+i[3][1])
                    self.lineEditMesNCE.setText(i[3][3::5])
                    self.lineEditAnoNCE.setText(i[3][6::])




    def createEvento(self):
        if(self.lineEditNomeCE.text() != '' and self.lineEditDiaNCE.text() != '' and self.lineEditMesNCE.text() != '' and self.lineEditAnoNCE.text() != ''):
            self.eventos = functions.getAllEventos()
            aux = 0
            for i in self.eventos:
                if(i[0] == self.lineEditNomeCE.text()):
                    aux = 1

            if(aux == 0):
                functions.insertEvento(self.lineEditNomeCE.text(),self.dados[0],self.dados[2],str(self.lineEditDiaNCE.text()+'/'+self.lineEditMesNCE.text()+'/'+self.lineEditAnoNCE.text()))
                self.showdialog2('Criar Evento','Evento Criado com sucesso')
                QtCore.QCoreApplication.instance().quit
            else:
                self.showdialog2('ERRO-Criar Evento','O Evento ja existe')
                QtCore.QCoreApplication.instance().quit
    
    def showdialog2(self,title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)

        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def retranslateUi(self, CriarEvento):
        _translate = QtCore.QCoreApplication.translate
        CriarEvento.setWindowTitle(_translate("CriarEvento", "MainWindow"))
        self.frame_3CE.setStyleSheet(_translate("CriarEvento", "background:transparent;"))
        self.labelNomeCE.setText(_translate("CriarEvento", "Nome do evento"))
        self.labelDataCE.setText(_translate("CriarEvento", "Data"))
        self.label_5.setText(_translate("CriarEvento", "/"))
        self.label_6.setText(_translate("CriarEvento", "/"))
        self.bttCriarCE.setText(_translate("CriarEvento", "Criar evento"))
        self.tableWidgetCE.setSortingEnabled(False)
        item = self.tableWidgetCE.horizontalHeaderItem(0)
        item.setText(_translate("CriarEvento", "Nome"))
        item = self.tableWidgetCE.horizontalHeaderItem(1)
        item.setText(_translate("CriarEvento", "Fantasia"))
        __sortingEnabled = self.tableWidgetCE.isSortingEnabled()
        self.tableWidgetCE.setSortingEnabled(False)
        self.tableWidgetCE.setSortingEnabled(__sortingEnabled)
import imgFundo
"""
lista = ['Aniversario da lola', 'Luiz Otavio Antunes GOncalves', 'CHico Bento', '02/12/2021']
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Ui_CriarEvento()
ui.setupUi(window,lista,[])
window.show()
sys.exit(app.exec_())
"""