class UserInterface():
    @staticmethod
    def __is_valid(text) -> bool:
        if "y" in text.lower():
            return True
        else:
            return False
        
    @staticmethod
    def get_params() -> list:
        print("Do you want to install? [Y/n]: ", end="")
        option_1 = UserInterface.__is_valid(input())

        return [option_1]
