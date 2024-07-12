from time import ctime


class Logger:
    filename = "build.log"
    
    @staticmethod
    def add_record(text: str) -> None:
        text = f"{ctime()} | {text} \n"
        print(text, end='')

        with open(Logger.filename, "a", encoding="UTF-8") as file:
            file.write(text)