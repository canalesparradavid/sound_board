import json

class Config:
    def __init__(self, config_file):
        # Leo la configuracion del fichero
        f = open(config_file, "r")
        config_json = f.read()
        f.close()

        # Almaceno la configuracion
        config_json = json.loads(config_json)
        self.dimension = config_json['dimensions']
        self.sound_path = config_json['directory']
        self.sounds = config_json['sounds']
