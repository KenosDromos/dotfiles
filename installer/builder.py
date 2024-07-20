from sys import exit as EXIT

from installer.logger import dynamic_logger as log
from installer.config import Config


# ______________________________________________________________________ Class Assembling
class Assembling():
    def start(params: dict):
        pass

        if params: 
            Assembling.building()

            end_text = f"Installation Completed Successfully"
        else:
            end_text =  f"Installation Canceled"

    def procesor(exit_program: bool = True):
        pass
    

        if exit_program:
                print("Program will terminate due to a critical error.")
                print(f"See the details in the file [???]")

                EXIT(1)

    def building():
        pass
        # SystemBuild.create_default_foleders()
        # "Create default directories"
