import sys
from datetime import datetime

import logging


class Logger:
    def __init__(self):
        self.log_file = self.__get_unique_log_file()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def __get_unique_log_file(self) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = f"logfile_{timestamp}.log"
        
        return log_file
    
    def log_action(self, action: str):
        message = f"Starting action: {action}"
        self.logger.info(message)
        print(message)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)
        print(message)

    def critical(self, message: str, exit_program: bool = True):
        self.logger.critical(message)
        print(message)
        if exit_program:
            self.logger.critical("Program will terminate due to a critical error.")
            print("Program will terminate due to a critical error.")
            sys.exit(1)

class TaskManager(Logger):
    def __init__(self):
        super().__init__()