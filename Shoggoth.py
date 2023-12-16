from Enemy import Enemy
from stats_config import stats


class Shoggoth(Enemy):

    def __init__(self):
        data = stats["Shoggoth"]
        super().__init__(data["max_hp"],
                         data["max_energy"],
                         data["damage"],
                         data["healing"],
                         "Shoggoth")

    def death_action(self):
        print(f"Shoggoth({self.id}): *decays*")

    def wounded_action(self):
        print(f"Shoggoth({self.id}): *screams with disgusting noises*")

    def healed_action(self):
        print(f"Shoggoth({self.id}): *regenerates*")

    def attack_skill(self):
        self.target.get_damage(self.damage)

    def healing_skill(self):
        if self.target != self:
            return
        else:
            self.target.get_healing(self.healing)

    def skill_action(self):
        print(f"Shoggoth({self.id}): Te-ke-li-ly!")
