import logging
from functools import wraps


# ______________________________________________________________________ Class Logger
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
    def debug(message: str):
        Logger.logger.debug(message)

    @staticmethod
    def critical(message: str):
        print(message)
        Logger.logger.critical(message)


# ______________________________________________________________________ Function dynamic_logger
def dynamic_logger(func = None):
    if func is None: 
        return lambda f: dynamic_logger(f)

    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        class_name = func.__qualname__.split('.')[0] if '.' in func.__qualname__ else None
        logger_name = f"{class_name}" if class_name else f"Global"

        # Return a logger with the specified name, creating it if necessary.
        Logger.get_logger(logger_name)

        # START
        Logger.debug(f"Calling {func_name}.")

        result = func(*args, **kwargs)

        # END
        Logger.debug(f"{func_name} completed.")

        return result
    return wrapper