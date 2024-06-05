class Animal:
    ZOO_NAME = "Hayaton"
    def __init__(self, name, hunger):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name;

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger):
        super().__init__(name, hunger)
        self._stink_count = 6


    def talk(self):
        print("tssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def talk(self):
        print("Good day,darling")
    def sing(self):
        print("There you go, sir!")

class Dragon(Animal):

    def __init__(self, name, hunger):
        super().__init__(name, hunger)
        self._color = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def __main__():
    zoo_lst = []
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky", 0))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))
    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    for animal in zoo_lst:
        print(f"{type(animal).__name__} {animal.get_name()}")
        while animal.is_hungry():
            animal.feed()

    for animal in zoo_lst:
        animal.talk()
        if isinstance(animal,Dog):
            animal.fetch_stick()
        elif isinstance(animal,Cat):
            animal.chase_laser()
        elif isinstance(animal,Skunk):
            animal.stink()
        elif isinstance(animal,Unicorn):
            animal.sing()
        elif isinstance(animal,Dragon):
            animal.breath_fire()

    print(animal.ZOO_NAME)


if __name__ == '__main__':
    __main__()
