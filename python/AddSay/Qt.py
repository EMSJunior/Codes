# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jumen\Documents\Codes\python\AddSay\Qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from re import S
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os

from numpy import choose


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 470)
        MainWindow.setStyleSheet("background-color: rgb(79, 79, 79);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameFundo = QtWidgets.QFrame(self.centralwidget)
        self.frameFundo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameFundo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameFundo.setObjectName("frameFundo")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameFundo)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameTextCima = QtWidgets.QFrame(self.frameFundo)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frameTextCima.sizePolicy().hasHeightForWidth())
        self.frameTextCima.setSizePolicy(sizePolicy)
        self.frameTextCima.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTextCima.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTextCima.setObjectName("frameTextCima")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameTextCima)
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelA = QtWidgets.QLabel(self.frameTextCima)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.labelA.sizePolicy().hasHeightForWidth())
        self.labelA.setSizePolicy(sizePolicy)
        self.labelA.setMaximumSize(QtCore.QSize(55, 16777215))
        self.labelA.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "")
        self.labelA.setObjectName("labelA")
        self.horizontalLayout_2.addWidget(self.labelA)
        spacerItem = QtWidgets.QSpacerItem(
            50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.labelS = QtWidgets.QLabel(self.frameTextCima)
        self.labelS.setStyleSheet("color: rgb(255, 255, 255);")
        self.labelS.setObjectName("labelS")
        self.horizontalLayout_2.addWidget(self.labelS)
        self.pushButtonEdit = QtWidgets.QPushButton(self.frameTextCima)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButtonEdit.sizePolicy().hasHeightForWidth())
        self.pushButtonEdit.setSizePolicy(sizePolicy)
        self.pushButtonEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButtonEdit.setStyleSheet("QPushButton{\n"
                                          "background-color: rgb(170, 0, 0); \n"
                                          "color: rgb(0,0,0);\n"
                                          "border-radius:5px;\n"
                                          "}QPushButton::hover{\n"
                                          "background-color: rgb(170, 0, 0); \n"
                                          "color: rgb(255,255,255);\n"
                                          "border-radius:5px;\n"
                                          "}QPushButton::pressed{\n"
                                          "background-color: rgb(209, 100, 100); \n"
                                          "color: rgb(255,255,255);\n"
                                          "border-radius:5px;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout_2.addWidget(self.pushButtonEdit)
        self.verticalLayout_2.addWidget(self.frameTextCima)
        self.frameAdd = QtWidgets.QFrame(self.frameFundo)
        self.frameAdd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAdd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAdd.setObjectName("frameAdd")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameAdd)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditA = QtWidgets.QLineEdit(self.frameAdd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEditA.sizePolicy().hasHeightForWidth())
        self.lineEditA.setSizePolicy(sizePolicy)
        self.lineEditA.setMaximumSize(QtCore.QSize(55, 16777215))
        self.lineEditA.setObjectName("lineEditA")
        self.horizontalLayout.addWidget(self.lineEditA)
        self.lineEditS = QtWidgets.QLineEdit(self.frameAdd)
        self.lineEditS.setObjectName("lineEditS")
        self.horizontalLayout.addWidget(self.lineEditS)
        self.pushButtonOk = QtWidgets.QPushButton(self.frameAdd)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButtonOk.sizePolicy().hasHeightForWidth())
        self.pushButtonOk.setSizePolicy(sizePolicy)
        self.pushButtonOk.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButtonOk.setStyleSheet("QPushButton{\n"
                                        "background-color: rgb(104,171,75); \n"
                                        "color: rgb(0,0,0);\n"
                                        "border-radius:5px;\n"
                                        "}QPushButton::hover{\n"
                                        "background-color: rgb(104,171,75); \n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius:5px;\n"
                                        "}QPushButton::pressed{\n"
                                        "background-color: rgb(154,231,125); \n"
                                        "color: rgb(255,255,255);\n"
                                        "border-radius:5px;\n"
                                        "}")
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.verticalLayout_2.addWidget(self.frameAdd)
        self.Tabela = QtWidgets.QTableWidget(self.frameFundo)
        self.Tabela.setStyleSheet("color: rgb(255, 255, 255);")
        self.Tabela.setObjectName("Tabela")
        self.Tabela.setColumnCount(2)
        self.Tabela.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tabela.setItem(0, 1, item)
        self.Tabela.horizontalHeader().setVisible(False)
        self.Tabela.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.Tabela)
        self.frame = QtWidgets.QFrame(self.frameFundo)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frameFundo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Say\'s - By Ehpsker"))
        self.labelA.setText(_translate("MainWindow", "Atalho"))
        self.labelS.setText(_translate("MainWindow", "Say"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Remove"))
        self.pushButtonOk.setText(_translate("MainWindow", "Add"))
        item = self.Tabela.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.Tabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Atalho"))
        item = self.Tabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Say"))
        __sortingEnabled = self.Tabela.isSortingEnabled()
        self.Tabela.setSortingEnabled(False)
        self.Tabela.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "Caminho"))

        header = self.Tabela.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.textobase = "//Olá amiginho, se compartilhar, não se esqueça dos creditos!\n\n//==================================================\n// Comandos da cfg:\n\n	alias \"sa\" \"clear;exec mc-say_by_Ehpsker\"\n\n\n//=================================================\n\n// COMANDOS FINAIS SEQUENCIADOS E TEXTO EXIBIDO NO CONSOLE\n\nclear\nECHO ==================================================\nECHO \nECHO CFG: mc-Say by Ehpsker.cfg\nECHO \nECHO O arquivo foi carregado com sucesso!\nECHO \nECHO AUTOR: Ehpsker\nECHO \nECHO O programa usado na criacao e edicao desta CFG foi o Notepad++.\nECHO \nECHO DATA DA ULTIMA EDICAO: 01/09/2021\nECHO \nECHO ==================================================\nECHO\nECHO Intrucoes: \nECHO\nECHO Para aparecer a lista, basta mandar no console 'sa' (sem aspa')\nECHO Depois de escolhido o say, so colocar no console o texto anterior a frase!\nECHO Ex: \nECHO mu - Ativaram o wi-fi no museu, tem 3 australopithecus jogando. \nECHO se vc digitar \"mu\", sera mandado no chat: Ativaram o wi-fi no museu, tem 3 australopithecus jogando.\nECHO\nECHO ==================================================\nECHO\nECHO ================================================== \nECHO Say da GC agora no MM! By Ehpsker \nECHO ================================================== \nECHO So digitar aqui no console! \nECHO ================================================== \nECHO \nECHO Lista de xigamentos/elogios : ( use com moderacao )"
        self.textofinal = "mc-say_by_Ehpsker.cfg"
        self.dados = []
        self.atalhos = []
        self.Tabela.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.acharcfg()

        self.pushButtonOk.clicked.connect(lambda: self.call())
        self.lineEdit.returnPressed.connect(lambda: self.definircaminho())
        self.Tabela.cellDoubleClicked.connect(lambda: self.avisoapagar())

    def avisoapagar(self):
        aviso = QMessageBox()
        aviso.setIcon(QMessageBox.Question)
        atalho = self.dados[self.Tabela.currentRow()]["atalho"]
        text = "Deseja apagar o atalho \""+atalho+"\" ?"
        aviso.setText(text)
        aviso.setWindowTitle("Apagar")
        aviso.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        chose = aviso.exec_()
        if chose == QMessageBox.Yes:
            try:
                self.apagar(atalho)
            except:
                self.erroapagar()

    def erroapagar(self):
        aviso = QMessageBox()
        aviso.setIcon(QMessageBox.Critical)
        atalho = self.dados[self.Tabela.currentRow()]["atalho"]
        text = "Erro ao apagar \""+atalho+"\"."
        aviso.setText(text)
        aviso.setWindowTitle("Erro")
        aviso.setStandardButtons(QMessageBox.Ok)
        chose = aviso.exec_()

    def apagar(self, atalho):
        say = self.dados[self.Tabela.currentRow()]["say"]
        linha=("ECHO " + atalho + self.contarletrasA(atalho) +say + " ;alias \"" + atalho + "\" \"say "+say+"\"\n")
        self.cfg.remove(linha)
        texto=""
        for i in self.cfg:
            texto += i
        with open(self.path,'w', encoding='UTF8') as cfg:
            cfg.write(texto)
        self.f5()


    def patherro(self):
        patherr = QMessageBox()
        patherr.setIcon(QMessageBox.Warning)
        patherr.setText(
            "Por favor verifique o local do arquivo!")
        patherr.setWindowTitle("Local não encontrado")
        patherr.setStandardButtons(QMessageBox.Yes)
        patherr.exec_()

    def acharcfg(self):
        if os.path.isdir("C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\csgo\cfg"):
            try:
                self.path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\mc-say_by_Ehpsker.cfg"
                self.f5()
            except:
                self.criarcfg()
            self.path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\mc-say_by_Ehpsker.cfg"
            self.lineEdit.setText(self.path)
        else:
            try:
                self.verivicartxt()
                self.lineEdit.setText(self.path)
            except:
                self.errocaminho()

    def verivicartxt(self):
        with open("cfg diretório_SayByEhpsker.txt", "r", encoding="utf-8") as txt:
            file = txt.read()
            try:
                lenf = len(file)
                if file[lenf-len(self.textofinal):lenf] == self.textofinal:
                    self.path = file
                    self.f5()
                else:
                    self.errocaminho()
            except:
                self.errocaminho()

    def definircaminho(self):
        caminho = self.lineEdit.text()
        if caminho != self.path:
            lenc = len(caminho)
            lent = len(self.textofinal)
            if caminho[lenc-lent:lenc] == self.textofinal:
                self.path = (caminho)
            else:
                self.path = (caminho + "\\mc-say_by_Ehpsker.cfg")
            try:
                self.f5()
                self.avisonovoarquivo()
            except:
                self.patherro()

    def avisonovoarquivo(self):
        newfile = QMessageBox()
        newfile.setIcon(QMessageBox.Information)
        newfile.setText(
            "Como o diretório do jogo é diferente, tem que ser criado um aquivo .txt, para que das próximas vezes que abrir o programa, não precise digitar.\n\n Criar o aquivo?")
        newfile.setWindowTitle("Novo Arquivo")
        newfile.setStandardButtons(QMessageBox.Yes | QMessageBox.Ignore)
        chose = newfile.exec_()

        if chose == QMessageBox.Yes:
            self.criartxt()

    def criartxt(self):
        with open("cfg diretório_SayByEhpsker.txt", "w") as txt:
            txt.write(self.path)

    def errocaminho(self):
        nopath = QMessageBox()
        nopath.setIcon(QMessageBox.Warning)
        nopath.setText(
            "Por favor insira o diretorio \\cfg do csgo!\n\nExemplo: \n\'C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\' .")
        nopath.setWindowTitle("Sem caminho")
        nopath.setStandardButtons(QMessageBox.Ok)
        nopath.exec_()

    def criarcfg(self):
        with open("C:\\Program Files (x86)\\Steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo\\cfg\\mc-say_by_Ehpsker.cfg", 'w+', encoding='UTF8') as aux:
            aux.write(self.textobase)

    def call(self):
        if self.lineEditS.text() and self.lineEditA.text():
            self.additem()
        else:
            self.f5
        self.f5()
        self.Tabela.scrollToBottom()

    def jaexiste(self):
        nopath = QMessageBox()
        nopath.setIcon(QMessageBox.Warning)
        nopath.setText(
            "Atalho já existente!")
        nopath.setWindowTitle("Erro")
        nopath.setStandardButtons(QMessageBox.Ok)
        nopath.exec_()

    def verificasaspas(self):
        if "\"" in self.lineEditA.text():
            self.lineEditA.setText(self.lineEditA.text().replace('"', "'"))
        if "\"" in self.lineEditS.text():
            self.lineEditS.setText(self.lineEditS.text().replace('"', "'"))

    def additem(self):
        self.verificasaspas()

        if self.lineEditA.text() in self.atalhos:
            self.jaexiste()
        else:
            self.linha = "\nECHO " + str(self.lineEditA.text()) + str(self.contarletrasA(self.lineEditA.text())) + str(self.lineEditS.text(
            )) + " ;alias \"" + str(self.lineEditA.text()) + "\" \"say "+str(self.lineEditS.text())+"\"\n"
            self.finaltext = ''.join([str(item) for item in self.cfg])
            self.finaltext += self.linha
            with open(self.path, 'w', encoding='utf-8') as conf:
                txtt = conf.write(self.finaltext)
            self.lineEditS.setText("")
            self.lineEditA.setText("")

    def contarletrasA(self, txt):
        n = len(txt)
        setinhas = " "
        for i in range(8-n):
            setinhas += "-"
        setinhas += "> "
        return(setinhas)

    def pegaratalho(self, texto):
        alias = ";alias \""
        posI = texto.index(alias)+len(alias)
        posF = texto.index("\" \"")
        atalho = texto[posI:posF]
        self.atalhos.append(atalho)
        return(atalho)

    def pegarsay(self, texto):
        sayr = "\"say "
        posI = texto.index(sayr)+len(sayr)
        posF = texto.index("\n")-1
        say = texto[posI:posF]
        return(say)

    def pegardados(self):
        self.dados = []
        with open(self.path, 'r', encoding='UTF8') as conf:
            self.cfg = conf.readlines()

        for j in range(len(self.cfg)):
            try:
                atalho = self.pegaratalho(self.cfg[j])
                say = self.pegarsay(self.cfg[j])
                self.dado = {"atalho": ""+atalho+"", "say": ""+say+""}
                self.dados.append(self.dado)
            except:
                p = 0

    def f5(self):
        self.pegardados()
        self.Tabela.setRowCount(len(self.dados))
        for i in range(len(self.dados)):
            self.Tabela.setItem(i, 0, QtWidgets.QTableWidgetItem(
                str(self.dados[i]["atalho"])))
            self.Tabela.setItem(i, 1, QtWidgets.QTableWidgetItem(
                str(self.dados[i]["say"])))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
