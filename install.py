from app.option import Configuration
from app.builder import Assembling


class Application:
    __to_begin = False

    def configuration(self):
        user = Configuration()

    def run(self):
        if self.user.ready(): 
            Assembling.start()
        else: 
            print("Canceling the installation")

def main():
    app = Application()
    app.run()

if __name__ == "__main__":
    main()