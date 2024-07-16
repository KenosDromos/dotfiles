import time

from installer.actions import Action
from installer.logger import dynamic_logger as log

class UserInterface():
    def __init__(self) -> None:
        pass

    def print():
        pass

    def request(push: str) -> bool:
        """ 
        Find symbol
        
        push: Notification to the user about the decision [Y/n]

        Return y, n or 0
        """
        is_valid = lambda text: 'y' if "y" in text.lower() else 'n' if  "n" in text.lower() else '0' 

        while True:
            print(f"{push} [Y/n]: ", end="")
            user_input = is_valid(input())

            if 'y' == user_input:
                return True
            if 'n' == user_input:
                return False
            if '0' == user_input: 
                print(f"Incorrect data entry [{user_input}]")
    
    def __start_install(self):
        notice = "Do you want to start the installation"
        response = UserInterface.request(notice)

        return response
    
    def __start_config(self):
        notice = "Do you want to change preset config"
        self.user_approved_config_change = UserInterface.request(notice)
