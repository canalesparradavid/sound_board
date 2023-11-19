import pygame

class Sound:
    def __init__(self, name, sound_path, loop=False):
        self.sound_instance = None
        self.name = name
        self.sound_path = sound_path
        self.loop = loop

    # Handler del sonido
    def switch_sound(self, pygame):
        if self.sound_instance == None:
            self.play(pygame)
        else:
            self.stop()

    # Repoduce el sonido
    def play(self, pygame):
        try:
            sound = pygame.mixer.Sound(self.sound_path)
            sound.play(loops=-1 if self.loop else 0)
            self.sound_instance =  sound
        except Exception as e:
            print(f"Error al cargar el archivo {self.sound_path}. {e}")

    # Para el sonido
    def stop(self):
        if(self.sound_instance is not None):
            self.sound_instance.stop()
        self.sound_instance =  None
