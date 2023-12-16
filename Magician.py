from abc import abstractmethod

from Enemy import Enemy
from Entity import Entity


class Magician(Entity):

    def __init__(self, max_hp: int, max_energy: int,
                 damage: int, healing: int,
                 energy_cost: int, name: str):
        super().__init__(max_hp, max_energy,
                         damage, healing, name)
        self.__energy_cost = energy_cost

    def attack(self):
        if self.__energy < self.__energy_cost:
            self.__out_of_energy()
            return
        if self.__target is None:
            self.__wrong_target()
            return
        if not isinstance(self.__target, Enemy):
            self.__wrong_target()
            return
        if not self.__target.get_status:
            self.__wrong_target()
            return
        self.__attack_skill()
        self.__skill_action()
        self.__energy -= self.__energy_cost

    def heal(self):
        if self.__energy < self.__energy_cost:
            self.__out_of_energy()
            return
        if self.__target is None:
            self.__wrong_target()
            return
        if not isinstance(self.__target, Magician):
            self.__wrong_target()
            return
        if not self.__target.get_status:
            self.__wrong_target()
            return
        self.__healing_skill()
        self.__skill_action()
        self.__energy -= self.__energy_cost

    @abstractmethod
    def __out_of_energy(self):
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
