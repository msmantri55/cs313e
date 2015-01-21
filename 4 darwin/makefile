all:

Darwin.html: Darwin.py
	pydoc3 -w Darwin

Darwin.log:
	git log > Darwin.log

RunDarwin.out: RunDarwin.py
	RunDarwin.py > RunDarwin.out

RunDarwin.tmp: RunDarwin.py
	RunDarwin.py > RunDarwin.tmp
	diff RunDarwin.tmp RunDarwin.out

TestDarwin.out: TestDarwin.py
	coverage3 run    --branch TestDarwin.py >  TestDarwin.out 2>&1
	coverage3 report -m                     >> TestDarwin.out

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f RunDarwin.tmp
	rm -f TestDarwin.out
	rm -rf __pycache__
