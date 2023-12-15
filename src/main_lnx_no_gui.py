import curses
import pygame

from config import Config
from board import Board

config = None
board = None

def run(stdscr):
    # Inicializar la ventana de curses
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Mostrar instrucciones
    # stdscr.addstr(0, 0, "Presiona las teclas de 1 a {} para reproducir sonidos.".format(len(sounds)))
    stdscr.refresh()

    while True:
        # Obtener la tecla presionada
        key = stdscr.getch()

        # Activar cambio de matriz
        if key == ord('a'):
            board.switch_change_option()
        # Parar todos los sonidos
        elif key == ord('b'):
            board.stop_all()
        # Reproducir sonido
        elif not board.can_change_matrix and ord('c') <= key <= ord('c') + config.dimension[0] * config.dimension[1]:
            board.play_sound(key - ord('c'))
        # Cambiar de matriz
        elif board.can_change_matrix and ord('c') <= key <= ord('c') + len(config.sounds):
            board.change_to_matrix(key - ord('c'))
        # Cambiar de LED
        elif ord('x') <= key <= ord('z'):
            board.change_led(key - ord('x'))

def start_board():
    global config
    global board

    # Inicializar pygame
    pygame.init()

    # Inicializo el programa
    config = Config("config.json", pygame)
    board = Board(config)
    config.boot_sound.play()

    # Arranco el programa
    curses.wrapper(run)

if __name__ == "__main__":
    start_board()
