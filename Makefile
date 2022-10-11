all: run
build: lint test clean

run: setup
	python3 main.py

test: setup
	python3 tests/test.py

#not all files are getting checked - bug
lint: setup autopep
	flake8 *.py
	
autopep: setup
	autopep8 --in-place *.py

#testing scrap util
scrap: setup
	autopep8 --in-place src/services/medservice.py
	flake8 src/services/medservice.py
	python3 src/services/medservice.py
    
setup: requirements.txt
	pip3 install -r requirements.txt
    
.PHONY: clean

clean:
	rm -rf __pycache__
