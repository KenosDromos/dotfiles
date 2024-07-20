from typing import Callable, Optional, List, Tuple, Dict, Any

from installer.logger import Logger, dynamic_logger as logger
from installer.config import Config
from installer.action import BuilderAction

# ______________________________________________________________________ Class Assembling
class Assembling():
    _builder_options: Dict[str, Dict[str, Any]]

    @logger
    @staticmethod
    def setup():
        Assembling._builder_options = Config.get_builder_config()

    @logger
    @staticmethod
    def start():
        BuilderAction.clean_console()
        Assembling._building()

    @logger
    @staticmethod
    def _building():
        logger = Logger.get_logger("_building")
        
        for option in Assembling._builder_options:
            

    @logger
    @staticmethod
    def _procesor(exit_program: bool = True):
        pass
    

        if exit_program:
                print("Program will terminate due to a critical error.")
                print(f"See the details in the file [???]")
                exit()