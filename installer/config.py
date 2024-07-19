import json
import logging
from datetime import datetime
from typing import Optional

class Config:
    """
    Static class for managing configuration settings.
    """
    
    _is_setup = False

    _logger: Optional['Config.LoggerConfigurator'] = None
    _builder: Optional['Config.BuilderConfigurator'] = None

    @staticmethod
    def setup() -> None:
        """
        Initialize the configuration by setting up logger and builder configurations.
        """
        if not Config._is_setup:
            Config._logger = Config.LoggerConfigurator()
            Config._builder = Config.BuilderConfigurator()

            Config._is_setup = True

    @staticmethod
    def get_logger_config() -> dict:
        """
        Get the logger configuration.

        :return: Dictionary with logger configuration.
        """
        Config._check_setup()
        return Config._logger.get_config()

    @staticmethod
    def get_builder_config() -> dict:
        """
        Get the builder configuration.

        :return: Dictionary with builder configuration.
        """
        Config._check_setup()
        return Config._builder.get_config()

    @staticmethod
    def set_builder_config(config: dict) -> None:
        """
        Set the logger configuration.
        """
        Config._check_setup()
        Config._builder.set_config(config)

    @staticmethod
    def _check_setup():
        """
        Checks whether its configuration has been configured

        Raises:
            RuntimeError: If the config has not been set up.
        """
        if not Config._is_setup:
            raise RuntimeError("Config.setup() must be called before any other method.")
        
    class LoggerConfigurator:
        """
        Class for configuring and managing logger settings.
        """
        
        def __init__(self) -> None:
            """
            Initialize LoggerConfigurator with default parameters.
            """
            self._log_dir = "installer/logs/"
            self._filename_prefix = "install_"
            self._filename = None
            self._file_path = None

            self._set_params()
            self._configure_logging()

        def _set_params(self) -> None:
            """
            Set parameters for log filename and file path.
            """
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self._filename = f"{self._filename_prefix}{timestamp}.log"
            self._file_path = self._log_dir + self._filename

        def _configure_logging(self) -> None:
            """
            Configure logging settings including format and file handler.
            """
            formatter = '%(asctime)s | %(name)s - %(levelname)s | %(message)s'
            logging.basicConfig(filename=self._file_path, encoding='utf-8', level=logging.DEBUG, format=formatter)

        def get_config(self) -> dict:
            """
            Get the current logger configuration.

            :return: Dictionary with logger configuration.
            """
            return {
                "log_dir": self._log_dir,
                "log_filename": self._filename,
                "log_file_path": self._file_path
            }

    class BuilderConfigurator:
        """
        Class for loading and storing configuration data from a JSON file.
        """
        
        def __init__(self, config_path: str = "config.json") -> None:
            """
            Initialize BuilderConfigurator with the specified path to the configuration file.

            :param config_path: Path to the configuration file.
            """
            self._config_path = config_path
            self._config_data = self._read_config_file()

        def _read_config_file(self) -> dict:
            """
            Read configuration data from the JSON file.

            :return: Content of the configuration file as a dictionary.
            """
            with open(self._config_path, 'r', encoding="utf-8") as file:
                return json.load(file)
            
        def _write_config_file(self, config: dict) -> None:
            """
            Write configuration data from the JSON file.
            """
            with open(self._config_path, 'w', encoding="utf-8") as file:
                json.dump(config, file, indent = 4)
            
        def get_config(self) -> dict:
            """
            Get the current configuration data.

            :return: Dictionary with configuration data.
            """
            return {
                "config_path": self._config_path,
                "config_data": self._config_data
            }
        
        def set_config(self, config: dict) -> None:
            """
            Set the current configuration data.
            """
            self._write_config_file(config["config_data"])
            self._config_data = config