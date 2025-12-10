from abc import ABC, abstractmethod
class StorageInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def add_item(self, item):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class LocalStorage(StorageInterface):
    def connect(self):
        print("Локал сақтау жүйесіне қосылу...")
    def add_item(self, item):
        print(f"Элемент локалды базаға сақталды: {item}")
    def disconnect(self):
        print("Локал база жабылды.")
class CloudStorage(StorageInterface):
    def connect(self):
        print("Бұлтты сақтау жүйесіне қосылу...")
    def add_item(self, item):
        print(f"Элемент бұлтты базаға жүктелді: {item}")
    def disconnect(self):
        print("Бұлтты сақтау жүйесі ажыратылды.")
if __name__ == "__main__":
    ls = LocalStorage()
    cs = CloudStorage()
    ls.connect()
    ls.add_item("Жаңа кітап")
    ls.disconnect()
    print()
    cs.connect()
    cs.add_item("Оқырман дерегі")
    cs.disconnect()
