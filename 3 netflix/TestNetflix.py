# ---------------------------
# project repos/cs313e-netflix/TestNetflix.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# Daniel Croy
# dsc986
# ---------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_solve, rmse

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    
    # ----
    # RMSE
    # ----

    def test_rmse_1 (self) :
        w = StringIO()
        rmse(w, [1, 5, 3],[1.5, 5, 2] )
        self.assertEqual(w.getvalue(), "RMSE: 0.65")
        self.assertNotEqual(w.getvalue(), 1)

    def test_rmse_2 (self) :
        w = StringIO()
        rmse(w, [4, 3, 2], [3.7, 2.9, 1.2])
        self.assertEqual(w.getvalue(), "RMSE: 0.50")
        self.assertNotEqual(w.getvalue(), 1)

    def test_rmse_3 (self) :
        w = StringIO()
        rmse(w, [2, 3, 5], [2.9, 1.7, 4.1])
        self.assertEqual(w.getvalue(), "RMSE: 1.05")
        self.assertNotEqual(w.getvalue(), 1)

    # -----
    # netflix_solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("15826:\n414332\n418752\n300388\n1151430\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "RMSE: 0.63")
        self.assertNotEqual(w.getvalue(), "15826:\n414332\n418752\n300388\n1151430\n")

    def test_solve_2 (self) :
        r = StringIO("15830:\n798181\n688738\n1589443\n415206\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "RMSE: 0.99")
        self.assertNotEqual(w.getvalue(), "15830:\n798181\n688738\n1589443\n415206\n")

    def test_solve_3 (self) :
        r = StringIO("15832:\n1462949\n2246845\n2052636\n2306573\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "RMSE: 1.08")
        self.assertNotEqual(w.getvalue(), "15830:\n798181\n688738\n1589443\n415206\n")

# ----
# main
# ----

main()