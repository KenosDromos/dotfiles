import os
import re

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
        install_list =  packages.PACMAN["BASE"] + \
                    packages.PACMAN["ENVIRONMENTS"] + \
                    packages.PACMAN["ENVIRONMENTS_ADDITION"] + \
                    packages.PACMAN["WINDOWS_MANAGER_COMPONENTS"] + \
                    packages.PACMAN["NVIDIA_DRIVER"] 

        os.system("sudo pacman -Syy && sudo pacman -Su")
        os.system("sudo pacman -S --noconfirm " + ' '.join(install_list))
    
    @staticmethod
    def replace_config():
        file_path = ""

        config = {}
        with open(file_path, 'r') as file:
            for line in file:
                match = re.match(r'(\w+)=\((.*?)\)', line)
                if match:
                    key = match.group(1)
                    values = match.group(2).split()
                    config[key] = values

        for element in ["nvidia", "nvidia_modeset", "nvidia_uvm", "nvidia_drm"]:
            if element not in config['MODULES']:
                config['MODULES'].append(element)
        
        with open(file_path, 'w') as file:
            for key, values in config.items():
                file.write(f'{key}=({" ".join(values)})\n')

        with open("/etc/modprobe.d/nvidia.conf", "w") as file:
            file.write("options nvidia_drm modeset=1 fbdev=1\n")

    @staticmethod
    def update_pacman():
        os.system("sudo pacman -Syu")

    @staticmethod
    def aur_helper():
        os.system("git -C /tmp clone https://aur.archlinux.org/paru.git")
        os.system("cd /tmp/paru && makepkg -si")