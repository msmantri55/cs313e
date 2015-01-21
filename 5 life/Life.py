# ---------------------------
# project repos/cs313e-life/Life.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# ---------------------------
def reader(r):
    """
    reads the input file and breaks it down into each set of Life grids for running
    """

    life_lists = []
    x = True

    while x == True:
        grid = []

        col = r.readline()
        col = int(col.strip("\n"))

        row = r.readline()
        row = int(row.strip("\n"))

        for i in range(col):
            grid_line = []
            line = r.readline()
            for j in range(row):
                grid_line.append(line[j])

            grid.append(grid_line)

        life_lists.append(grid)
        line = r.readline()

        if line == "":
            x = False
        else:
            pass

    return life_lists


class Life():
    def __init__(self, grid):
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        self.population = 0
        self.generation = 0
        self.cells = []


    def __str__(self):
        output = ""
        for i in range(self.row):
            for j in range(self.col):
                output += str(self.grid[i][j])
            output += "\n"

        return output

    def identify(self):
        """
        identifies cells in the initial Life grid as a dead or alive Conway or Fredkin Cell and then calls their particular class
        """
        cell = None

        for i in range(1, self.row + 1):
            for j in range(1, self.col + 1):
                if self.grid[i][j] == ".":
                    cell = ConwayCell(i, j)
                    cell.is_alive = False
                    self.grid[i][j] = cell

                elif self.grid[i][j] == "*":
                    cell = ConwayCell(i, j)
                    cell.is_alive = True
                    self.grid[i][j] = cell


                elif self.grid[i][j] == "-":
                    cell = FredkinCell(i, j)
                    cell.is_alive = False
                    self.grid[i][j] = cell

                elif self.grid[i][j] == "0":
                    cell = FredkinCell(i, j)
                    cell.is_alive = True
                    self.grid[i][j] = cell

                self.cells.append(cell)


    def cell_count(self):
        """
        returns the number of alive cells in the grid
        """
        self.population = 0

        for cell in self.cells:
            assert type(cell) != str
            if cell.is_alive == True:
                self.population += 1

        return self.population

    def add_buffer(self):
        """
        adds a buffer around the grid so that during the neighborhood check,corner cases don't have to be
        coded for
        """

        self.grid.extend([['.']])  # bottom border
        for b in range(self.col - 1):
            self.grid[self.row].append('.')

        self.grid.insert(0, ['.'])  # top border
        for y in range(self.col - 1):
            self.grid[0].append('.')

        for x in range(self.row + 2):
            self.grid[x].insert(self.col + 1, '.')  # right border

        for x in range(self.row + 2):
            self.grid[x].insert(0, '.')  # left border

    def remove_buffer(self):
        """
        removes the buffer for output
        """
        grid2 = self.grid[1:-1]
        for x in range(self.row):
            row = grid2[x][1:-1]
            grid2[x] = row

        self.grid = grid2
        return self.grid

    def Conway_neighborhood(self, cell):
        """
        builds the Conway neighborhood, meaning the 8 cells surrounding this particular cell
        """
        x = cell.x
        y = cell.y

        cell.neighborhood = []
        cell.neighborhood.append(self.grid[x - 1][y])  # up
        cell.neighborhood.append(self.grid[x + 1][y])  # down
        cell.neighborhood.append(self.grid[x][y + 1])  # right
        cell.neighborhood.append(self.grid[x][y - 1])  # left
        cell.neighborhood.append(self.grid[x - 1][y + 1])  # top right
        cell.neighborhood.append(self.grid[x + 1][y + 1])  # bottom right
        cell.neighborhood.append(self.grid[x - 1][y - 1])  # top left
        cell.neighborhood.append(self.grid[x + 1][y - 1])  # bottom left

    def Fredkin_neighborhood(self, cell):
        """
        builds the Fredkin neighborhood, meaning the 4 cells surrounding this particular cell
        """
        x = cell.x
        y = cell.y

        cell.neighborhood = []
        cell.neighborhood.append(self.grid[x - 1][y])  # up
        cell.neighborhood.append(self.grid[x + 1][y])  # down
        cell.neighborhood.append(self.grid[x][y + 1])  # right
        cell.neighborhood.append(self.grid[x][y - 1])  # left

    def run(self):
        """
        this method runs through the grid and determines the changes to be made for the next generation
        """

        for c in self.cells:
            if isinstance(c, ConwayCell) == True:
                self.Conway_neighborhood(c)
            elif isinstance(c, FredkinCell) == True:
                self.Fredkin_neighborhood(c)
            c.outcome()

        for c in self.cells:
            if c.need_switch == True:
                c.switch()

        for c in self.cells:
            if isinstance(c, FredkinCell) and c.convert == True:
                self.cells.remove(c)
                x = c.x
                y = c.y
                c = ConwayCell(x, y)
                c.is_alive = True
                self.grid[x][y] = c
                self.Conway_neighborhood(c)
                self.cells.append(c)

        self.generation += 1


class AbstractCell():
    """
    class that both ConwayCell and FredkinCell feed from.
    """

    def __init__(self, x, y):
        self.is_alive = False
        self.neighborhood = []
        self.neighbors = 0
        self.need_switch = False
        self.x = x
        self.y = y


class ConwayCell(AbstractCell):
    """
    Conway cell has 8 neighbors
    Conway cell will switch from dead to alive if there are exactly 3 alive cells in its neighborhood
    anything else and the cell will stay dead or become dead.
    """

    def __init__(self, x, y):
        AbstractCell.__init__(self, x, y)

    def __str__(self):
        if self.is_alive == True:
            output = "*"
        else:
            output = "."

        return output

    def outcome(self):
        """
        determines the outcome of the cell by observing the neighborhood and calculating using the cells' rules
		whether cell switches or not
		"""

        self.neighbors = 0
        for cell in self.neighborhood:
            if type(cell) != str and (cell.is_alive == True):
                self.neighbors += 1

        if self.is_alive == True and (self.neighbors > 3 or self.neighbors < 2):
            self.need_switch = True

        elif self.is_alive == False and self.neighbors == 3:
            self.need_switch = True

        else:
            self.need_switch = False

    def switch(self):
        """
        switches a creature from dead to alive or alive to dead
        """
        if self.is_alive == True:
            self.is_alive = False
            self.age = 0
        else:
            self.is_alive = True

        self.need_switch = False


class FredkinCell(AbstractCell):
    """
    Fredkin cell has 4 neighbors up, down, left, and right.
    A Fredkin cell becomes alive if there are 1 or 3 alive neighbors
    any other amount of alive neighbors will cause the cell to die
    if a Fredkin cell lives to age 2, it becomes a Conway cell
    """

    def __init__(self, x, y):
        AbstractCell.__init__(self, x, y)
        self.age = 0
        self.convert = False

    def __str__(self):
        if self.is_alive == True:
            self.output = str(self.age)
        else:
            self.output = "-"

        return self.output

    def switch(self):
        """
        switches a creature from dead to alive or alive to dead
        """
        if self.is_alive == True:
            self.is_alive = False
            self.output = "-"
            self.age = 0
        else:
            self.is_alive = True
            self.output = str(self.age)

        self.need_switch = False

    def outcome(self):
        '''
		determines the outcome of the cell by observing the neighborhood and calculating using the cells' rules
		whether cell switches or not
		'''

        self.neighbors = 0
        for cell in self.neighborhood:
            if (type(cell) is not str) and (cell.is_alive is True):
                self.neighbors += 1
        if self.age == 2:
            self.convert = True
        if self.is_alive is True:
            self.age += 1
        if (self.neighbors in [1,3]) and self.is_alive is False:
            self.need_switch = True
        elif (self.neighbors in [0,2,4]) and self.is_alive is True:
            self.need_switch = True
        else:
            self.need_switch = False





