# Drugpedia
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![Python application](https://github.com/parismita/Drugpedia/actions/workflows/python-app.yml/badge.svg)](https://github.com/parismita/Drugpedia/actions/workflows/python-app.yml)



# Introduction
This project is developed by Parismita Das (22M0815) and Vaibhav Singh (22M0827). Our aim is to implement a platform where a user can find all the details related to the prescribed medicine and its ingredient compositions and their potential roles. This project is starting off as an assignment to the course CS699 Software Lab, guided by Prof. Bhaskar Raman, from Indian Institute of Technology, Bombay. 


Note: The project report and proposal for this project is inside [documentation](https://github.com/parismita/Drugpedia/blob/main/documentation/report.pdf) folder


# Instalation guidelines
- clone the repo using `git clone https://github.com/parismita/Drugpedia.git`
- run `make setup` to install the python package
- goto the project directory and create `.env` file
- if you want to connect to postgres database put 
`USER=postgres` `HOST=localhost` `PASS=yourpassword` `DB=drugpedia` `POST=5432`,
where postgres is the default username, you can put your username here and write host and port of your postgres server and the database you want to connect with.
- if you dont have the database ready, you can make one using this command in psql `CREATE DATABASE drugpedia;`
- to create the required tables run `localhost:8080/create` API in your browser 
- to start the server goto the project directory and run `make`
- Now we have started our server and ready to use the website.


# Dependancies
The python dependencies are mentioned in [requirements.txt](https://github.com/parismita/Drugpedia/blob/main/requirements.txt). 

# Developer guidelines
The detailed description of of code structure and the methods are provided [Here](https://github.com/parismita/Drugpedia/blob/main/developer.md)

# Contribution guidelines
Welcome to Drugpedia and thank you for your interest in this project!!
Here are some guidelines to help you get onboard and some rules which we follow.

## How to Contribute?
To find something to contribute to, please checkout our issue tracker, we actively maintain the list of todos as well as bugs. If you are new, you may look for the labels such as "good first issue" or "easy issue".

You may raise an issue, if you want to add new feature, found new bugs or have any questions, with labels as mentioned in the issue tracker.

To submit to an issue, here are some guildelines and rules:
- Before submitting any PR, please mention on the issue that you are working on this particular task so that we know you are working on it.
- During PR, please mention the issue number in description so that we know which issue that PR belong to.
- Always create your own branch while working on something.
- Branch name format: \<author\>/<branch_type>/\<module\>, eg: parismita/feature/init or parismita/bug/user_login
- Never merge your own commit without review check and github action success, into the main branch
- Please, Don't edit/create files directly to main branch without PRs
- To Review a PR, please Squash and Merge while merging any PR, after the GitHub Actions are passing :)
- All Communications to be done via Issue Tracker

## Good Practices 
- Please ensure that all of your code follows PEP8 format for python.
- Please make sure your code is well tested
- Please give descriptive message while comitting and on PRs

Thank you thats all!! Congratulations on your first contrib <3

# Todos
- Mentioned in Issue Tracker

