import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import pygame

from config import Config
from board import Board

class TablaSonidosApp(QWidget):
    def __init__(self):
        super().__init__()

        # Inicializar pygame para la reproducción de sonido
        pygame.init()

        # Cargo la configuracion
        self.config = Config("config.json", pygame)
        self.board = Board(self.config)

        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()

        # Agregar botones de sonido de la matriz actual
        self.update_buttons()

        self.setLayout(self.layout)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tabla de Sonidos')

    def update_buttons(self):
        # Limpiar botones existentes
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)

        # Agregar botones de sonido de la matriz actual en forma de matriz (3x3)
        for row in range(self.config.dimension[0]):
            for col in range(self.config.dimension[1]):
                index = row * self.config.dimension[1] + col
                if index < len(self.config.sounds[self.board.actual_matrix]):
                    sound = self.config.sounds[self.board.actual_matrix][index]
                    btn = QPushButton(sound.name, self)
                    btn.clicked.connect(lambda _, sound=sound: sound.switch_sound())
                    self.layout.addWidget(btn, row, col)

    def keyPressEvent(self, event):
        modifiers = event.modifiers()
        key = event.key()

        # Reproducir el sonido con Ctrl+NUM
        if modifiers == Qt.AltModifier:
            self.board.switch_change_option()
            print("changed")
        elif not self.board.can_change_matrix and ord('a')-32 <= key <= ord('z')-32:
            #Reproducir sonido
            index = key - 65
            self.board.play_sound(index)
        # Cambiar de matriz de sonidos
        elif self.board.can_change_matrix and Qt.Key_0 <= key <= Qt.Key_9:
            # Cambiar y bloquear cambio
            index = key - Qt.Key_0 - 1
            self.board.change_to_matrix(index)
            self.update_buttons()
        # Parar todos los sonidos
        elif Qt.Key_Escape == key:
            self.board.stop_all()


'''if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TablaSonidosApp()
    ex.show()
    sys.exit(app.exec_())'''

def start_board():
    app = QApplication(sys.argv)
    ex = TablaSonidosApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start_board()
