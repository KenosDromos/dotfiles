import os

from installer.logger import dynamic_logger as log

class Action:
    @log
    @staticmethod
    def clean_console():
        os.system("clear")

    @log
    @staticmethod
    def create_folders():
        default_folders = "~/Videos ~/Documents ~/Downloads ~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")

    @log
    @staticmethod
    def copy_bspwm_dotfiles():
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")