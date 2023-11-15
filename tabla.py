import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
import pygame

from config import Config

class TablaSonidosApp(QWidget):
    def __init__(self):
        super().__init__()

        # Cargo la configuracion
        self.config = Config("config.json")

        # Directorio de sonidos
        self.sounds_path = self.config.sound_path

        # Lista de matrices de sonidos
        self.matrices_sonidos = self.config.sounds

        # Índice de la matriz actual
        self.matriz_actual = 0

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
                    nombre, _ = self.matrices_sonidos[self.matriz_actual][index]
                    btn = QPushButton(nombre, self)
                    btn.clicked.connect(lambda _, nombre=nombre: self.play_sound(nombre))
                    self.layout.addWidget(btn, row, col)

    def play_sound(self, nombre):
        # Obtener la ruta del sonido correspondiente
        sonido_path = self.sounds_path + "/" + next(path for nombre_s, path in self.matrices_sonidos[self.matriz_actual] if nombre_s == nombre)

        # Cargar y reproducir el sonido con pygame
        try:
            pygame.mixer.music.load(sonido_path)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Error al cargar el archivo {sonido_path}.")

    def keyPressEvent(self, event):
        modifiers = event.modifiers()
        key = event.key()

        # Reproducir el sonido con Ctrl+NUM
        if modifiers == Qt.ControlModifier and Qt.Key_0 <= key <= Qt.Key_9:
            index = key - Qt.Key_0 - 1
            if 0 <= index < len(self.matrices_sonidos[self.matriz_actual]):
                nombre, _ = self.matrices_sonidos[self.matriz_actual][index]
                self.play_sound(nombre)
        # Cambiar de matriz de sonidos
        elif modifiers == Qt.AltModifier and Qt.Key_0 <= key <= Qt.Key_9:
            index = key - Qt.Key_0 - 1
            if 0 <= index < len(self.matrices_sonidos):
                self.matriz_actual = index
                self.update_buttons()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TablaSonidosApp()
    ex.show()
    sys.exit(app.exec_())
