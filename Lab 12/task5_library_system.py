from abc import ABC, abstractmethod
class MembershipSystem(ABC):
    @abstractmethod
    def authorize(self):
        pass
    @abstractmethod
    def pay(self):
        pass
    @abstractmethod
    def cancel(self):
        pass
class StudentMembership(MembershipSystem):
    def authorize(self):
        print("Студент абонементі тексерілді.")
    def pay(self):
        print("Студенттік тариф бойынша төлем жасалды.")
    def cancel(self):
        print("Студент абонементі тоқтатылды.")
class PremiumMembership(MembershipSystem):
    def authorize(self):
        print("Premium абонементі тексерілді.")
    def pay(self):
        print("Premium төлем өңделді.")
    def cancel(self):
        print("Premium абонементі тоқтатылды.")
class DailyPass(MembershipSystem):
    def authorize(self):
        print("Бір күндік рұқсат белсендірілді.")
    def pay(self):
        print("Күндік төлем қабылданды.")
    def cancel(self):
        print("Күндік рұқсат өшірілді.")
if __name__ == "__main__":
    systems = [StudentMembership(), PremiumMembership(), DailyPass()]
    for s in systems:
        s.authorize()
        s.pay()
        s.cancel()
        print()
