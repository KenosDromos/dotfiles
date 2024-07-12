from preset import Configuration

class UserInterface():
    @staticmethod
    def __is_valid(text) -> bool:
        return "y" in text.lower()
        
    @staticmethod
    def get_params() -> Configuration:
        print("Do you want to change preset config [Y/n]: ", end="")
        
        if UserInterface.__is_valid(input()):
            for index, option in enumerate(Configuration):
                print(f"{index + 1}) {option.value.prompt} [Y/n]: ", end="")

                option.value.enable = UserInterface.__is_valid(input())

        return Configuration
