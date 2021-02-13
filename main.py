class LivingThing:
    def __init__(self, habitat):
        self.habitat = habitat

    def habitat(self):
        return "I live in" + self.habitat


class Animal:
    def __init__(self, type, location, habitat, is_carnivore):
        super(Animal, self).__init__(habitat)
        self.type = type
        self.location = location
        self.is_carnivore = is_carnivore


class Person:
    def __init__(self, name, age, location, type, habitat, is_carnivore):
        super(Person, self).__init__(type, location, habitat, is_carnivore)
        self.name = name
        self.age = age
        self.is_carnivore = False


class Wolf:
    def __init__(self, pack_leader, type, location, habitat, is_carnivore):
        super(Wolf, self).__init__(location, type, habitat, is_carnivore)
        self.pack_leader = pack_leader
        self.is_carnivore = True


class Caribou:
    def __init__(self, type, location, habitat, is_carnivore):
        super(Caribou, self).__init__(type, location, habitat, is_carnivore)
        self.is_carnivore = False

class Plant:
    def __init__(self, habitat, uses_sun):
        super(Plant, self).__init__(habitat)
        self.uses_sun = uses_sun

class Flower:
    def __init__(self, habitat, uses_sun, colour):
        super(Flower, self).__init__(habitat, uses_sun)
        self.colour = colour


class Dandelion:
    def __init__(self, habitat, uses_sun, colour):
        super(Dandelion, self).__init__(habitat, uses_sun, colour)


class Rose:
    def __init__(self, habitat, uses_sun, colour):
        super(Rose, self).__init__(habitat, uses_sun, colour)


class Tree:
    def __init__(self, habitat, uses_sun, branches):
        super(Tree, self).__init__(habitat, uses_sun)
        self.branches = branches
        
class Maple:
    def __init__(self, habitat, uses_sun, branches):
        super(Maple, self).__init__(habitat, uses_sun, branches)
