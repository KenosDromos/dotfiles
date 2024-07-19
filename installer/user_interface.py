from installer.logger import dynamic_logger as logger
from installer.config import Config

class UserInterface:
    @logger
    @staticmethod
    def display_items(items: list) -> None:
        """
        Display a list of items to the user

        :param items: List of items to display
        """
        for index, text in enumerate(items):
            print(f"{index + 1}) {text}")
    
    @logger
    @staticmethod
    def get_user_choice(num_items: int) -> int:
        """
        Get the user's choice from the list of items

        :param num_items: The number of items in the list
        :return: The number of the chosen item (int)
        """
        while True:
            print("Enter the item number: ", end="")
            user_input = input()

            if user_input.isdigit():
                user_input = int(user_input) - 1

                if user_input >= 0 and user_input < num_items:
                    return user_input
                else:
                    print(f"Number out of range. Please enter a number between 1 and {num_items}.")
            else:
                print("Please enter a valid number.")


    @logger
    @staticmethod
    def confirm_action(message: str) -> bool:
        """ 
        User's request for action agreements in the form of [Y/n]
        
        message: Notifying the user about the decision

        :return: bool
        """
        while True:
            print(f"{message} [Y/n]: ", end="")
            user_input = input().lower()

            if user_input in "yn":
                return user_input == 'y'
            else:
                print(f"Incorrect data entry [{user_input}]")
    
    @logger
    @staticmethod
    def builder_interface():
        manager = UserInterface.BuilderInterface()
        manager.load_interface()

    class BuilderInterface:
        @logger
        def __init__(self):
            self._exit = False
            self._interface = (
                ("Exit", self.exit),
                ("View config", self.view_config), 
                ("Change config", self.change_config),
                ("Start Building", self.start)
            )
            self._count_items = len(self._interface)
            self._interface_items = [i[0] for i in self._interface]
            self._interface_funcs = [i[1] for i in self._interface]
            self._config = Config.get_builder_config()
        
        @logger
        def load_interface(self):
            while not self._exit:
                self._display_interface()
                choice = self._get_user_choice()
                self._execute_choice(choice)

        @logger
        def _display_interface(self):
            UserInterface.display_items(self._interface_items)

        @logger
        def _get_user_choice(self) -> int:
            return UserInterface.get_user_choice(self._count_items)

        @logger
        def _execute_choice(self, choise: int):
            action = self._interface_funcs[choise]
            action()

        @logger
        def view_config(self):
            for key, value in self._config.items():
                prompt = value["prompt"]
                symbol = 'Y' if value["enabled"] else 'N'
                option = f"{prompt} [{symbol}]"

                print(option)
                
        @logger
        def change_config(self):
            for key, value in self._config.items():
                prompt = value["prompt"]
                response = UserInterface.confirm_action(prompt)

                value["enabled"] = response
            
            Config.set_builder_config(self._config)

        @logger
        def start(self):
            pass

        @logger
        def exit(self):
            self._exit = True
    