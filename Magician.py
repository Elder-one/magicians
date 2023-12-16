from abc import abstractmethod

from Enemy import Enemy
from Entity import Entity


class Magician(Entity):

    def __init__(self, max_hp: int, max_energy: int,
                 damage: int, healing: int,
                 energy_cost: int, name: str):
        super().__init__(max_hp, max_energy,
                         damage, healing, name)
        self.energy_cost = energy_cost

    def attack(self):
        if self.energy < self.energy_cost:
            self.out_of_energy()
            return
        if self.target is None:
            self.wrong_target()
            return
        if not isinstance(self.target, Enemy):
            self.wrong_target()
            return
        if not self.target.alive:
            self.wrong_target()
            return
        self.attack_skill()
        self.skill_action()
        self.energy -= self.energy_cost

    def heal(self):
        if self.energy < self.energy_cost:
            self.out_of_energy()
            return
        if self.target is None:
            self.wrong_target()
            return
        if not isinstance(self.target, Magician):
            self.wrong_target()
            return
        if not self.target.alive:
            self.wrong_target()
            return
        self.healing_skill()
        self.skill_action()
        self.energy -= self.energy_cost

    @abstractmethod
    def out_of_energy(self):
        return

    @abstractmethod
    def death_action(self):
        return

    @abstractmethod
    def wounded_action(self):
        return

    @abstractmethod
    def healed_action(self):
        return

    @abstractmethod
    def attack_skill(self):
        return

    @abstractmethod
    def healing_skill(self):
        return

    @abstractmethod
    def skill_action(self):
        return
