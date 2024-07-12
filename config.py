from builder.actions import Action

configuration = {
    "create_folders": {
        "prompt": "Create default folders",
        "enabled": True,
        "action": lambda: Action.create_folders
    },
    "packages": {
        "prompt": "Install software packages",
        "enabled": True,
        "action": lambda: print("Installing software packages")
    },
    "dotfiles": {
        "prompt": "Install dotfiles",
        "enabled": True,
        "action": lambda: print("Installing dotfiles")
    },
    "aur_helper": {
        "prompt": "Install AUR helper (Paru)",
        "enabled": True,
        "action": lambda: print("Installing AUR helper (Paru)")
    },
    "nvidia_driver": {
        "prompt": "Install Nvidia driver",
        "enabled": True,
        "action": lambda: print("Installing Nvidia driver")
    }
}
