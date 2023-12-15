import os
import json
from sound import Sound

class Config:
    def __init__(self, config_file, pygame):
        # Leo la configuracion del fichero
        self.directorio_script = os.path.dirname(os.path.abspath(__file__))
        f = open(self.directorio_script + "/" + config_file, "r")
        config_json = f.read()
        f.close()

        # Almaceno la configuracion
        config_json = json.loads(config_json)
        self.dimension = config_json['dimensions']
        self.sound_path = config_json['directory']
        self.sounds = self.create_sounds(pygame, config_json['sounds'])
        self.boot_sound = Sound(pygame, '', self.directorio_script + "/" + self.sound_path + "/" + config_json['boot_sound'])

    def create_sounds(self, pygame, sound_matrix):
        all_sounds = []

        # Recorro las matrices
        for i in range(len(sound_matrix)):
            matrix_sounds = []
            # Recorro sonidos de la matriz actual
            for j in range(len(sound_matrix[i])):
                s = sound_matrix[i][j]
                matrix_sounds.append(Sound(pygame,                                  \
                    s[0],                                                           \
                    self.directorio_script + "/" + self.sound_path + "/" + s[1],    \
                    s[2] if len(s) == 3 else False                                  \
                ))
            all_sounds.append(matrix_sounds)

        return all_sounds
