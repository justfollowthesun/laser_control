import sys
import os
import random

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def CreateEmployeeData() -> None:
    """
    Create sample database for project.
    Function demonstrates how to connect to a database, create queries, and
    create tables and records in those tables.
    """

    # Create connection to db. If db file does not exist,
    # a new db file will be created.

    # db.setDatabaseName(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_db.db"))
    # Create database connection.

    # Можно получить список драйверов вызвав
    # QSqlDatabase.drivers() -> List[str]

    db = QSqlDatabase('QPSQL')
    db.setHostName('localhost')
    db.setDatabaseName('pyqt5_test_db')
    db.setUserName('postgres')
    db.setPassword('ghbdtnlfnf')
    query = QSqlQuery(db=db)

    if not db.open():
        print('cannot open database')
        sys.exit(1) # Error code 1 - signifies error
    else:
        pass
        # if query.exec_("CREATE DATABASE pyqt5_test_db"):
        #     print('done')
        # else:
        #     print(query.lastError().text())


    # Positional binding to insert records into the database

    # Add the values to the query to be inserted in countries

     # Create the second table, countries

    countries = {"USA": 1, "India": 2, "China": 3, "France": 4, "Germany": 5}
    country_names = list(countries.keys())
    country_codes = list(countries.values())


    country_query = QSqlQuery(db=db)
    country_query.prepare("INSERT INTO countries (id, country) VALUES (?, ?)")
    for name, id in countries.items():

        country_query.addBindValue(id)
        country_query.addBindValue(name)
        print(country_query.exec_())
        print(query.lastError().text())


    query.prepare("""
                    INSERT INTO accounts (
                        id, employee_id, first_name, last_name,
                        email, department, country_id
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)"""
                )

    first_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Mia",
    "Charlotte", "Amelia", "Evelyn", "Abigail", "Valorie", "Teesha",
    "Jazzmin", "Liam", "Noah", "William", "James", "Logan", "Benjamin",
    "Mason", "Elijah", "Oliver", "Jason", "Lucas", "Michael"]

    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore",
    "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris"]

    employee_ids = random.sample(range(1000, 2500), len(first_names))

    departments = ["Production", "R&D", "Marketing", "HR",
    "Finance", "Engineering", "Managerial"]

    # Add the values to the query to be inserted in accounts
    counter = 0
    for f_name in first_names:
        l_name = last_names.pop()
        email = (l_name + f_name[0]).lower() + "@job.com"
        country_id = random.choice(country_codes)
        dept = random.choice(departments)
        employee_id = employee_ids.pop()
        query.addBindValue(counter)
        query.addBindValue(employee_id)
        query.addBindValue(f_name)
        query.addBindValue(l_name)
        query.addBindValue(email)
        query.addBindValue(dept)
        query.addBindValue(country_id)
        counter += 1
        print(query.exec_())
        print(query.lastError().text())


    print("[INFO] Database successfully created.")
    sys.exit(0)


if __name__ == "__main__":
    CreateEmployeeData()
