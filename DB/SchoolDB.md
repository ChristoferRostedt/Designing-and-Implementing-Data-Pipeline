## Creating Database
```
cd DB
sqlite3 school.db
.table
CREATE TABLE Task (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT);
.table
SELECT * FROM Task;
CREATE TABLE CourseAssignment(id INTEGER PRIMARY KEY AUTOINCREMENT, id_task INTEGER NOT NULL, id_course INTEGER NOT NULL);
CREATE TABLE Course (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT);
CREATE TABLE TaskCompletion (id INTEGER PRIMARY KEY AUTOINCREMENT, id_courseAssignment INTEGER NOT NULL, id_student INTEGER NOT NULL, time TEXT);
CREATE TABLE Student (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, birthday TEXT, major TEXT);
CREATE TABLE CreditS (id INTEGER PRIMARY KEY AUTOINCREMENT, id_course INTEGER NOT NULL, id_student INTEGER NOT NULL, date TEXT NOT NULL, grade TEXT, credits INTEGER);

PRAGMA table_info(Student);
0|id|INTEGER|0||1
1|name|TEXT|1||0
2|birthday|TEXT|0||0
3|major|TEXT|0||0
sqlite> INSERT INTO Task (name, description) VALUES('Essay', 'Short written assignment'),('Quit', 'Multiple-choice Quiz');
sqlite> SELECT * FROM Course
INSERT INTO Student (name, birthday, major) VALUES('Alex Student', '2000-05-15', 'Computer Science'),('Blake Student', '2001-08-22', 'Computer Science'),('Casey Learner', '1999-11-03', 'Information Tech');
INSERT INTO Credits (id_course, id_student, date, grade, credits) VALUES(1, 1, date('now'), '5', 5),(1, 2, date('now'), '5', 5),(2, 3, date('now'), '5', 6),(2, 4, date('now'), '5', 6);
INSERT INTO Course (id, name, description) VALUES(1, 'Data Pipelines', 'Intro to building and operating data pipelines'),(2,'Embedded Systems', 'Intro to embedded software and hardware basics');
```