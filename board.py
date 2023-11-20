class Board:
    def __init__(self, config):
        self.config = config
        self.actual_matrix = 0
        self.can_change_matrix = False

    def play_sound(self, index):
        if not self.can_change_matrix and 0 <= index < len(self.config.sounds[self.actual_matrix]):
            sound = self.config.sounds[self.actual_matrix][index]
            sound.switch_sound()

    def switch_change_option(self):
        self.can_change_matrix = not self.can_change_matrix

    def change_to_matrix(self, index):
        if self.can_change_matrix and 0 <= index <= len(self.config.sounds):
            self.actual_matrix = index
        self.can_change_matrix = False

    def stop_all(self):
        for matrix in self.config.sounds:
            for sound in matrix:
                sound.stop()
        self.can_change_matrix = False

    def change_led(self, index):
        print("cambiando led: ", index)
        self.can_change_matrix = False
