import psycopg2
import json

with open('year_0.txt') as data_file:
    data0 = json.load(data_file)
with open('year_1.txt') as data_file:
    data1 = json.load(data_file)
with open('year_2.txt') as data_file:
    data2 = json.load(data_file)
with open('year_3.txt') as data_file:
    data3 = json.load(data_file)


conn = psycopg2.connect("dbname='postgres' user='' host='localhost' password=''")
cur = conn.cursor()
cur.execute("set SEARCH_PATH To UofT;")


def add_course(id, course_name, course_type,conn):
    cur = conn.cursor()
    cur.execute("insert into course VALUES ({}, '{}', '{}');".format(id, course_name, course_type))
    conn.commit()


def add_section(sec_id, course_id, sec_code,teachingMethod, control, conn):
    cur = conn.cursor()
    cur.execute("insert into section VALUES ({}, '{}', '{}','{}');".format(sec_id, sec_code, teachingMethod, control))
    cur.execute("insert into course_section VALUES ('{}','{}')".format(course_id, sec_id))
    conn.commit()


def sec_add_time(sec_id, day, start, end, conn):
    cur = conn.cursor()
    if day == 'MO':
        td = 1
    elif day == 'TU':
        td = 2
    elif day == 'WE':
        td = 3
    elif day == 'TH':
        td = 4
    elif day == 'FR':
        td = 5
    else:
        return False
    cur.execute("insert into time VALUES ({}, {}, '{}', '{}');".format(sec_id, td, start, end))
    conn.commit()

count_i = 0
count_j = 0
def load(data, conn):
    global count_j
    global count_i
    for i in data:
        count_i += 1
        add_course(count_i, i[:6], i[9], conn)
        for j in data[i]['meetings']:
            count_j += 1
            if add_section(count_j, count_i, j, data[i]['meetings'][j]['teachingMethod'],data[i]['meetings'][j]['enrollmentIndicator'],conn) == False:
                break
            for k in data[i]['meetings'][j]['schedule']:
                schedule = data[i]['meetings'][j]['schedule'][k]
                sec_add_time(count_j, schedule['meetingDay'], schedule['meetingStartTime'], schedule['meetingEndTime'],conn)


load(data0, conn)
load(data1, conn)
load(data2, conn)
load(data3, conn)


