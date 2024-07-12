import os

from builder.logger import Logger


class SystemBuild:
    @staticmethod
    def start(params: dict):
        Logger.add_record(f"Starting assembly. Options {params}")

        if params: 
            SystemBuild.building()

            end_text = f"Installation Completed Successfully"
            Logger.add_record(end_text)
        else:
            end_text =  f"Installation Canceled"
            Logger.add_record(end_text)
        

    @staticmethod
    def building():
        # SystemBuild.create_default_foleders()
        pass

    @staticmethod
    def create_default_foleders():
        Logger.add_record("Create default directories")

        default_folders = "~/Videos ~/Documents ~/Downloads ~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")

    @staticmethod
    def copy_bspwm_dotfiles():
        Logger.add_record("Copy Dotfiles & GTK")

        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")