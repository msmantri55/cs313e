# ---------------------------
# project repos/cs313e-voting/RunVoting.py
# CS313E - Elements of Software Design
# Parth H. Patel
# php274
# ---------------------------

# -------
# imports
# -------

#simport sys

#from Voting import voting_solve

# ----
# main
# ----

"""
voting_solve(sys.stdin, sys.stdout)
"""

import sys
from Voting import read, Election

def main():
	numElections = read(sys.stdin)

	while numElections > 0:
		election = Election()
		election.read(sys.stdin)
		election.evaluate()
		print (election)

		numElections -= 1

if __name__ == '__main__':
	main()