from installer.config import Config
from installer.logger import dynamic_logger as logger
from installer.user_interface import UserInterface
from installer.builder import Assembling


class Application:
    def __init__(self):
        Config.setup()
        
    @logger
    def launch(self) -> bool:
        message = "Do you want to start the installation"
        return UserInterface.confirm_action(message)

    @logger
    def launching_interfaces(self):
        UserInterface.builder_interface()

    @logger
    def change_builder_config(self):
        builder_interface = [
            ("View config"), 
            ("Change config"),
            ("Start Building")
        ]
        message = "Do you want to change preset config"
        response = UserInterface.confirm_action(message)

        if response:
            config = Config.get_builder_config()

            for key, value in config["config_data"].items():
                message = value["prompt"]
                response = UserInterface.confirm_action(message)

                if response != value["enabled"]:
                    config["config_data"][key]["enabled"] = response
            
            Config.set_builder_config(config)

    @logger
    def run(self):
        if self.user.ready(): 
            Assembling.start()
        else: 
            print("Canceling the installation")


if __name__ == "__main__":
    app = Application()
    
    # if app.launch():
    app.launching_interfaces()

        # app.run()

