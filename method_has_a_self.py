class Tryclass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def have_a_self(self):
        print("My name is", self.__repr__(), end='.')
        print("I have a self!")


def i_donot(name):
    print("my name is", name, end='.')
    print("I don't have a self anymore")


def change_method():
    tryobject = Tryclass('Alice')
    tryobject.have_a_self()
    tryobject.have_a_self = i_donot
    tryobject.have_a_self('Bob')


if __name__ == '__main__':
    change_method()

