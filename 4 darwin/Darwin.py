# ---------------------------
# project repos/cs313e-darwin/Darwin.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# Jeremy Phan
# jp43992
# ---------------------------

#----------
# imports
#----------

import random

#----------
# Darwin
#----------

class Darwin():
    """
    Darwin's World is maintained and manipulated here
    All instructions are taken in through Creature and from Creature, Species
    and then used to do the action or control itself.
    """

    def __init__(self, vertical, horizontal):

        self.vertical = vertical
        self.horizontal = horizontal
        
        self.creature_list = []



        assert isinstance(vertical, int)
        assert isinstance(horizontal, int)
        assert vertical > 0
        assert horizontal > 0


        self.world = [["." for i in range(horizontal)] for j in range(vertical)]

    def __str__(self):
        output = "  "


        for i in range(self.horizontal): #top row in output
            output += str(i%10)

        output += "\n"

        for i in range(self.vertical):
            output += str(i%10) + " "     #first number of each row
            for j in range(self.horizontal):
                try:
                    output += self.world[i][j]   #for loop to print all of the items in the row
                except TypeError:
                    creature_name = self.world[i][j].__str__()
                    output += creature_name

            output += "\n"

        assert isinstance(output, str)
        return output

    def addCreature(self, y, x, creature):
        """
        this method adds a particular creature initialized through
        the Creature class onto a particular coordinate of Darwin's World
        """
        assert isinstance(creature, Creature)


        self.world[y][x] = creature
        self.creature_list.append(creature)



    def darwin_solve(self):
        """
        the solve function performs all actions required to manipulate within Darwins World
        """

        for creature in self.creature_list:
            creature.turn = True
            creature.empty = False


        for y_dir in range(len(self.world)):

            for x_dir in range(len(self.world[y_dir])):

                if self.world[y_dir][x_dir] == ".":
                    continue


                else:


                    creature = self.world[y_dir][x_dir]


                    while creature.turn == True:
                        



                        if creature.program[creature.counter] == "left":
                            creature.counter += 1
                            creature.direction = creature.species.left(creature.direction)

                            #print (creature.species, "left")
                            creature.turn = False
                            break

                        elif creature.program[creature.counter] == "right":
                            creature.counter +=1
                            creature.direction = creature.species.right(creature.direction)

                            #print (creature.species, "right")

                            creature.turn = False
                            return ("right")
                            break

                        elif creature.program[creature.counter] == "hop":

                            creature.counter += 1

                            creature.turn = False

                            #print (creature.species, "hop", creature.direction)

                            if creature.direction == 0 and x_dir >= 1 and self.world[y_dir][x_dir - 1] == ".":

                                self.world[y_dir][x_dir - 1] = creature

                                self.world[y_dir][x_dir] = "."

                            elif creature.direction == 1 and y_dir >= 1 and self.world[y_dir - 1][x_dir] == ".":
                                self.world[y_dir - 1][x_dir] = creature
                                self.world[y_dir][x_dir] = "."

                            elif creature.direction == 2 and x_dir < len(self.world[y_dir]) - 1 and self.world[y_dir][x_dir + 1] == ".":

                                self.world[y_dir][x_dir + 1] = creature
                                self.world[y_dir][x_dir] = "."

                            elif creature.direction == 3 and y_dir < len(self.world) - 1 and self.world[y_dir + 1][x_dir] == ".":

                                self.world[y_dir + 1][x_dir] = creature
                                self.world[y_dir][x_dir] = "."

                            break



                        elif creature.program[creature.counter] == "infect":
                            creature.turn = False
                            creature.counter += 1

                            #print (creature.species, "infect")
                            assert isinstance(creature.program, list)
                            if creature.direction == 0 and x_dir >= 1:
                                direction_store = self.world[y_dir][x_dir - 1].direction
                                
                                self.addCreature(y_dir, x_dir -1, Creature(creature.species, direction_store))

                            elif creature.direction == 1 and y_dir >= 1:
                                direction_store = self.world[y_dir - 1][x_dir].direction

                                self.addCreature(y_dir - 1, x_dir, Creature(creature.species, direction_store))


                            elif creature.direction == 2 and x_dir < len(self.world[y_dir]) - 1:
                                direction_store = self.world[y_dir][x_dir + 1].direction

                                self.addCreature(y_dir, x_dir + 1, Creature(creature.species, direction_store))


                            elif creature.direction == 3 and y_dir < len(self.world) - 1:
                                direction_store = self.world[y_dir + 1][x_dir].direction
        
                                self.addCreature(y_dir + 1, x_dir, Creature(creature.species, direction_store))


                            break


                        elif creature.program[creature.counter][0:2] == "go":
                            creature.counter = int(creature.program[creature.counter][-1])

                            #print (creature.species, "go")

                        elif creature.program[creature.counter][0:8] == "if_empty":

                            #print (creature.species, "if empty")

                            assert isinstance(creature.program, list)
                            if creature.direction == 0 and x_dir >= 1 and self.world[y_dir][x_dir - 1] == ".":

                                creature.counter = int(creature.program[creature.counter][-1])


                            elif creature.direction == 1 and y_dir >= 1 and self.world[y_dir - 1][x_dir] == ".":


                                
                                creature.counter = int(creature.program[creature.counter][-1])

                            elif creature.direction == 2 and x_dir < len(self.world[y_dir]) - 1 and self.world[y_dir][x_dir + 1] == ".":

                                creature.counter = int(creature.program[creature.counter][-1])

                            elif creature.direction == 3 and y_dir < len(self.world) - 1 and self.world[y_dir + 1][x_dir] == ".":

    
                                creature.counter = int(creature.program[creature.counter][-1])

                            else:
                                creature.counter += 1
                                continue

                        elif creature.program[creature.counter][0:9] == "if_random":

                            #print (creature.species, "if random")
                            assert isinstance(creature.program, list)
                            random.seed(0)
                            if random.randrange(0,2)%2 == 1:
                                creature.counter = int(creature.program[creature.counter][-1])
                            else:
                                creature.counter += 1

                        elif creature.program[creature.counter][0:7] == "if_wall":

                            #print (creature.species, "if wall")
                            assert isinstance(creature.program, list)
                            if creature.direction == 0:
                                if x_dir == 0:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1

                            if creature.direction == 1:
                                if y_dir == 0:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1

                            if creature.direction == 2:
                                if x_dir == len(self.world[y_dir]) - 1:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1

                            if creature.direction == 3:

                                if y_dir == len(self.world) - 1:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1
                       

                        elif creature.program[creature.counter][0:8] == "if_enemy":

                            #print (creature.species, "if enemy")
                            assert isinstance(creature.program, list)

                            if creature.direction == 0:
                                if x_dir > 0 and self.world[y_dir][x_dir -1] != "." and self.world[y_dir][x_dir -1].species != creature.species:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1

                            if creature.direction == 1:
                                if y_dir > 0 and self.world[y_dir - 1][x_dir ] != "." and self.world[y_dir - 1][x_dir].species != creature.species:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1

                            if creature.direction == 2:
                                if x_dir < len(self.world[y_dir]) -2 and self.world[y_dir][x_dir + 1] != "." and self.world[y_dir][x_dir +1].species != creature.species:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1

                            if creature.direction == 3:

                                if y_dir < len(self.world) - 1 and self.world[y_dir + 1][x_dir] != "." and self.world[y_dir+1][x_dir ].species != creature.species:
                                    creature.counter = int(creature.program[creature.counter][-1])

                                else:
                                    creature.counter += 1




                        





                        

#----------
# Creature
#----------


class Creature():
    """
    The Creature class takes an instance of Species class and contains
    the set of instructions for an individual of that Species.
    """
    def __init__(self, species, direction):
        self.turn = True  #True identifies a creature that hasn't gone. Will need to be changed to False when it has gone.

        self.counter = 0
        self.direction = direction

        self.empty = False

        self.species = species
        self.program = species.instructions

    def __str__(self):

        assert isinstance(self.species.name, str)
        return self.species.name[0]



                

            




#----------
# Species
#----------

class Species():
    """
    The Species class simply outlines the different actions and
    control actions that Creatures within Darwin's World can
    perform.
    """
    def __init__(self, name):

        self.name = name
        self.instructions = []


    def addInstruction(self, instruction):
        """
        Adds particular instructions from the other methods in Class species
        to the list of steps to perform identified as the instructions list.
        """
        self.instructions.append(instruction)


    def left(self, direction):
        """
        instruction that turns the creature to face one unit to the left.
        """
        assert 0 <= direction <= 3

        if direction > 0:
            direction -= 1
        else:
            direction = 3
        

        return direction


    def right(self, direction):
        """
        instruction that turns the creature to face one unit to the right.
        """
        assert 0 <= direction <= 3

        if direction > 2:
            direction = 0
        else:
            direction +=1
        

        return direction


    def __str__(self):
        return self.name

