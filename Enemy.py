from abc import abstractmethod

from Entity import Entity
from Magician import Magician


class Enemy(Entity):

    def __init__(self, max_hp: int, max_energy: int,
                 damage: int, healing: int, name: str):
        super().__init__(max_hp, max_energy,
                         damage, healing, name)

    def attack(self):
        if self.__target is None:
            self.__wrong_target()
            return
        if not isinstance(self.__target, Magician):
            self.__wrong_target()
            return
        if not self.__target.get_status:
            self.__wrong_target()
            return
        self.__attack_skill()
        self.__skill_action()

    def heal(self):
        if self.__target is None:
            self.__wrong_target()
            return
        if not isinstance(self.__target, Enemy):
            self.__wrong_target()
            return
        if not self.__target.get_status:
            self.__wrong_target()
            return
        self.__healing_skill()
        self.__skill_action()

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
