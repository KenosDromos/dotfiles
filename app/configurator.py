
class ConfigHandler:
    PATH_FILE_CONFIG = "config.json"

    def __init__(self):
        Action.clean_console()

        self.__start_install()
        
        if self.__to_begin:
            configur = self.__start_config()


    def __del__(self):
        time.sleep(3)
        Action.clean_console()

    def __start_install(self):
        notice = "Do you want to start the installation"
        response = UserInterface.request(notice)

        return response
    
    def __start_config(self):
        notice = "Do you want to change preset config"
        self.user_approved_config_change = UserInterface.request(notice)

    def __get_params(self) -> dict:
        params = configuration
        
        if self.user_approved_config_change:
            for index, item in enumerate(params):
                notice = f"{index + 1}) {configuration[item]["prompt"]}"
                response = UserInterface.request(notice)
                configuration[item]["enabled"] = response
        else:
            print("The file configuration will be used [config.py]")
        
        return params
    
    def ready(self) -> bool:
        return self.__to_begin