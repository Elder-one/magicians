from Cultist import Cultist
from Magician import Magician
from stats_config import stats


class Wizard(Magician):

    def __init__(self, name: str):
        data = stats["Wizard"]
        super().__init__(data["max_hp"],
                         data["max_energy"],
                         data["damage"],
                         data["healing"],
                         data["energy_cost"],
                         name)

    def out_of_energy(self):
        print(f"{self.name}: My energy flow is interrupted!")

    def death_action(self):
        print(f"{self.name}: A worthy opponent ..")

    def wounded_action(self):
        print(f"{self.name}: Barely a scratch!")

    def healed_action(self):
        print(f"{self.name}: Alright, it's my turn")

    def attack_skill(self):
        amount = self.damage
        if isinstance(self.target, Cultist):
            amount /= 2
        self.target.get_damage(amount)

    def healing_skill(self):
        self.target.get_healing(self.healing)

    def skill_action(self):
        print(f"{self.name}: *casts a spell*")

