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

    def __death_action(self):
        print(f"Cultist({self.__id}): You! You will.. regret this..")

    def __wounded_action(self):
        print(f"Cultist({self.__id}): You shall pay a bucket of your blood"
              f"\nfor each drop of mine!")

    def __healed_action(self):
        print(f"Cultist({self.__id})Invincible! That the word you was looking for")

    def __attack_skill(self):
        self.__target.get_damage(self.__damage)

    def __healing_skill(self):
        amount = self.__healing
        if isinstance(self.__target, Shoggoth):
            amount *= 3
        self.__target.get_healing(amount)

    def __skill_action(self):
        print(f"Cultist({self.__id}): Hear the eternal call!")
