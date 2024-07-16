from installer.logger import LoggerConfigurator, dynamic_logger as logger
from installer.configurator import ConfigHandler
from installer.cli import UserInterface
from installer.builder import Assembling


class Application:
    def __init__(self):
        LoggerConfigurator.setup()
        self.config = ConfigHandler()
        self.config.read_json()
        # self.assembler = Assembling(self.config, self.logger)

    def run(self):
        if self.user.ready(): 
            Assembling.start()
        else: 
            print("Canceling the installation")

@logger
def main():
    pass

if __name__ == "__main__":
    app = Application()
    # app.run()
    main()
