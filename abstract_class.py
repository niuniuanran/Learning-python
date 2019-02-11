from abc import ABC, abstractmethod


class Talker(ABC):
    name = 'talker'
    @abstractmethod
    def talk(self):
        pass

    def cry(self):
        pass


class Baby(Talker):
    def talk(self):
        print("Yay yay")

    def cry(self):
        print('Waa waa')

    def eat(self):
        print(self.name, 'is eating! Yum Yum!')


def test():
    baby = Baby()
    baby.talk()
    baby.cry()


if __name__ == '__main__':
    test()
