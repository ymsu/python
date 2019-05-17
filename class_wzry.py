#coding:gbk
import time

class Hero:
    def __init__(self, health, output1, cd1, output2, cd2):
        self.health = health
        self.output1 = output1
        self.cd1 = cd1
        self.output2 = output2
        self.cd2 = cd2

    def skill_1(self):
        #print("skill 1")
        return self.output1

    def skill_2(self):
        #print("skill 2")
        return self.output2

def kill(first_act, second_act):

    def print_health():
        print("first_act's health is %s, second_act's health is %s" % (first_act.health, second_act.health))
    # 技能 cd 都是好的
    start_time = time.time()
    print_health()

    print("Start Killing...")
    second_act.health -= first_act.skill_1()
    print_health()
    first_act.health -= second_act.skill_1()
    print_health()
    second_act.health -= first_act.skill_2()
    print_health()
    first_act.health -= second_act.skill_2()
    print_health()

    while True:
        now = time.time()
        if first_act.health <= 0:
            print("first_act is dead")
            break
        elif second_act.health <= 0:
            break
            print("second_act is dead")

        cd_interval = int(now - start_time)

        if cd_interval % 4 == 0:
            first_act.health -= second_act.skill_1()
        elif cd_interval % 5 == 0 :
            second_act.health -= first_act.skill_1()
        elif cd_interval % 6 == 0:
            first_act.health -= second_act.skill_2()
        elif cd_interval % 7 == 0:
            second_act.health -= first_act.skill_2()
        else:
            continue

        print("first_act's health is %s, second_act's health is %s" % (first_act.health, second_act.health))


lb = Hero(health=5000, output1=1300, cd1=5, output2=1700, cd2=7)
xy = Hero(health=6000, output1=1300, cd1=4, output2=1200, cd2=6)

kill(lb, xy)
kill(xy, lb)
