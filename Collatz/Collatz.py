#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_cache
# ------------
"""
def collatz_cache (i, j):
"""

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    if i > j: #Here the program takes into account an input with i being larger than j (which is not illegal for input).
        i_place_holder = i
        i = j
        j = i_place_holder
        
    if ((j//2)+1) > i: #This is the range reducing optimization. Used to eliminate parts of the range when numbers exist in the range that have a lower cycle length
        i = ((j//2)+1)

    max_cycle_length = 0
    
    for num in range(i,j+1): #This for loop runs the traditional Collatz Conjecture.
        
        assert num > 0
        c = 1
        while num > 1 :
            if (num % 2) == 0 :
                num = (num // 2)
                c += 1
            else :
                num = num + (num // 2) + 1
                c += 2
        assert c > 0
        if c > max_cycle_length:
            max_cycle_length = c

    return max_cycle_length
    

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    
    cache_dictionary = {} #cache implemented in the form of a dictionary
    
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        
        key = "{0} {1}".format(i, j) #This variable creates a string form of the input that is used to check for an existing key.
        if cache_dictionary.get(key) != None:
            v = cache_dictionary.get(key)
            
        else:

            v = collatz_eval(i, j)
            cache_dictionary[key] = "{0}".format(v) #if the string in variable key does not exist as a key in the cache_dictionary, this line will add it with the value as the max_cycle_length
            

        collatz_print(w, i, j, v)

