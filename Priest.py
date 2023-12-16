from Magician import Magician
from Shoggoth import Shoggoth
from stats_config import stats


class Priest(Magician):

    def __init__(self, name: str):
        data = stats["Priest"]
        super().__init__(data["max_hp"],
                         data["max_energy"],
                         data["damage"],
                         data["healing"],
                         data["energy_cost"],
                         name)

    def out_of_energy(self):
        print(f"{self.name}: I no longer posses a Gods blessing")

    def death_action(self):
        print(f"{self.name}: Nodence.. has not.. protected me..")

    def wounded_action(self):
        print(f"{self.name}: How dare you!")

    def healed_action(self):
        print(f"{self.name}: Now that's more like it!")

    def attack_skill(self):
        amount = self.damage
        if isinstance(self.target, Shoggoth):
            amount *= 5
        self.target.get_damage(amount)

    def healing_skill(self):
        self.target.get_healing(self.healing)

    def skill_action(self):
        print(f"{self.name}: *prays to the Outer Gods*")
