# Desenvolvendo este projeto para verificar meu conhecimento em segurança da informação e Forense digital.
# Kevin Moreira (c), 2023
# 15/12/23

# PROJETO DESENVOLVIDO COM AUXÍLO DO GPT 3.5 (versão gratuita)

# Bibliotecas necessários (ou talvez não)

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget

import img

# Instãncia 

class Alert(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("warning.ui", self)
        self.setWindowTitle("Nossa ética - CardPass Crasher")

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.quit.clicked.connect(self.close)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'drag_start_position') and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_start_position)

        self.show

class splashScreen(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("splashScreen.ui", self)
        self.setWindowTitle("CardPass Crasher")

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.timer_interval = 10
        self.progress_value = 0

        self.timer.start(self.timer_interval)

    def update_progress(self):
        self.progress_value += 1
        self.progressBar.setValue(self.progress_value)

        if self.progress_value == 100:
            self.timer.stop()
            self.close()
            alert = Alert()
            alert.exec_()
        else:
            self.show()

# Execução ou Prompt (Ou outra coisa que tu quiser chamar)        

app = QtWidgets.QApplication(sys.argv)
SplashScreen = splashScreen()
SplashScreen.show()
app.exec_()