PYTHON=/usr/bin/python3
all: test
test:
	${PYTHON} -m gui.py
	python3 create_table.py