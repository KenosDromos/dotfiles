from installer.logger import dynamic_logger as logger

class UserInterface:
    @logger
    @staticmethod
    def listing(items: list) -> int:
        """
        Displaying a list of items to the user

        :return: the number of the list item (int)
        """
        for index, text in enumerate(items):
            print(f"{index + 1}) {text}")
        
        while True:
            print("Enter the item number: ", end="")
            user_input = input()

            if user_input.isdigit():
                user_input -= 1

                if user_input <= len(items):
                    return user_input
                else:
                    print(f"Number out of range. Please enter a number between 1 and {len(items)}.")
            else:
                print("Please enter a valid number.")


    @logger
    @staticmethod
    def request(message: str) -> bool:
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
    