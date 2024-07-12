import os

from builder.logger import Logger, LoggerStatus

class SystemBuild:
    @staticmethod
    def start(*args):
        start_text = f"[+] Starting assembly. Options {args}"
        Logger.add_record(start_text, status=LoggerStatus.SUCCESS)

        if args[0]: 
            SystemBuild.__building()

            end_text = f"[+] Installation Completed Successfully"
            Logger.add_record(end_text, status=LoggerStatus.SUCCESS)
        else:
            end_text =  f"[+] Installation Canceled"
            Logger.add_record(end_text, status=LoggerStatus.ERROR)
        

    @staticmethod
    def building():
        SystemBuild.create_default_foleders()


    @staticmethod
    def create_default_foleders():
        Logger.add_record("[+] Create default directories", status=LoggerStatus.SUCCESS)
        default_folders = "~/Videos ~/Documents ~/Downloads " + \
                          "~/Music ~/Desktop"
        os.system("mkdir -p ~/.config")
        os.system(f"mkdir -p {default_folders}")

    @staticmethod
    def copy_bspwm_dotfiles():
        Logger.add_record("[+] Copy Dotfiles & GTK", status=LoggerStatus.SUCCESS)
        os.system("cp -r config/* ~/.config/")
        os.system("cp Xresources ~/.Xresources")
        os.system("cp gtkrc-2.0 ~/.gtkrc-2.0")
        os.system("cp -r local ~/.local")
        os.system("cp -r themes ~/.themes")
        os.system("cp xinitrc ~/.xinitrc")
        os.system("cp -r bin/ ~/")