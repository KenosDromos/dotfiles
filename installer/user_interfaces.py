from dataclasses import dataclass
from typing import Callable, Optional, List, Tuple, Dict, Any

from installer.logger import dynamic_logger as logger
from installer.config import Config
from installer.user_action import UserAction


# ______________________________________________________________________ Dataclass Button
@dataclass
class Button:
    name: str
    title: str
    action: Callable[[], None]


# ______________________________________________________________________ Class BlockButtons
class BlockButtons:
    def __init__(self):
        self._buttons: Dict[str, Button] = {}
        self._num_buttons = 0

    @logger
    def get_buttons(self) -> Dict[str, Button]:
        return self._buttons
    
    @logger
    def get_button(self, btn_name: str) -> Button:
        if self.check_button(btn_name):
            return self._buttons[btn_name]
        raise ValueError(f"No button found with the name '{btn_name}'")
    
    def get_button_attributes(self, attr: str) -> List[Any]:
        return [getattr(button, attr) for button in self._buttons.values()]
    
    @logger
    def set_button(self, btn_name: str, new_btn: Button):
        if self.check_button(btn_name):
            self._buttons[btn_name] = new_btn
        else:
            raise ValueError(f"No button found with the name '{btn_name}'")

    @logger
    def add_button(self, btn: Button) -> None:
        if not isinstance(btn, Button):
            raise ValueError("The provided object is not of type Button")
        if self.check_button(btn.name):
            raise ValueError(f"A button with the name '{btn.name}' already exists")
        self._buttons[btn.name] = btn
        self._num_buttons += 1

    @logger
    def action_button(self, btn_name: str):
        if self.check_button(btn_name):
            self.get_button(btn_name).action()
        else:
            raise ValueError(f"No button found with the name '{btn_name}'")

    @logger
    def remove_button(self, btn_name: str) -> None:
        if self.check_button(btn_name):
            del self._buttons[btn_name]
            self._num_buttons -= 1
        else:
            raise ValueError(f"No button found with the name '{btn_name}'")

    @logger
    def check_button(self, btn_name: str) -> bool:
        return btn_name in self._buttons
    
    @logger
    def get_num_button(self):
        return self._num_buttons



# ______________________________________________________________________ Class BuilderInterface
class BuilderInterface:
    def __init__(self):
        self._interface = BlockButtons()
        self._interface.add_button(Button("exit", "Exit", self.exit))
        self._interface.add_button(Button("view_config", "View Config", self.view_config))
        self._interface.add_button(Button("change_config", "Change Config", self.change_config))
        self._interface.add_button(Button("start", "Start", self.start))

        self._config = Config.get_builder_config()
        self._start = False

    @logger
    def load_interface(self):
        while not self._start:
            items = self._interface.get_button_attributes("title")
            UserAction.display_items(items)

            buttons_name = self._interface.get_button_attributes("name")
            btn_name = UserAction.get_user_choice(buttons_name)
            
            print("\n")

            self._interface.action_button(btn_name)

            print("\n" * 2)

    @logger
    def view_config(self):
        for key, value in self._config.items():
            prompt = value["prompt"]
            symbol = 'Y' if value["enabled"] else 'N'
            option = f"{prompt} [{symbol}]"

            print(option)
            
    @logger
    def change_config(self):
        for key, value in self._config.items():
            prompt = value["prompt"]
            response = UserAction.confirm_action(prompt)

            value["enabled"] = response
        
        Config.set_builder_config(self._config)

    @logger
    def start(self):
        self._start = True

    @logger
    def exit(self):
        print("Canceling the installation")
        exit()
