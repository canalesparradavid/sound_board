import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import pygame

from config import Config

canChangematrix = False

class TablaSonidosApp(QWidget):
    def __init__(self):
        super().__init__()

        # Cargo la configuracion
        self.config = Config("config.json")

        self.sounds_path = self.config.sound_path       # Directorio de sonidos
        self.matrices_sonidos = self.config.sounds      # Lista de matrices de sonidos
        self.matriz_actual = 0                          # Índice de la matriz actual

        # Inicializar pygame para la reproducción de sonido
        pygame.init()

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
                if index < len(self.matrices_sonidos[self.matriz_actual]):
                    sound = self.matrices_sonidos[self.matriz_actual][index]
                    btn = QPushButton(sound.name, self)
                    btn.clicked.connect(lambda _, sound=sound, pygame=pygame: sound.switch_sound(pygame))
                    self.layout.addWidget(btn, row, col)

    def keyPressEvent(self, event):
        modifiers = event.modifiers()
        key = event.key()

        # Reproducir el sonido con Ctrl+NUM
        if modifiers == Qt.AltModifier:
            # Habilitar cambio
            global canChangematrix
            canChangematrix = not canChangematrix
        elif not canChangematrix and ord('a')-32 <= key <= ord('z')-32:
            #Reproducir sonido
            index = key - 65
            if 0 <= index < len(self.matrices_sonidos[self.matriz_actual]):
                sound = self.matrices_sonidos[self.matriz_actual][index]
                sound.switch_sound(pygame)
        # Cambiar de matriz de sonidos
        elif canChangematrix and Qt.Key_0 <= key <= Qt.Key_9:
            # Cambiar y bloquear cambio
            index = key - Qt.Key_0 - 1
            if 0 <= index < len(self.matrices_sonidos):
                self.matriz_actual = index
                self.update_buttons()
            canChangematrix = False
        # Parar todos los sonidos
        elif Qt.Key_Escape == key:
            for matrix in self.matrices_sonidos:
                for sound in matrix:
                    sound.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TablaSonidosApp()
    ex.show()
    sys.exit(app.exec_())
