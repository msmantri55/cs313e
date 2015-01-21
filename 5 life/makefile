all:

Life.html: Life.py
	pydoc3 -w Life

Life.log:
	git log > Life.log

Runlife.out: Runlife.py RunLife.in
	Runlife.py < RunLife.in > Runlife.out

Runlife.tmp: Runlife.py RunLife.in
	Runlife.py < RunLife.in > Runlife.tmp
	diff Runlife.tmp Runlife.out

TestLife.out: TestLife.py
	coverage3 run    --branch TestLife.py >  TestLife.out 2>&1
	coverage3 report -m                   >> TestLife.out

clean:
	rm -f .coverage
	rm -f *.pyc
	rm -f RunLife.tmp
	rm -f TestLife.out
	rm -rf __pycache__
