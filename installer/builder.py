import logging
from typing import Callable, Optional, List, Tuple, Dict, Any

from installer.logger import Logger, dynamic_logger as logger
from installer.config import Config
from installer.action import BuilderAction

# ______________________________________________________________________ Class Assembling
class Assembling():
    _logger: logging.Logger
    _builder_options: Dict[str, Dict[str, Any]]
    _log_file_path: str

    @logger
    @staticmethod
    def setup():
        Assembling._logger = Logger.get_logger("Assembling")
        Assembling._builder_options = Config.get_builder_config()
        Assembling._log_file_path = Config.get_logger_config()["log_file_path"]

        Assembling._del_disabled_options()
        # Assembling._valid_options()
        

    @logger
    @staticmethod
    def start():
        # BuilderAction.clean_console()
        Assembling._building()

    @logger
    @staticmethod
    def _building():
        for option, value in Assembling._builder_options.items():
            prompt = value["prompt"]
            message = f"[Builder] {prompt}"

            Assembling._info_message(message)
            Assembling._procesor(option)

    @logger
    @staticmethod
    def _procesor(func_name: str):
        action = getattr(BuilderAction, func_name)

        try:
            action()
        except Exception as error:
            Assembling._critical_message(error)
    
    @logger
    @staticmethod
    def _valid_options():
        for option, value in Assembling._builder_options.items():
            if not hasattr(BuilderAction, option):
                message = f"The config parameter is not valid [{option}]"
                Assembling._critical_message(message)
    
    @logger
    @staticmethod
    def _del_disabled_options():
        delete_options = []

        for option, value in Assembling._builder_options.items():
            enabled = value["enabled"]

            if not enabled:
                delete_options.append(option)
        
        for option in delete_options:
            del Assembling._builder_options[option]

    @logger
    @staticmethod
    def _info_message(message: str):
        Assembling._logger.info(message)
        print(f"{message}", end="\n" * 2)

    @logger
    @staticmethod
    def _critical_message(message: str):
        Assembling._logger.critical(message)
        print(f"{message}", end="\n" * 2)

        print("Program will terminate due to a critical error.")
        print(f"See the details in the file [{Assembling._log_file_path}]")
        exit()