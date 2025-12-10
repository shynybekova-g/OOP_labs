from abc import ABC, abstractmethod
class Logger(ABC):
    def header(self):
        print("=== КІТАПХАНА ЖУРНАЛЫ ===")
    @abstractmethod
    def log(self, message):
        pass
class FileLogger(Logger):
    def log(self, message):
        with open("library_log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n")
class ConsoleLogger(Logger):
    def log(self, message):
        print(message)
console_logger = ConsoleLogger()
console_logger.header()
console_logger.log("Жаңа кітап қосылды: 'Python негіздері'")
