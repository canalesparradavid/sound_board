import pygame

class Sound:
    def __init__(self, pygame, name, sound_path, loop=False):
        self.sound_instance = False
        self.name = name
        self.loop = loop
        self.sound = None

        try:
            self.sound = pygame.mixer.Sound(sound_path)
        except Exception as e:
            print(f"Error al cargar el archivo {sound_path}. {e}")

    # Handler del sonido
    def switch_sound(self):
        if not self.sound_instance:
            self.play()
        else:
            self.stop()

    # Repoduce el sonido
    def play(self):
        try:
            self.sound.play(loops=-1 if self.loop else 0)
            self.sound_instance =  True
        except Exception as e:
            print(f"No se pudo reproducir el archivo. {e}")

    # Para el sonido
    def stop(self):
        if(self.sound_instance):
            self.sound.stop()
        self.sound_instance =  False
