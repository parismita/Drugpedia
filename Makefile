all: lint run test
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
	autopep8 --in-place src/utils/scraping.py
	flake8 src/utils/scraping.py
	python3 src/utils/scraping.py
    
setup: requirements.txt
	pip3 install -r requirements.txt
    
.PHONY: clean

clean:
	rm -rf __pycache__
