class Hero_hw:
    name =""
    hp =0
    power = 0
    speaking = ""

    def fight(self,enemy_name,enemy_hp,enemy_power):
        my_hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        if my_hp > enemy_hp:
            print(f"{self.name}赢了")
        elif my_hp == enemy_hp:
            print(f"打平了")
        else:
            print(f"{enemy_name}赢了")

    def speak_lines(self):
        print(f"{self.speaking}")
