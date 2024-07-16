import logging
from functools import wraps
from sys import exit as EXIT
from datetime import datetime


class LoggerConfigurator:
    log_dir = "installer/logs/"
    log_file_name = "install_"
    log_full_path = None

    @staticmethod
    def setup():
        """Configuring the configuration for logs"""
        if LoggerConfigurator.log_full_path is None:
            LoggerConfigurator.log_file_name = LoggerConfigurator.__get_unique_log_file_name()
            LoggerConfigurator.log_full_path = LoggerConfigurator.log_dir + LoggerConfigurator.log_file_name
            formatter = '%(asctime)s | %(name)s - %(levelname)s | %(message)s'
            logging.basicConfig(filename=LoggerConfigurator.log_full_path, encoding='utf-8', level=logging.DEBUG, format=formatter)

    @staticmethod
    def __get_unique_log_file_name() -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = f"{LoggerConfigurator.log_file_name}{timestamp}.log"
        
        return log_file


class Logger:
    logger: logging.Logger

    @staticmethod
    def get_logger(logname: str):
        Logger.logger = logging.getLogger(logname)
    
    @staticmethod
    def info(message: str):
        print(message)
        Logger.logger.info(message)

    @staticmethod
    def critical(message: str, exit_program: bool = True):
        print(message)
        Logger.logger.critical(message)

        if exit_program:
            print("Program will terminate due to a critical error.")
            print(f"See the details in the file [{LoggerConfigurator.log_full_path}]")

            EXIT(1)


@staticmethod
def dynamic_logger(func = None, *, message: str = ""):
    if func is None: 
        return lambda f: dynamic_logger(f, message=message)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # START Block naming
        func_name = func.__name__
        class_name = func.__qualname__.split('.')[0] if '.' in func.__qualname__ else None

        if class_name:
            logger_name = f"{class_name}"
        else:
            logger_name = f"Global"
        # END Block naming

        # Return a logger with the specified name, creating it if necessary.
        Logger.get_logger(logger_name)

        # START
        Logger.info(f"Calling {func_name}. {message}")

        result = func(*args, **kwargs)

        # END
        Logger.info(f"{func_name} completed.")

        return result

    return wrapper