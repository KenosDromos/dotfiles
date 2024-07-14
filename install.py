from app.logs.logger import TaskManager

from app.configurator import ConfigHandler
from app.cli import UserInterface
from app.builder import Assembling


class Application(TaskManager, ConfigHandler, UserInterface, Assembling):
    def __init__(self):
        super().__init__()
        self.config = self.__get_config()

    def __get_config():
        return ConfigHandler()
    
    def configuration(self):
        user = Configuration()

    def run(self):
        if self.user.ready(): 
            Assembling.start()
        else: 
            print("Canceling the installation")

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()

# TODO: Вытаскиваем сюда всю логику, не прячем внутри