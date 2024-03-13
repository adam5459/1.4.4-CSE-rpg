import random as rd


class Entity:
    def __init__(self, name, health,  attack, defense, description):
        self.name = name
        self.luck = rd.randint(1, 20) + rd.randint(1, 20)
        self.health = int(health)
        self.attack = int(attack)
        self.defense = int(defense)
        self.alive = True
        self.description = description

    def is_dead(self):
        if int(self.health) <= 0:
            self.alive = False
            self.name = f"*DEAD* {self.name}"

    def printDetails(self):
        print(f"""
        -----------------------------
            Name == {self.name}
            Health == {self.health}
            Atk == {self.attack}
            Def == {self.defense}
            Description ==
                {self.description}
        -----------------------------
        """)

class npc(Entity):
    def __init__(self, name, health,  attack, defense, description):
        super().__init__(name, health,  attack, defense, description)

    def initialize(self):
        name = ''.join(char for char in str(self.name) if not char.isdigit())
        if name == "Goblin":
            self.attack = rd.randint(1, 15) + rd.randint(1, 15)
            self.defense = rd.randint(1, 10) + rd.randint(1, 10)
            self.luck = rd.randint(1, 20) + rd.randint(1, 20)
        elif name == "Drawf":
            self.attack =  rd.randint(1, 17) + rd.randint(1, 17)
            self.defense = rd.randint(1, 9) + rd.randint(1, 9)
            self.luck = rd.randint(1, 20) + rd.randint(1, 20)


        elif name == "Big Goblin":
            self.attack = rd.randint(1, 20) + rd.randint(1, 20)
            self.defense =  rd.randint(1, 15) + rd.randint(1, 25)
            self.luck = rd.randint(1, 20) + rd.randint(1, 20)


class pc(Entity):
    def __init__(self, name, health, attack, defense, description):
        super().__init__(name, health, attack, defense, description)
        self.health = rd.randint(1, 20) + rd.randint(1, 20)
        self.attack = rd.randint(1, 20) + rd.randint(1, 20)
        self.defense = rd.randint(1, 20) + rd.randint(1, 20)

    def initialize(self):
        self.attack = rd.randint(1, 20) + rd.randint(1, 20)
        self.defense = rd.randint(1, 20) + rd.randint(1, 20)
        self.luck = rd.randint(1, 20) + rd.randint(1, 20)


def fight(p1, p2):
    attacking, defending = p1, p2
    if p1.luck > p2.luck:
        pass
    elif p1.luck < p2.luck:
        attacking, defending = p2, p1
    hit_points = attacking.attack - defending.defense
    if hit_points >= 0:
        defending.health -= hit_points
        print(f"{attacking.name} hit {defending.name} for {hit_points}")
    else:
        attacking.health += hit_points
        print(f"{defending.name} countered {attacking.name} for {hit_points * -1}")

#####################################################################################################################
name = input("whats your name? ")
descrip = input("describe your self: ")
mobLst = []
goblin = {'name': "Goblin",
          'health': rd.randint(1, 10) + rd.randint(1, 10),
          "attack": rd.randint(1, 15) + rd.randint(1, 15),
          'defense': rd.randint(1, 10) + rd.randint(1, 10),
          "description": "some green goblin thing"}


drawf = {"name": "Drawf",
         "health": rd.randint(1, 10) + rd.randint(1, 10),
         "attack": rd.randint(1, 17) + rd.randint(1, 17),
         "defense": rd.randint(1, 9) + rd.randint(1, 9),
         "description": "short"}


big_goblin = {"name": "Big Gobblin",
              "health": rd.randint(1, 20) + rd.randint(1, 20),
              "attack": rd.randint(1, 20) + rd.randint(1, 20),
              "defense": rd.randint(1, 15) + rd.randint(1, 25),
              "description": "big guy", }
amount_of_enemys = 0
temp = input("Would you like to play (E)asy (M)edium or (H)ard: ")
if temp.lower() == "e":
    mode = "easy"
    amount_of_enemys = 5
elif temp.lower() == "m":
    mode = "medium"
    amount_of_enemys = 10
elif temp.lower() == "h":
    mode = "hard"
    amount_of_enemys = 20
easyC, mediumC, hardC = 0, 0, 0
for _ in range(amount_of_enemys):
    value = rd.randint(1,50) + rd.randint(1, 50)
    if value <= 50:
        easyC += 1
    elif value <= 80:
        mediumC += 1
    elif value <= 100:
        hardC += 1
for x in range(easyC):
    mobLst.append(npc(goblin['name']+str(x+1),
                      rd.randint(1, 10) + rd.randint(1, 10),
                      rd.randint(1, 15) + rd.randint(1, 15),
                      rd.randint(1, 10) + rd.randint(1, 10),
                      goblin['description']))
for x in range(mediumC):
    mobLst.append(npc(drawf['name']+str(x+1),
                      rd.randint(1, 10) + rd.randint(1, 10),
                      rd.randint(1, 17) + rd.randint(1, 17),
                      rd.randint(1, 9) + rd.randint(1, 9),
                      drawf['description']))
for x in range(hardC):
    mobLst.append(npc(big_goblin['name']+str(x+1),
                      rd.randint(1, 20) + rd.randint(1, 20),
                      rd.randint(1, 20) + rd.randint(1, 20),
                      rd.randint(1, 15) + rd.randint(1, 25),
                      big_goblin['description']))  

for c, mob in enumerate(mobLst):
    print(f"{c+1}. \n")
    mob.printDetails()

aliveMobLst = [mob for mob in mobLst if mob.alive]

mc = pc(name, '40', '20', '20', descrip)

while mc.alive and aliveMobLst:
        mob_fighting = rd.randint(1, amount_of_enemys)
        mob_fighting %= len(aliveMobLst)
        mob = aliveMobLst[mob_fighting]
        while mob.alive and mc.alive:
            print(F"""
            -------------------------------
              Fighting {mob.name}
            -------------------------------
              """)
            fight(mc, mob)
            input()
            mc.initialize()
            mob.initialize()
            mob.is_dead()
            mc.is_dead()
        aliveMobLst = [mob for mob in aliveMobLst if mob.alive]

if mc.alive:
    print("you win")
    mc.printDetails()
else:
    for mob in aliveMobLst:
        mob.printDetails()
    for mob in mobLst:
        mob.printDetails()

    print('you died')
