DROP SCHEMA IF EXISTS UofT CASCADE;
CREATE SCHEMA UofT;
set SEARCH_PATH To UofT;

CREATE TABLE course(
  id INT PRIMARY KEY,
  course_code VARCHAR(10) NOT NULL ,
  course_type VARCHAR(1) NOT NULL
);

CREATE TABLE section(
  id INT PRIMARY KEY ,
  section_name VARCHAR(8),
  section_type varchar(3),
  enrol_control varchar(5)
);

CREATE TABLE course_section(
  course_id int REFERENCES course(id),
  section_id int REFERENCES section(id),
  PRIMARY KEY(course_id, section_id)
);

CREATE TABLE time(
  section_id int REFERENCES section(id),
  day int,
  starttime TIME,
  endtime TIME
);

