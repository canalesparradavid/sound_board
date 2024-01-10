import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt, QObject
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
        self.actual_matrix = 1

        # Reproduzco sonido de arrancado
        self.config.boot_sound.play()

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

        # Agregar botones de menu
        back_button = QPushButton('<---', self)
        back_button.clicked.connect(self.back_matrixes)
        self.layout.addWidget(back_button, 0, 0)
        reset_button = QPushButton('Reset', self)
        reset_button.clicked.connect(self.reset)
        self.layout.addWidget(reset_button, 0, 1)
        advance_button = QPushButton('--->', self)
        advance_button.clicked.connect(self.advance_matrixes)
        self.layout.addWidget(advance_button, 0, 2)

        # Agregar botones de sonido de la matriz actual en forma de matriz (3x3)
        for row in range(self.config.dimension[0]):
            for col in range(self.config.dimension[1]):
                index = row * self.config.dimension[1] + col
                if index < len(self.config.sounds[self.board.actual_matrix]):
                    sound = self.config.sounds[self.board.actual_matrix][index]
                    btn = QPushButton(sound.name, self)
                    btn.clicked.connect(lambda _, sound=sound: sound.switch_sound())
                    self.layout.addWidget(btn, row + 1, col)

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

    def reset(self):
        self.board.stop_all()
        print("reset")

    def advance_matrixes(self):
        max_matrix_index = len(self.config.sounds)
        if (self.actual_matrix == max_matrix_index):
            return
        self.actual_matrix = self.actual_matrix + 1
        self.board.switch_change_option()
        self.board.change_to_matrix(self.actual_matrix - 1)
        self.update_buttons()

    def back_matrixes(self):
        if (self.actual_matrix == 1):
            return
        self.actual_matrix = self.actual_matrix - 1
        self.board.switch_change_option()
        self.board.change_to_matrix(self.actual_matrix - 1)
        self.update_buttons()

def start_board():
    app = QApplication(sys.argv)
    ex = TablaSonidosApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start_board()
