#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r    = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        i, j = collatz_read(r)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)
    
        k, l = collatz_read(r)
        self.assertEqual(k, 100)
        self.assertEqual(l, 200)

        m, n = collatz_read(r)
        self.assertEqual(m, 201)
        self.assertEqual(n, 210)
        
        p, q = collatz_read(r)
        self.assertEqual(p, 900)
        self.assertEqual(q, 1000)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)
        self.assertNotEqual(v, 1)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)
        self.assertNotEqual(v, 1)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)
        self.assertNotEqual(v, 1)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)
        self.assertNotEqual(v, 1)
    
    def test_eval_5 (self):
        v = collatz_eval(60, 50)
        self.assertEqual(v, 113)
        
    def test_eval_6 (self):
        v = collatz_eval(23, 22)
        self.assertEqual(v, 16)
        
    def test_eval_7 (self):
        v = collatz_eval(60, 6)
        self.assertEqual(v, 113)
        
    def test_eval_8 (self):
        v = collatz_eval(100, 1000)
        self.assertEqual(v, 179)

    def test_eval_9 (self):
        v = collatz_eval(100, 1000)
        self.assertEqual(v, 179)
        
    def test_eval_10 (self):
        v = collatz_eval(2373, 75)
        self.assertEqual(v, 183)
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")
        self.assertNotEqual(w.getvalue(), "1 10 1\n")
        
    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 2373, 75, 183)
        self.assertEqual(w.getvalue(), "2373 75 183\n")
        self.assertNotEqual(w.getvalue(), "2373 75 1\n")

        
    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 50, 60, 113)
        self.assertEqual(w.getvalue(), "50 60 113\n")
        self.assertNotEqual(w.getvalue(), "50 60 1\n")
    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
        self.assertNotEqual(w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz.py
FFFF..F
======================================================================
FAIL: test_eval_1 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 47, in test_eval_1
    self.assertEqual(v, 20)
AssertionError: 1 != 20

======================================================================
FAIL: test_eval_2 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 51, in test_eval_2
    self.assertEqual(v, 125)
AssertionError: 1 != 125

======================================================================
FAIL: test_eval_3 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 55, in test_eval_3
    self.assertEqual(v, 89)
AssertionError: 1 != 89

======================================================================
FAIL: test_eval_4 (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 59, in test_eval_4
    self.assertEqual(v, 174)
AssertionError: 1 != 174

======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz.py", line 78, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (failures=5)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      0      0    97%   86
----------------------------------------------------------
TOTAL            51      1      6      0    98%
"""
