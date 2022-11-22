all: lint run
build: lint test clean

run: setup
	python3 main.py

test: setup
	python3 tests/test.py

#not all files are getting checked - bug
lint: setup autopep
	flake8 main.py setup.py
	flake8 src/services
	flake8 src/controllers
	flake8 src/models
	flake8 src/routes
	flake8 src/utils
	
autopep: setup
	autopep8 --in-place main.py setup.py
	autopep8 --in-place --recursive src/services
	autopep8 --in-place --recursive src/controllers
	autopep8 --in-place --recursive src/models
	autopep8 --in-place --recursive src/routes
	autopep8 --in-place --recursive src/utils

#testing scrap util
medscrap: setup
	autopep8 --in-place src/services/medservice.py
	flake8 src/services/medservice.py
	python3 src/services/medservice.py

#testing scrap util
ingscrap: setup
	autopep8 --in-place src/services/ingservice.py
	flake8 src/services/ingservice.py
	python3 src/services/ingservice.py

    
setup: requirements.txt
	pip3 install -r requirements.txt
    
.PHONY: clean

clean:
	rm -rf __pycache__
