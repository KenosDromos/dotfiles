from installer.action import BuilderAction

def test():
    BuilderAction.create_folders()
    BuilderAction.update_pacman()
    BuilderAction.packages()
    BuilderAction.replace_config()