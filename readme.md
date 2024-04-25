
  

## Class-Database: A Simple SQLite3 Project
This project provides a basic database management system for storing student information. It utilizes the SQLite3 library to create and interact with a database named "class.db".
 1. Features:
	- Creates a table named "Alunos" (Students) upon first execution, containing columns for:
		- Nome (Name) - Text

		- Curso (Course) - Text

		- Matrícula (Registration Number) - Integer

2. Usage:

	 - Run the script (`python main.py`).

		The script will automatically connect to "class.db" (creating it if it doesn't exist) and check for the "Alunos" table.

		If the table is absent, it will be created.

3. You can:
	- Insert student data
	- Delete entries

4. Dependencies:
	- Python 3 with sqlite3 library (usually included by default)

5. Additional Notes:
	- This is a basic project to demonstrate database creation and connection using SQLite3.
