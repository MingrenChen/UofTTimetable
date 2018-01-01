SELECT course_code,course_type,section_type, section_name, day, starttime, endtime
from course, section, course_section,time
WHERE course_code = 'CSC104'
  and section.id = course_section.section_id
  and course.id = course_section.course_id
  and time.section_id = section.id
  and (enrol_control = 'P' or enrol_control = 'E' or enrol_control = 'null');