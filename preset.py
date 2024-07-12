from enum import Enum

class Param:
    def __init__(self, prompt: str, enable: bool):
        self.prompt = prompt
        self.enable = enable   
    
class Configuration(Enum):
    START_INSTALL = Param("Do you want to install", True)
    DOTFILES = Param("Do you want to install Dotfiles", True)
    AUR_HELPER = Param("Install AUR helper Paru", True)
    NVIDIA_DRIVER = Param("Do you want to Nvidia driver", True)