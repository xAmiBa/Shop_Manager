# Shop Manager Application

This repository contains a Python application for managing a shop, demonstrating various programming concepts and skills. As a junior software developer, I have focused on implementing the application using Object-Oriented Programming (OOP) principles, Test-Driven Development (TDD) using pytest, and applying software engineering principles. The application involves parent-child classes, model and repository classes, and interaction with a PostgreSQL database using the psycopg library.

## Features and Concepts

### Object-Oriented Programming (OOP)
- Utilized OOP principles to structure the codebase effectively.
- Created classes such as `Application`, `ItemRepository`, `OrderRepository`, `Item`, and `Order` to encapsulate data and behavior.

### Test-Driven Development (TDD) with pytest
- Implemented comprehensive unit tests using pytest to ensure the functionality and correctness of the application.
- Wrote tests for the `OrderRepository` and `ItemRepository` classes, covering various use cases and functionalities.

### Model and Repository Classes
- Designed model classes (`Item` and `Order`) to represent data entities with attributes and behavior specific to each.
- Implemented repository classes (`ItemRepository` and `OrderRepository`) to handle data retrieval, creation, and interaction with the database.

### Working with Databases and SQL
- Integrated PostgreSQL database using the psycopg library for data storage and retrieval.
- Executed SQL queries for creating, seeding, and interacting with the database, ensuring data integrity and consistency.

## Running the Application

To run the shop manager application, follow these steps:
1. Ensure you have PostgreSQL installed and running on your machine.
2. Create a PostgreSQL database named "shop_manager".
3. Execute the SQL schema and seed script using the command `psql -d shop_manager -f seeds/shop_manager.sql`.
4. Run the application using the command `python app.py`.

## Running Tests

To run the tests for the application, follow these steps:
1. Ensure you have the required dependencies installed by running `pip install -r requirements.txt`.
2. Run the tests using the command `pytest`.

## Acknowledgements

This project showcases my understanding and application of software development principles, particularly in the context of a shop management application. It reflects my ability to work with databases, design effective class hierarchies, and implement robust unit tests. I am continuously working on improving my skills and exploring new concepts.