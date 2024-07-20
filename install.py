from installer.config import Config
from installer.logger import dynamic_logger as logger
from installer.user_interfaces import UserAction, BuilderInterface
from installer.builder import Assembling


# ______________________________________________________________________ Class Application
class Application:
    def __init__(self):
        Config.setup()
        
    @logger
    def launch(self) -> bool:
        message = "Do you want to start the installation"
        return UserAction.confirm_action(message)

    @logger 
    def manager_interface(self):
        manager = BuilderInterface()
        manager.load_interface()

    @logger
    def run(self):
        Assembling.setup()
        Assembling.start()


if __name__ == "__main__":
    app = Application()
    
    # if app.launch():
    # app.manager_interface()
    app.run()

