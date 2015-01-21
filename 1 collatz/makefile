all:

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f RunCollatz.out
	rm -f RunCollatz.tmp
	rm -f TestCollatz.out
	rm -rf __pycache__

scrub:
	make --no-print-directory clean
	rm -f Collatz.html
	rm -f Collatz.log

Collatz.html: Collatz.py
	pydoc3 -w Collatz

Collatz.log:
	git log > Collatz.log

RunCollatz.out: RunCollatz.py RunCollatz.in
	RunCollatz.py < RunCollatz.in > RunCollatz.out

RunCollatz.tmp: RunCollatz.py RunCollatz.in RunCollatz.out
	RunCollatz.py < RunCollatz.in > RunCollatz.tmp
	diff RunCollatz.out RunCollatz.tmp

TestCollatz.out: TestCollatz.py
	coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1
	coverage3 report -m                   >> TestCollatz.out
