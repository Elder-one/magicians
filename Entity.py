from abc import ABC, abstractmethod


class Entity(ABC):

    counter = 0

    def __init__(self, max_hp: int, max_energy: int,
                 damage: int, healing: int, name: str):
        self.healing = healing
        self.damage = damage
        self.name = name
        self.alive = True
        self.max_hp = max_hp
        self.max_energy = max_energy
        self.hp = max_hp
        self.energy = max_energy
        self.id = Entity.counter
        self.target = None
        Entity.counter += 1

    def get_damage(self, amount):
        if not self.alive:
            return
        if self.hp <= amount:
            self.alive = False
            self.hp = 0
            self.death_action()
            return
        else:
            self.hp -= amount
            self.wounded_action()
            return

    def get_healing(self, amount):
        if not self.alive:
            return
        if self.hp + amount >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += amount
        self.healed_action()

    def set_target(self, target):
        if target.alive:
            self.target = target
        return

    def wrong_target(self):
        print(f"{self.name}: wrong target")

    @abstractmethod
    def attack(self):
        return

    @abstractmethod
    def heal(self):
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

    def __eq__(self, other):
        return self.id == other.id
