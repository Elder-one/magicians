from abc import ABC, abstractmethod


class Entity(ABC):

    __counter = 0

    def __init__(self, max_hp: int, max_energy: int,
                 damage: int, healing: int, name: str):
        self.__healing = healing
        self.__damage = damage
        self.__name = name
        self.__alive = True
        self.__max_hp = max_hp
        self.__max_energy = max_energy
        self.__hp = max_hp
        self.__energy = max_energy
        self.__id = Entity.__counter
        self.__target = None
        Entity.__counter += 1

    def get_damage(self, amount):
        if not self.__alive:
            return
        if self.__hp <= amount:
            self.__alive = False
            self.__hp = 0
            self.__death_action()
            return
        else:
            self.__hp -= amount
            self.__wounded_action()
            return

    def get_healing(self, amount):
        if not self.__alive:
            return
        if self.__hp + amount >= self.__max_hp:
            self.__hp = self.__max_hp
        else:
            self.__hp += amount
        self.__healed_action()

    def set_target(self, target):
        if target.alive:
            self.__target = target
        return

    def __wrong_target(self):
        print(f"{self.__name}: wrong target")

    @property
    def get_target(self):
        return self.__target

    @property
    def get_status(self):
        return self.__alive

    @property
    def get_id(self):
        return self.__id

    @property
    def get_name(self):
        return self.__name

    @property
    def get_hp(self):
        return self.__hp

    @property
    def get_max_hp(self):
        return self.__max_hp

    @property
    def get_energy(self):
        return self.__energy

    @property
    def get_max_energy(self):
        return self.__max_energy

    @property
    def get_class(self):
        return self.__class__.__name__

    @abstractmethod
    def attack(self):
        return

    @abstractmethod
    def heal(self):
        return

    @abstractmethod
    def __death_action(self):
        return

    @abstractmethod
    def __wounded_action(self):
        return

    @abstractmethod
    def __healed_action(self):
        return

    @abstractmethod
    def __attack_skill(self):
        return

    @abstractmethod
    def __healing_skill(self):
        return

    @abstractmethod
    def __skill_action(self):
        return

    def __eq__(self, other):
        return self.__id == other.get_id
