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

        # Directorio de sonidos
        self.sounds_path = self.config.sound_path

        # Lista de matrices de sonidos
        self.matrices_sonidos = self.config.sounds

        # Índice de la matriz actual
        self.matriz_actual = 0

        # Array de sonidos reproduciendose
        self.sound_objects = {}

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
                    nombre, sound_path, loop = self.matrices_sonidos[self.matriz_actual][index]
                    btn = QPushButton(nombre, self)
                    btn.clicked.connect(lambda _, loop=loop, sound_path=sound_path: self.play_sound(sound_path, loop))
                    self.layout.addWidget(btn, row, col)

    def play_sound(self, nombre, loop=False):
        # Detener la reproducción del sonido si está en reproducción
        if nombre in self.sound_objects:
            self.sound_objects[nombre].stop()
            del self.sound_objects[nombre]
            return

        # Obtener la ruta del sonido correspondiente
        sonido_path = self.sounds_path + "/" + nombre

        # Cargar el sonido si aún no se ha cargado
        if nombre not in self.sound_objects:
            self.sound_objects[nombre] = pygame.mixer.Sound(sonido_path)

        # Reproducir el sonido
        try:
            self.sound_objects[nombre].play(loops=-1 if loop else 0)
        except Exception as e:
            print(f"Error al cargar el archivo {sonido_path}. {e}")

    def stop_sounds(self):
        to_delete = []
        for sound_name in self.sound_objects:
            to_delete.append(sound_name)

        for sound_name in to_delete:
            self.sound_objects[sound_name].stop()
            del self.sound_objects[sound_name]

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
                nombre, sound_path, loop = self.matrices_sonidos[self.matriz_actual][index]
                self.play_sound(sound_path, loop)
        # Cambiar de matriz de sonidos
        elif canChangematrix and Qt.Key_0 <= key <= Qt.Key_9:
            # Cambiar y bloquear cambio
            index = key - Qt.Key_0 - 1
            if 0 <= index < len(self.matrices_sonidos):
                self.matriz_actual = index
                self.update_buttons()
            canChangematrix = False
        elif Qt.Key_Escape == key:
            self.stop_sounds()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TablaSonidosApp()
    ex.show()
    sys.exit(app.exec_())
