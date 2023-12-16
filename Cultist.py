from Enemy import Enemy
from Shoggoth import Shoggoth
from stats_config import stats


class Cultist(Enemy):

    def __init__(self):
        data = stats["Cultist"]
        super().__init__(data["max_hp"],
                         data["max_energy"],
                         data["damage"],
                         data["healing"],
                         "Cultist")

    def death_action(self):
        print(f"Cultist({self.id}): You! You will.. regret this..")

    def wounded_action(self):
        print(f"Cultist({self.id}): You shall pay a bucket of your blood"
              f"\nfor each drop of mine!")

    def healed_action(self):
        print(f"Cultist({self.id})Invincible! That the word you was looking for")

    def attack_skill(self):
        self.target.get_damage(self.damage)

    def healing_skill(self):
        amount = self.healing
        if isinstance(self.target, Shoggoth):
            amount *= 3
        self.target.get_healing(amount)

    def skill_action(self):
        print(f"Cultist({self.id}): Hear the eternal call!")
