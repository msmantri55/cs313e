# ---------------------------
# project repos/cs313e-darwin/TestDarwin.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# ---------------------------

# -------
# imports
# -------
from io       import StringIO
from unittest import main, TestCase

from Darwin import Darwin, Creature, Species

# -----------
# TestDarwin
# -----------

class TestDarwin (TestCase) :
    def test_addCreature1(self):
        x = Darwin(3, 3)
        food = Species("food")
        food1 = Creature(food, 0)
        x.addCreature(0, 0 , food1)

        assert len(x.creature_list) == 1

    def test_addCreature2(self):
        x = Darwin(3, 3)
        food = Species("food")
        food1 = Creature(food, 0)
        x.addCreature(0, 0 , food1)

        assert isinstance(x.world[0][0], Creature)

    def test_addCreature3(self):
        x = Darwin(3, 3)
        food = Species("food")
        food1 = Creature(food, 0)
        food2 = Creature(food, 2)

        x.addCreature(0, 0 , food1)
        x.addCreature(2, 2 , food2)

        assert len(x.creature_list) == 2



    def test_addCreature4(self):
        x = Darwin(3, 3)
        food = Species("food")
        food1 = Creature(food, 0)
        food2 = Creature(food, 2)

        x.addCreature(0, 0 , food1)
        x.addCreature(2, 2 , food2)

        assert len(x.creature_list) == 2

    def test_darwin_solve1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food.addInstruction("go 0")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert isinstance(x.world[0][1], Creature)

    def test_darwin_solve2(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food.addInstruction("go 0")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert food1.direction == 3


    def test_addInstruction1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (x.creature_list[0].program == ["left"])

    def test_addInstruction2(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food.addInstruction("right")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (x.creature_list[0].program == ["left", "right"])

    def test_addInstruction3(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (len(x.creature_list[0].program) == 1)

    def test_left1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert food1.direction == 3

    def test_left2(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food1 = Creature(food, 1)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (food1.direction == 0)

    def test_left3(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("left")
        food1 = Creature(food, 3)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (food1.direction == 2)

    def test_right1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (food1.direction == 1)

    def test_right2(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food1 = Creature(food, 1)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (food1.direction == 2)
    def test_right3(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food1 = Creature(food, 2)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()
        assert (food1.direction == 3)

    def test_creature_str1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food1 = Creature(food, 0)

        assert (str(food1) == "f")

    def test_creature_str2(self):
        x = Darwin(2, 2)
        hopper = Species("hopper")
        hopper1 = Creature(hopper, 0)

        assert (str(hopper1) == "h")


    def test_right_conditional1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food.addInstruction("go 0")
        food1 = Creature(food, 0)
        x.addCreature(0, 1 , food1)

        counter = food1.counter
        solve = x.darwin_solve()
        assert (food1.direction == 1)
        assert (food1.counter == counter + 1)

    def test_right_conditional2(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food.addInstruction("go 0")
        food1 = Creature(food, 1)
        x.addCreature(0, 1 , food1)

        counter = food1.counter
        solve = x.darwin_solve()
        assert (food1.direction == 2)
        assert (food1.counter == counter + 1)


    def test_right_conditional3(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food.addInstruction("go 0")
        food1 = Creature(food, 2)
        x.addCreature(0, 1 , food1)

        counter = food1.counter
        solve = x.darwin_solve()
        assert (food1.direction == 3)
        assert (food1.counter == counter + 1)

    def test_right_conditional4(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("right")
        food.addInstruction("go 0")
        food1 = Creature(food, 3)
        x.addCreature(0, 1 , food1)

        counter = food1.counter
        solve = x.darwin_solve()
        assert (food1.direction == 0)
        assert (food1.counter == counter + 1)

    def test_go1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("go 1")
        food.addInstruction("right")
        food.addInstruction("go 0")

        food1 = Creature(food, 3)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()

        assert (food1.counter == 2)

    def test_empty1(self):
        x = Darwin(2, 2)
        food = Species("food")
        food.addInstruction("if_empty 2")
        food.addInstruction("right")
        food.addInstruction("hop")
        food.addInstruction("go 0")

        food1 = Creature(food, 3)
        x.addCreature(0, 1 , food1)

        solve = x.darwin_solve()

        assert (food1.counter == 3)


    def test_empty2(self):
        x = Darwin(8, 8)
        food = Species("food")
        food.addInstruction("if_empty 2")
        food.addInstruction("right")
        food.addInstruction("hop")
        food.addInstruction("go 0")


        food2 = Creature(food, 0)
        x.addCreature(2, 2 , food2)
        food3 = Creature(food, 1)
        x.addCreature(4, 4 , food3)
        food4 = Creature(food, 2)
        x.addCreature(6, 6 , food4)


        solve = x.darwin_solve()

        assert (food2.counter == 3)
        assert (food2.direction == 0)
        assert (food3.counter == 3)
        assert (food3.direction == 1)
        assert (food4.counter == 3)
        assert (food4.direction == 2)


    def test_infect1(self):
        x = Darwin(3, 3)

        food = Species("food")
        food.addInstruction("right")

        rover = Species("rover")
        rover.addInstruction("if_enemy 2")
        rover.addInstruction("right")
        rover.addInstruction("infect")
        rover.addInstruction("go 0")



        food1 = Creature(food, 0)
        x.addCreature(1, 1 , food1)

        rover1 = Creature(rover, 2)
        x.addCreature(1, 0 , rover1)

        solve = x.darwin_solve()

        assert (x.world[1][1].species == rover1.species)




main()