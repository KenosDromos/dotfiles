import os
import time
from builder.logger import Logger

class Action:
    @staticmethod
    def clean_console(timeout: float = 0):
        time.sleep(timeout)
        os.system("clear")

    @staticmethod
    def create_folders():
        default_folders = "~/Videos ~/Documents ~/Downloads ~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")

    @staticmethod
    def copy_bspwm_dotfiles():
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")