# ---------------------------
# project repos/cs313e-life/TestLife.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# ---------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Life import Life, AbstractCell, ConwayCell, FredkinCell, reader

# -----------
# TestLife
# -----------

class TestLife (TestCase) :

    def test_identify_1(self):
        grid = [[".",".",".",".","."],[".","*","-","0","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(len(life.cells),25)

    def test_identify_2(self):
        grid = [[".","*","-","0","."],[".",".",".",".","."],[".",".","0",".","."],["*",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(len(life.cells),20)

    def test_identify_3(self):
        grid = [[".",".",".",".","."],[".",".","0",".","."],["*",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(len(life.cells),15)

    def test_identify_4(self):
        grid = [[".",".","0",".","."],["*",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(len(life.cells),10)
    def test_identify_5(self):
        grid = [["*",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(len(life.cells),5)
    def test_identify_6(self):
        grid = [["*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(len(life.cells),1)

    def test_cell_count_1(self):
        grid = [[".",".",".",".","."],[".","*","-","0","."],[".","0","*",".","."],[".",".",".",".","."],[".",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(life.cell_count(), 2)

    def test_cell_count_2(self):
        grid = [[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.remove_buffer()
        self.assertEqual(life.cell_count(), 0)
        self.assertEqual(life.__str__(),".....\n.....\n.....\n.....\n.....\n")

    def test_cell_count_3(self):
        grid = [["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(life.cell_count(), 25)

    def test_cell_count_4(self):
        grid = [["*", "*", ".", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(life.cell_count(), 24)

    def test_cell_count_5(self):
        grid = [["*", "*", ".", ".", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(life.cell_count(), 23)

    def test_cell_count_6(self):
        grid = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        self.assertEqual(life.cell_count(), 20)

    def test_remove_buffer_1(self):
        grid = [["*","*", "*"],["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.remove_buffer()

        self.assertEqual(life.__str__(), "***\n***\n***\n***\n")

    def test_remove_buffer_2(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.remove_buffer()

        self.assertEqual(life.__str__(), "***\n***\n***\n")
    def test_remove_buffer_3(self):
        grid = [["*","*"],["*", "*"], ["*", "*"], ["*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.remove_buffer()

        self.assertEqual(life.__str__(), "**\n**\n**\n**\n")

    def test_Conway_neighborhood_1(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        cell = grid[2][2]
        life.Conway_neighborhood(cell)
        self.assertEqual(len(cell.neighborhood), 8)

    def test_Conway_neighborhood_2(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        cell = grid[2][3]
        life.Conway_neighborhood(cell)
        self.assertEqual(len(cell.neighborhood), 8)
    def test_Conway_neighborhood_3(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        cell = grid[1][2]
        life.Conway_neighborhood(cell)
        self.assertEqual(len(cell.neighborhood), 8)

    def test_Fredkin_neighborhood_1(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        cell = life.grid[1][2]
        life.Fredkin_neighborhood(cell)
        self.assertEqual(len(cell.neighborhood), 4)

    def test_Fredkin_neighborhood_2(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        cell = life.grid[2][2]
        life.Fredkin_neighborhood(cell)
        self.assertEqual(len(cell.neighborhood), 4)
    def test_Fredkin_neighborhood_3(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        cell = life.grid[3][2]
        life.Fredkin_neighborhood(cell)
        self.assertEqual(len(cell.neighborhood), 4)

    def test_run_1(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.run()
        self.assertEqual(life.generation, 1)

    def test_run_2(self):
        grid = [["*", "*", "*"],["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.run()
        self.assertEqual(life.generation, 1)
    def test_run_3(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        for i in range(4):
            life.run()
        self.assertEqual(life.generation, 4)
    def test_run_4(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        life.run()
        life.run()
        life.run()
        self.assertEqual(life.generation, 3)
    def test_run_5(self):
        grid = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        for i in range(6):
            life.run()
        self.assertEqual(life.generation, 6)
    def test_run_6(self):
        grid = [["*", "*", "*"], ["*", "0", "*"], ["*", "*", "*"]]
        life = Life(grid)
        life.add_buffer()
        life.identify()
        for i in range(4):
            life.run()
        self.assertEqual(life.generation, 4)


    def test_reader_1(self):
        raw_input = StringIO("4\n12\n............\n............\n............\n............\n")
        self.assertEqual(reader(raw_input), [[[".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".","."]]])

    def test_reader_2(self):
        raw_input = StringIO("3\n13\n.............\n.............\n.............\n")
        self.assertEqual(reader(raw_input), [[[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]]])

    def test_reader_3(self):
        raw_input = StringIO("2\n13\n.............\n.............\n\n2\n13\n.............\n.............\n")
        self.assertEqual(reader(raw_input), [[[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]], [[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]]])
    def test_reader_4(self):
        raw_input = StringIO("4\n13\n.............\n.............\n.............\n.............\n")
        self.assertEqual(reader(raw_input), [[[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]]])

    def test_reader_5(self):
        raw_input = StringIO("3\n11\n...........\n...........\n...........\n")
        self.assertEqual(reader(raw_input), [[[".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".","."]]])

    def test_reader_6(self):
        raw_input = StringIO("2\n13\n.............\n.............\n\n2\n13\n.............\n.............\n\n2\n13\n.............\n.............\n")
        self.assertEqual(reader(raw_input), [[[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]], [[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]],[[".",".",".",".",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".",".",".",".","."]]])


main()