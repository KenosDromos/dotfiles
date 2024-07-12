from builder.option import Configuration
from builder.builder import Assembling


def main():
    user = Configuration()

    if user.start():
        user.replace_config()
        params = user.get_params()
        del user

        print(params)

        # Assembling.start(params)

if __name__ == "__main__":
    main()