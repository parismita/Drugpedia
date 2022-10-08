all: lint run test
build: lint test clean

run: setup
	python3 main.py

test: setup
	python3 tests/test.py
	
lint: setup autopep
	flake8 *.py
	
autopep: setup
	autopep8 --in-place *.py
    
setup: requirements.txt
	pip3 install -r requirements.txt
    
.PHONY: clean

clean:
	rm -rf __pycache__
