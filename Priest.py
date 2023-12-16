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

    def __out_of_energy(self):
        print(f"{self.__name}: I no longer posses a Gods blessing")

    def __death_action(self):
        print(f"{self.__name}: Nodence.. has not.. protected me..")

    def __wounded_action(self):
        print(f"{self.__name}: How dare you!")

    def __healed_action(self):
        print(f"{self.__name}: Now that's more like it!")

    def __attack_skill(self):
        amount = self.__damage
        if isinstance(self.__target, Shoggoth):
            amount *= 5
        self.__target.get_damage(amount)

    def __healing_skill(self):
        self.__target.get_healing(self.__healing)

    def __skill_action(self):
        print(f"{self.__name}: *prays to the Outer Gods*")
