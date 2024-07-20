from typing import Callable, Optional, List, Tuple, Dict, Any

from installer.logger import dynamic_logger as logger


# ______________________________________________________________________ Class UserAction
class UserAction:
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
    def get_user_choice(items: List[Any]) -> Any:
        """
        Get the user's choice from the list of items

        :param items: Items in the list
        :return: Selected item (Any)
        """
        num_items = len(items)

        while True:
            print("Enter the item number: ", end="")
            user_input = input()

            if user_input.isdigit():
                user_input = int(user_input) - 1

                if user_input >= 0 and user_input < num_items:
                    return items[user_input]
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