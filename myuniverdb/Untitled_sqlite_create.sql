CREATE TABLE Staff (
	id integer PRIMARY KEY AUTOINCREMENT,
	first_name varchar,
	last_name varchar
);

CREATE TABLE Student (
	id integer PRIMARY KEY AUTOINCREMENT,
	first_name varchar,
	last_name varchar,
	group_id integer
);

CREATE TABLE FGroup (
	id binary PRIMARY KEY AUTOINCREMENT,
	number integer PRIMARY KEY AUTOINCREMENT,
	faculty_id integer
);

CREATE TABLE Faculty (
	id integer PRIMARY KEY AUTOINCREMENT,
	name varchar
);

CREATE TABLE Exam_record (
	date varchar,
	grade integer,
	exam_id integer,
	student_id integer
);

CREATE TABLE Exam (
	id integer PRIMARY KEY AUTOINCREMENT,
	discipline varchar,
	staff_id integer
);

CREATE TABLE HR_record (
	position varchar,
	staff_id integer,
	faculty_id integer
);

