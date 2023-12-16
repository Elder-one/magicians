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

    def __out_of_energy(self):
        print(f"{self.__name}: My energy flow is interrupted!")

    def __death_action(self):
        print(f"{self.__name}: A worthy opponent ..")

    def __wounded_action(self):
        print(f"{self.__name}: Barely a scratch!")

    def __healed_action(self):
        print(f"{self.__name}: Alright, it's my turn")

    def __attack_skill(self):
        amount = self.__damage
        if isinstance(self.__target, Cultist):
            amount /= 2
        self.__target.get_damage(amount)

    def __healing_skill(self):
        self.__target.get_healing(self.__healing)

    def __skill_action(self):
        print(f"{self.__name}: *casts a spell*")

