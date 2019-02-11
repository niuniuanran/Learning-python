from classes_objects.abstract_class import Baby, Talker


class TalkativeBaby(Baby):
    def talk(self):
        print('Talky talk!')

    def chat(self):
        print('Chatty chat')


def test():
    baby = TalkativeBaby()
    baby.talk()
    baby.cry()
    baby.chat()
    baby.name = 'Ruby'
    baby.eat()
    print(isinstance(baby, Talker))


if __name__ == '__main__':
    test()
