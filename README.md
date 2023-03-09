# Brett's Pets CLI
Ari Marz
Brett DeBear
Diana Lin
Ja'Vonn Williams

## Learning Goals
- Explore the structure of a simple Python CLI.
- Evaluate a simple Python CLI using the Phase 3 Project Rubric.
***

## Introduction
This CLI makes use of SQLAlchemy, Alembic, and Python fundamentals to allow
users to shop for pets in a series of ten pet stores. It can be executed via command line from the `lib/`
directory with `python cli.py` or `./cli.py`.

## Deliverables
- Used two external libraries: Faker (used to generate fake names and fake numbers to simplify the creation of databases) and Rich (which generates tables and can change text colors within a CLI.)

- Makes use of three tables -- Stores that includes a list of ten store names along with ten random addresses generated through the use of Faker; Pets, which has a list of 50 pet breeds along with the quantity of pets available at each store, and a randomly generated price; Pet-Item-Stores, which is a table that correlates each store with a pet. Each of our 10 individual stores contains different pets.

- Used SQLAlchemy and Object-Relational-Mapping in models.py in order to generate a usable CLI (Command Line Interface)

- When entering the CLI, you'll see different fonts and colors (generated using the the Python library Rich). Which each message prompt, a table or a question pops up and user will be able to get a response.

- Use Alembic to manage migrations of databases throughout the project

## Using the CLI
- First, cd into lib/db then run python cli.py

- There will be a welcome line that welcomes the user to Brett's Pets, followed by a table of the available stores you can choose from. Please enter a number between 1 and 10 and a list of pets that correlates to each store will appear.

- User has the option to add multiple pets to cart. After confirming that you are ready to check out, the total price of all the pets purchased will appear, and now you have a few new pets!
Our wireframe link is here: https://www.figma.com/file/HhuPRRkTUFGYZ8fLV8AcBy/Untitled?node-id=0%3A1&t=jwwjY3v8uL0TIcBV-1

