# Drugpedia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Python application](https://github.com/parismita/Drugpedia/actions/workflows/python-app.yml/badge.svg)](https://github.com/parismita/Drugpedia/actions/workflows/python-app.yml)


# Developer guidelines
Here's the file structure and the modules of this project
- `src` - has the backend and frontend code
  - `controllers` - Rendering the pages and re-directions are written here.
    - `homecontroller.py` - render the main page \
      Consist of the method `index` which renders `index.html` page and `create` which create the tables in postgreSQL if its not already present
    - `ingcontroller.py` - controller for ingredient module \
      Consist of the following methods
      - `details()` - returns the dict consisting the ingredient details: name, precautions, side_effect, url, use
      - `search()` - returns the dict of urls and name
      - `search_ingredient()` - render `search-ingredient.html`
      - `search_ingredient_results()` - render `search-ingredient-results.html`
      - `ingredient_details()` - render `ingredient-details.html`
    - `medcontroller.py` - controller for medicine module \
      Consist of the following methods
      - `details()` - returns the dict consisting the medicine details: name, description, side_effect, url, use
      - `search()` - returns the dict of urls and name
      - `search_results()` - render `search_results.html`
      - `medicine_details()` - render `medicine_details.html`
  - `models` - the SQLAlchemy models for the tables
	  - `medicine.py` - The medicine table's model
    - `ingredient.py` - The ingredient table's model
  - `services` - main logic is written here
    - `medservice.py` - modules for CRUD, search and details of medicine \
      Consist of the following methods
      - `MedSearch(key)` - the module for searching the medicine names, \
        it takes the user input value to be searched as argument and returns the dict of medicine list. \
        It calls two seperate search functions to do webscraping from otc and drugs lists and combine the results into one dataframe.
      - `MedDetails(id, name)` - the module for the medicine summary, \
        it takes the unique url and name to medicine as argument and returns the dict of medicine data. The details for otc and drugs are computed seperately and combined in this function.
      - `OtcDetails(content)` - takes the parsed html as input and returns dict of otc summary 
      - `DrugDetails(content)` - takes the parsed html as input and returns dict of drugs summary 
    - `ingservice.py` - modules for CRUD, search and details of ingredient \
      Consist of the following methods
      - `IngredientDetails(id, name)` - the module for the medicine summary, \
        it takes the unique url and name to medicine as argument and returns the dict of ingredient data.
      - `IngredientSearch(key)` - the module for searching the medicine names, \
        it takes the user input value to be searched as argument and returns the dict of ingredient list.
  - `routes` - routing on given urls
    - `homeroute.py` - main page route
    - `ingroute.py` - ingredient module routes
    - `medroute.py` - medicine module routes
  - `utils` - utility files
	- `initdb.py` - initializing the database here
	  - `create_db()` - creates the postgreSQL tables  
  - `template` - contain the html codes
      - `search-ingredient.html`
      - `search-ingredient-results.html`
      - `ingredient-details.html`
      - `index.html`
      - `search-results.html`
      - `medicine-details.html`
- `test` - For unit testing
  - `test.py` - For unit testing, currently no tests there
- `main.py` - Creating the application, connecting to postgres here.
- `Makefile` - Build and Run the application, linting and installation of dependencies
- `requirement.txt` - The dependencies
- `documentation` - Contains documentation folder


