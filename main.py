import sys
import platform

argv = sys.argv
system = platform.system()

if system == "Windows":
    from main_gui import start_board
elif system == "Linux" and "--no-gui" in argv:
    from main_lnx_no_gui import start_board
elif system == "Linux":
    from main_gui import start_board
else:
    print("Estás en un sistema operativo no compatible.")
    exit()

start_board()
