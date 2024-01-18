

Project badge
Python - Object-relational mapping -1

    Master
    By: Guillaume, CTO at Holberton School
    Weight: 1
    Your score will be updated once you launch the project review.
    Project will start Jan 13, 2024 12:00 AM, must end by Jan 18, 2024 11:59 PM

Before you start…

Please make sure your MySQL server is in 5.7 -> How to install MySQL 5.7 in Ubuntu 14.04
Background Context

In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

With an ORM:

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.
Resources

Read or watch:

    Object-relational mappers
    mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
    How to connect MySQL database in Python
    MySQLdb tutorial
    SQLAlchemy tutorial
    SQLAlchemy
    mysqlclient/MySQLdb
    Introduction to SQLAlchemy
    Flask SQLAlchemy
    10 common stumbling blocks for SQLAlchemy newbies
    Python SQLAlchemy Cheatsheet
    SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
    SQLAlchemy Tutorial

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    Why Python programming is awesome
    How to connect to a MySQL database from a Python script
    How to SELECT rows in a MySQL table from a Python script
    How to INSERT rows in a MySQL table from a Python script
    What ORM means
    How to map a Python Class to a MySQL table

Requirements
General

    Recommended editors: Visual studio code
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
    Your files will be executed with MySQLdb version 1.3.x
    Your files will be executed with SQLAlchemy version 1.2.x
    All your files should end with a new line
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the PEP 8 style (version 1.7.*)
    The length of your files will be tested using wc
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    You are not allowed to use execute with sqlalchemy

More Info
Install MySQLdb module version 1.3.x

For installing MySQLdb, you need to have MySQL installed: How to install MySQL 5.7 in Ubuntu 14.04

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==1.3.10
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.10'

Install SQLAlchemy module version 1.2.x

$ pip3 install SQLAlchemy==1.2.5
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.5'

Also, you can have this warning message:

/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  

You can ignore it.
Introductory session for this project
Live learning session for this project
Tasks
0. Get all states
mandatory

Write a script that lists all states from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ python3 0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$ 

No test cases needed



Click here to show/hide hint
To be able to solve this task correctly, you will need to know how to use and also you would have to pay particular attention to how the results is to be printed out.

Repo:

    GitHub repository: alx_python
    Directory: python-object_relational_mapping
    File: 0-select_states.py

0/9 pts
1. Filter states
mandatory

Write a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/$ 

No test cases needed

Repo:

    GitHub repository: alx_python
    Directory: python-object_relational_mapping
    File: 1-filter_states.py

0/10 pts
2. Filter states by user input
mandatory

Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

    Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    You must use format to create the SQL query with the user input
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$ 

No test cases needed

Repo:

    GitHub repository: alx_python
    Directory: python-object_relational_mapping
    File: 2-my_filter_states.py

0/12 pts
3. SQL Injection...
mandatory

Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?

guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
(2, 'Arizona')
guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
guillaume@ubuntu:~/$ 

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

    Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

guillaume@ubuntu:~/$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/$ 

No test cases needed



Click here to show/hide hint
To be able to solve this task correctly, you will need to understand in SQL while using MySQLdb.

Repo:

    GitHub repository: alx_python
    Directory: python-object_relational_mapping
    File: 3-my_safe_filter_states.py

0/10 pts
4. Cities by states
mandatory

Write a script that lists all cities from the database hbtn_0e_4_usa

    Your script should take 3 arguments: mysql username, mysql password and database name
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
    Results must be sorted in ascending order by cities.id
    You can use only execute() once
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");

guillaume@ubuntu:~/$ cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/$ ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
guillaume@ubuntu:~/$ 

No test cases needed

Repo:

    GitHub repository: alx_python
    Directory: python-object_relational_mapping
    File: 4-cities_by_state.py

0/9 pts
Score
Project badge

Your score will be updated once you launch the project review.

Please review all the tasks before you start the peer review.
Previous project
Copyright © 2024 ALX, All rights reserved.
