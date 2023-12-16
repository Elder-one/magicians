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

    def __death_action(self):
        print(f"Shoggoth({self.__id}): *decays*")

    def __wounded_action(self):
        print(f"Shoggoth({self.__id}): *screams with disgusting noises*")

    def __healed_action(self):
        print(f"Shoggoth({self.__id}): *regenerates*")

    def __attack_skill(self):
        self.__target.get_damage(self.__damage)

    def __healing_skill(self):
        if self.__target != self:
            return
        else:
            self.__target.get_healing(self.__healing)

    def __skill_action(self):
        print(f"Shoggoth({self.__id}): Te-ke-li-ly!")
