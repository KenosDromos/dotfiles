import os
from builder.option import UserInterface
from builder.builder import SystemBuild


def main():
    params = UserInterface.get_params()
    SystemBuild.start(params)

           
if __name__ == "__main__":
    os.system("clear")
    main()