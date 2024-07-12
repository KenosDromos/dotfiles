from builder.actions import Action
from config import configuration


class UserInterface:
    @staticmethod
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


class Configuration:
    user_approved_config_change = True

    def __init__(self) -> None:
       Action.clean_console()

    def __del__(self) -> None:
        Action.clean_console(3)

    def start(self) -> bool:
        notice = "Do you want to start the installation"
        response = UserInterface.request(notice)
        
        if not response:
            print("Canceling the installation")

        return response

    def replace_config(self):
        notice = "Do you want to change preset config"
        self.user_approved_config_change = UserInterface.request(notice)

    def get_params(self) -> dict:
        params = configuration
        
        if self.user_approved_config_change:
            for index, item in enumerate(params):
                notice = f"{index + 1}) {configuration[item]["prompt"]}"
                response = UserInterface.request(notice)
                configuration[item]["enabled"] = response
        else:
            print("The file configuration will be used [config.py]")
        
        return params