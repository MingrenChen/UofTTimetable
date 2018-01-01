

class Time:
    def __init__(self, day, start, duration):
        self.day = day
        self.start = start
        self.duration = duration

    def conflict(self, other):
        if self.day != other.day:
            return False
        self_end = self.start + self.duration
        other_end = other.start + other.duration
        if self_end <= other.start:
            return False
        if other_end <= self.start:
            return False
        return True


class Section:
    def __init__(self,course, sec_code):
        self.time = []
        self.sec_code = sec_code
        self.course = course

    def add_time(self, day, start, end):
        s = start.hour
        if end.minute == 30:
            e = end.hour + 1
        else:
            e = end.hour
        self.time.append(Time(day, s, e - s))

    def conflict(self, other):
        for i in self.time:
            for j in other.time:
                if i.conflict(j):
                    return True
        return False

    def __str__(self):
        return self.course + self.sec_code

    def __repr__(self):
        return self.course + self.sec_code


class Course:
    """
    a single course. A course has a course code, and several section
    """
    def __init__(self, name, type_):
        self.type = type_
        self.name = name
        self.sections = []
        self.tutorials = []

    def add_sec(self, sec):
        self.sections.append(sec)

    def add_tut(self, tut):
        self.tutorials.append(tut)

    def __str__(self):
        return self.name + self.type


class TimeTable:
    """
    The whole time table, you can add class to time table
    """
    def __init__(self):
        self.secs = []
        self.score = 100
        self.timetable = {1: None, 2: None,
                          3: None, 4: None,
                          5: None}
        for i in self.timetable:
            time = {}
            j = 9
            while j <= 20:
                time[j] = None
                j += 1
            self.timetable[i] = time

    def copy(self):
        result = TimeTable()
        result.secs = self.secs.copy()
        for i in range(5):
            result.timetable[i+1] = self.timetable[i+1].copy()
        return result

    def suit(self,section):
        for sec in self.secs:
            if sec.conflict(section):
                return False
        return True

    def add(self, section):
        self.secs.append(section)
        for time in section.time:
            for t in range(time.duration):
                self.timetable[time.day][time.start+t] = section

    def time_for_eat(self):
        for i in self.timetable:
            for j in range(3):
                if self.timetable[i][11+j] is not None:
                    self.score -= 10

    def not_morning(self):
        for i in self.timetable:
            for j in range(4):
                if self.timetable[i][9+j] is not None:
                    self.score -= 10

    def not_continue(self):
        for i in self.timetable:
            for j in range(11):
                if self.timetable[i][9+j] != self.timetable[i][j+10] and self.timetable[i][j+10] is not None:
                    self.score -= 10

    def __str__(self):
        return str(self.timetable)

    def __repr__(self):
        return str(self.timetable)




def add_course(timetables, course):
    """
    add course to some timetables.
    :param timetables: list
    :param course: course
    :return:
    """

    def add_section(timetables, section):
        new_timetables = []
        for timetable in timetables:
            if timetable.suit(section):
                new_t = timetable.copy()
                new_t.add(section)
                new_timetables.append(new_t)
        return new_timetables

    final_result1 = []
    for section in course.sections:
        final_result1 += add_section(timetables, section)
    if course.tutorials == []:
        return final_result1
    final_result2 = []
    for section in course.tutorials:
        final_result2 += add_section(final_result1,section)

    return final_result2

