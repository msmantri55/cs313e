# -----------------------------
# project repos/cs313e-darwin/Darwin.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# -----------------------------

# -------
# imports
# -------

from random import randrange, seed
from Darwin import Darwin, Creature, Species
import sys



# ----
# food
# ----

food = Species("food")
food.addInstruction("left")
food.addInstruction("go 0")

"""
 0: left
 1: go 0
"""


# ------
# hopper
# ------
hopper = Species("hopper")
hopper.addInstruction("hop")
hopper.addInstruction("go 0")

"""
 0: hop
 1: go 0
"""

# -----
# rover
# -----

rover = Species("rover")
rover.addInstruction("if_enemy 9")
rover.addInstruction("if_empty 7")
rover.addInstruction("if_random 5")
rover.addInstruction("left")
rover.addInstruction("go 0")
rover.addInstruction("right")
rover.addInstruction("go 0")
rover.addInstruction("hop")
rover.addInstruction("go 0")
rover.addInstruction("infect")
rover.addInstruction("go 0")

"""
 0: if_enemy 9
 1: if_empty 7
 2: if_random 5
 3: left
 4: go 0
 5: right
 6: go 0
 7: hop
 8: go 0
 9: infect
10: go 0
"""

# ----
# trap
# ----

trap = Species("trap")
trap.addInstruction("if_enemy 3")
trap.addInstruction("left")
trap.addInstruction("go 0")
trap.addInstruction("infect")
trap.addInstruction("go 0")

"""
 0: if_enemy 3
 1: left
 2: go 0
 3: infect
 4: go 0
"""

# ----
# best
# ----

best = Species("best")
best.addInstruction("if_enemy 11")
best.addInstruction("if_empty 13")
best.addInstruction("left")
best.addInstruction("left")
best.addInstruction("hop")
best.addInstruction("left")
best.addInstruction("left")
best.addInstruction("if_enemy 13")
best.addInstruction("left")
best.addInstruction("right")
best.addInstruction("go 7")
best.addInstruction("infect")
best.addInstruction("go 0")
best.addInstruction("hop")
best.addInstruction("go 0")
best.addInstruction("infect 15")
best.addInstruction("go 7")

# ----------
# darwin 8x8
# ----------

print("*** Darwin 8x8 ***")
x = Darwin(8,8)




#x.addCreature(food1, 5, 4)
x.addCreature(0, 0, Creature(food, 2))
x.addCreature(3, 3, Creature(hopper, 1))
x.addCreature(3, 4, Creature(hopper, 2))
x.addCreature(4, 4, Creature(hopper, 3))
x.addCreature(4, 3, Creature(hopper, 0))
x.addCreature(7, 7, Creature(food, 1))

#print ("*** Darwin {0}x{1} ***".format(x.vertical, x.horizontal))

for simulation in range(6):
    print ("Turn : " + str(simulation))

    print(x)

    x.darwin_solve()

"""
8x8 Darwin
Food,   facing east,  at (0, 0)
Hopper, facing north, at (3, 3)
Hopper, facing east,  at (3, 4)
Hopper, facing south, at (4, 4)
Hopper, facing west,  at (4, 3)
Food,   facing north, at (7, 7)
Simulate 5 moves.
Print every grid.
"""

# ----------
# darwin 7x9
# ----------

print("*** Darwin 7x9 ***")


x = Darwin(7,9)


#x.addCreature(food1, 5, 4)
x.addCreature(0, 0, Creature(trap, 3))
x.addCreature(3, 2, Creature(hopper, 2))
x.addCreature(5, 4, Creature(rover, 1))
x.addCreature(6, 8, Creature(trap, 0))


#print ("*** Darwin {0}x{1} ***".format(x.vertical, x.horizontal))

for simulation in range(6):
    print ("Turn : " + str(simulation))

    print(x)

    x.darwin_solve()


"""
7x9 Darwin
Trap,   facing south, at (0, 0)
Hopper, facing east,  at (3, 2)
Rover,  facing north, at (5, 4)
Trap,   facing west,  at (6, 8)
Simulate 5 moves.
Print every grid.
"""

# ------------
# darwin 72x72
# without best
# ------------

print("*** Darwin 72x72 without Best ***")


x = Darwin(72, 72)
seed(0)


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72),Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))







for simulation in range(1000):


    if simulation < 10:
        print ("Turn : " + str(simulation))
        print(x)
    elif simulation == 99 or simulation == 199 or simulation == 299 or simulation == 399 or simulation == 499 or simulation == 599 or simulation == 699 or simulation == 799 or simulation == 899 or simulation == 999:
        print ("Turn : " + str(simulation))
        print(x)



    x.darwin_solve()

"""
Randomly place the following creatures facing randomly.
Call random.randrange(0, 72) to specify the row.
Call random.randrange(0, 72) to specify the col.
Call random.randrange(0,  4) to specify the direction: 0:west, 1:north, 2:east, 3:south.
Do that for each kind of creature.
10 Food
10 Hopper
10 Rover
10 Trap
Simulate 1000 moves.
Print the first 10 grids          (i.e. 0, 1, 2...9).
Print every 100th grid after that (i.e. 100, 200, 300...1000).
"""

# ------------
# darwin 72x72
# with best
# ------------

print("*** Darwin 72x72 with Best ***")

x = Darwin(72, 72)
seed(0)


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72),Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(food, randrange(0, 4)))


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(hopper, randrange(0, 4)))


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(rover, randrange(0, 4)))


x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(trap, randrange(0, 4)))

x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))
x.addCreature(randrange(0, 72), randrange(0, 72), Creature(best, randrange(0, 4)))





for simulation in range(1000):


    if simulation < 10:
        print ("Turn : " + str(simulation))
        print(x)
    elif simulation == 99 or simulation == 199 or simulation == 299 or simulation == 399 or simulation == 499 or simulation == 599 or simulation == 699 or simulation == 799 or simulation == 899 or simulation == 999:
        print ("Turn : " + str(simulation))
        print(x)



    x.darwin_solve()


"""
Randomly place the following creatures facing randomly.
Call random.randrange(0, 72) to specify the row.
Call random.randrange(0, 72) to specify the col.
Call random.randrange(0,  4) to specify the direction: 0:west, 1:north, 2:east, 3:south.
Do that for each kind of creature.
10 Food
10 Hopper
10 Rover
10 Trap
10 Best
Simulate 1000 moves.
Best MUST outnumber ALL other species for the bonus pts.
Print the first 10 grids          (i.e. 0, 1, 2...9).
Print every 100th grid after that (i.e. 100, 200, 300...1000).
"""
