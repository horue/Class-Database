
Class-Database: A Simple SQLite3 Project
About:

This project provides a basic database management system for storing student information. It utilizes the SQLite3 library to create and interact with a database named "class.db".

Features:

Creates a table named "Alunos" (Students) upon first execution, containing columns for:
Nome (Name) - Text
Curso (Course) - Text
Matrícula (Registration Number) - Integer
Usage:

Run the script (python main.py).
The script will automatically connect to "class.db" (creating it if it doesn't exist) and check for the "Alunos" table.
If the table is absent, it will be created.
You can then develop further functionalities to interact with the database, such as:
Inserting student data
Updating existing information
Retrieving student records
Deleting entries (optional)
Dependencies:

Python 3 with sqlite3 library (usually included by default)
Additional Notes:

This is a basic project to demonstrate database creation and connection using SQLite3.
You can extend it to incorporate various features for managing student information.