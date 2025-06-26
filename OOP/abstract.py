from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abs_method(self):
       pass

    def __init__(self, surname):
        self.surname = surname

class Child(AbstractClass):
    def __init__(self):
        super().__init__("Pandey")

    def abs_method(self):
        print("this is implementation to abs Method")

ch = Child()
ch.abs_method()
print(ch.surname)