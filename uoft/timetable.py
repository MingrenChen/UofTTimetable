"""
BFS to find a timetable.

"""

class schoolTime:
    def __init__(self, day, hour):
        self.hour = hour
        if day == 1:
            self.day = "Monday"
        elif day == 2:
            self.day = "Tuesday"
        elif day == 3:
            self.day = "Wednesday"
        elif day == 4:
            self.day = "Thursday"
        elif day == 5:
            self.day = "Friday"
        else:
            raise IndexError

    def __eq__(self, other):
        return self.hour == other.hour and self.day == other.day

    def __str__(self):
        return self.day + " {} O.clock".format(self.hour)


class Lecture:
    def __init__(self, course, code):
        self.course = course
        self.code = code
        self.time = []

    def add_time(self, time):
        self.time.append(time)

class Course:
    def __init__(self, name):
        self.name = name
        self.lec = []

    def add_lec(self, lec):
        self.lec.append(lec)

class TimeTable:
    def __init__(self):
        self.lecture = []
        self.timeoccupied = []

    def add_lec(self, lec):
        for time in lec.time:
            if time in self.timeoccupied:
                return False
        self.lecture.append(lec)
        for time in lec.time:
            self.timeoccupied.append(time)
        return True

    def clone_tt(self):
        result = TimeTable()
        result.lecture = self.lecture
        result.timeoccupied = self.timeoccupied
        return result

class TreeNode:
    def __init__(self, timetable):
        self.timetable = timetable
        self.children = []

    def add(self, timetable):
        self.children.append(TreeNode(timetable))


foo = TreeNode(TimeTable)
def addinto(treeNode, course):
    for lec in course:
        temp = treeNode.timetable.clone_tt()
        if temp.add_lec():
            treeNode.add(temp)