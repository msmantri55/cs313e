# ---------------------------
# project repos/cs313e-life/RunLife.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# ---------------------------


# -------
# imports
# -------

import sys
from Life import Life, AbstractCell, ConwayCell, FredkinCell, reader



#----------
# read file
#----------

life_lists = reader(sys.stdin)




# ---------------------
# Life ConwayCell 21x13
# ---------------------

print("*** Life ConwayCell 21x13 ***")
"""
Simulate 12 evolutions.
Print every grid (i.e. 0, 1, 2, 3, ... 12)
"""
grid = life_lists[0]
life = Life(grid)
life.add_buffer()
life.identify()
life.remove_buffer()
for i in range(13):
    print ("Generation = {0}, Population = {1}".format(life.generation, life.cell_count()))
    print(life)
    life.add_buffer()
    life.run()
    life.remove_buffer()

# ---------------------
# Life ConwayCell 20x29
# ---------------------

print("*** Life ConwayCell 20x29 ***")
"""
Simulate 28 evolutions.
Print every 4th grid (i.e. 0, 4, 8, ... 28)
"""
grid = life_lists[1]
life = Life(grid)
life.add_buffer()
life.identify()
life.remove_buffer()
for i in range(29):
    if i % 4 == 0:
        print ("Generation = {0}, Population = {1}".format(life.generation, life.cell_count()))
        print(life)
    life.add_buffer()
    life.run()
    life.remove_buffer()

# ----------------------
# Life ConwayCell 109x69
# ----------------------

print("*** Life ConwayCell 109x69 ***")
"""
Simulate 283 evolutions.
Print the first 10 grids (i.e. 0, 1, 2, ... 9).
Print the 283rd grid.
Simulate 40 evolutions.
Print the 323rd grid.
Simulate 2177 evolutions.
Print the 2500th grid.
"""
grid = life_lists[2]
life = Life(grid)
life.add_buffer()
life.identify()
life.remove_buffer()
for i in range(2501):
    if i < 10 or i in [283, 323, 2500]:
        print ("Generation = {0}, Population = {1}".format(life.generation, life.cell_count()))
        print(life)
    life.add_buffer()
    life.run()
    life.remove_buffer()

# ----------------------
# Life FredkinCell 20x20
# ----------------------

print("*** Life FredkinCell 20x20 ****")
"""
Simulate 5 evolutions.
Print every grid (i.e. 0, 1, 2, ... 5)
"""
grid = life_lists[3]
life = Life(grid)
life.add_buffer()
life.identify()
life.remove_buffer()
for i in range(6):
    print ("Generation = {0}, Population = {1}".format(life.generation, life.cell_count()))
    print(life)
    life.add_buffer()
    life.run()
    life.remove_buffer()