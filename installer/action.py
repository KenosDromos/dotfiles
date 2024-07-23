import os


import packages


# ______________________________________________________________________ Class BulderAction
class BuilderAction:
    @staticmethod
    def clean_console():
        os.system("clear")

    @staticmethod
    def action(action: str):
        BuilderAction.action()

    @staticmethod
    def create_folders():
        default_folders = "~/Videos ~/Documents ~/Downloads ~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")

    @staticmethod
    def packages():
        pass
    
    @staticmethod
    def copy_dotfiles():
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")

    @staticmethod
    def packages():
        install_list = packages.PACMAN
    
    @staticmethod
    def update_pacman():
        os.system("sudo pacman -Syu")

    @staticmethod
    def aur_helper():
        os.system("git -C /tmp clone https://aur.archlinux.org/paru.git")
        os.system("cd /tmp/paru && makepkg -si")