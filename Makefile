all: lint run test

run: setup
	python3 main.py

test: setup
	python3 tests/test.py
	
lint: setup autopep
	flake8 main.py
	
autopep: setup
	autopep8 --in-place main.py
    
setup: requirements.txt
	pip3 install -r requirements.txt
    
.PHONY: clean

clean:
	rm -rf __pycache__
