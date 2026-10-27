from abc import ABC, abstractmethod


# ABC - abstract base class
class RBI(ABC):
    # decorator
    @abstractmethod
    def HL(self):
        pass

    def sa(self):
        pass


class SBI(RBI):
    def HL(self):
        print("sbi hl 7%")

    def sa(self):
        print("sa 3.5%")


s = SBI()
s.HL()
s.sa()
