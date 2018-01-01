from timetable import *
import psycopg2
import pprint

def getCourse(courseName, courseType):
    conn = psycopg2.connect("dbname='postgres' user='' host='localhost' password=''")
    cur = conn.cursor()
    cur.execute("set SEARCH_PATH To UofT;")
    cur.execute("SELECT course_code,course_type,section_type, section_name, day, starttime, endtime"
                " from course, section, course_section,time WHERE "
                "course_code = '{}' and section.id = course_section.section"
                "_id and course.id = course_section.course_id and"
                " time.section_id = section.id AND "
                "(enrol_control = 'P' or enrol_control = 'E' or enrol_control = 'null') AND "
                "course_type = '{}';".format(courseName, courseType))
    rows = cur.fetchall()
    # for i in rows:
    #     print(i)
    course = Course(rows[0][0], rows[0][1])
    current_section = None
    current_section_name = None
    for meeting in rows:
        if meeting[3] != current_section_name:
            current_section_name = meeting[3]
            current_section = Section(meeting[0], current_section_name)
            current_section.add_time(meeting[4], meeting[5],meeting[6])
            if meeting[2] == 'LEC':
                course.add_sec(current_section)
            else:
                course.add_tut(current_section)
        else:
            current_section.add_time(meeting[4], meeting[5],meeting[6])
    return course

T = TimeTable()
CSC358 = getCourse("CSC358", "S")
a = add_course([T], CSC358)
CSC369 = getCourse("CSC369", "S")
b = add_course(a, CSC369)
ECO102 = getCourse("ECO102", "S")
c = add_course(b,ECO102)
# for i in b:
#     pprint.pprint(i)
for i in c:
    i.time_for_eat()
    i.not_continue()
    i.not_morning()
c.sort(key=lambda x: x.score, reverse=True)
for i in c[0:10]:
    print(i.secs)