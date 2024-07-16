import configparser

from installer.logger import dynamic_logger as log
from installer.actions import Action

class ConfigHandler():
    def __init__(self):
        self.config = self.get_config()

    @log
    def get_config(self):
        