import unittest

from Lab3.src.StudentManagement import StudentManagement

class StudentManagerTestCase(unittest.TestCase):
    def test_add_student_should_add_student_to_list(self):
        studentManagement = StudentManagement()

        result = studentManagement.add_student('1', 'Tom', 21)

        self.assertTrue(result)


    def test_update_student_should_update_student(self):
        studentManagement = StudentManagement()
        studentManagement.add_student('1', 'Tom', 21)

        result = studentManagement.update_student('1', 'Tom', 25)

        self.assertTrue(result)


    def test_remove_student_should_remove_student_from_list(self):
        studentManagement = StudentManagement()
        studentManagement.add_student('1', 'Tom', 21)

        result = studentManagement.remove_student('1')

        self.assertTrue(result)


    def test_add_grade_student_should_add_grade_to_list(self):
        studentManagement = StudentManagement()
        studentManagement.add_student('1', 'Tom', 21)

        result = studentManagement.add_grade('1', 'Math', 4.5)

        self.assertTrue(result)


    def test_avg_grades_should_return_average_grades(self):
        studentManagement = StudentManagement()
        studentManagement.add_student('1', 'Tom', 21)

        studentManagement.add_grade('1', 'Math', 4.5)
        studentManagement.add_grade('1', 'Math', 4.0)
        studentManagement.add_grade('1', 'Math', 3.0)
        studentManagement.add_grade('1', 'Math', 5.0)

        self.assertEqual(studentManagement.avg_grades('Math'), 4.125)

    def test_all_avg_grades_should_return_all_average_grades(self):
        studentManagement = StudentManagement()

        studentManagement.add_student('1', 'Tom', 21)

        studentManagement.add_grade('1', 'Math', 4.0)
        studentManagement.add_grade('1', 'Math', 4.0)
        studentManagement.add_grade('1', 'Language', 4.5)
        studentManagement.add_grade('1', 'Math', 4.0)
        studentManagement.add_grade('1', 'Math', 3.0)
        studentManagement.add_grade('1', 'Language', 3.5)
        studentManagement.add_grade('1', 'Technology', 3.5)
        studentManagement.add_grade('1', 'Math', 4.0)
        studentManagement.add_grade('1', 'Math', 5.0)
        studentManagement.add_grade('1', 'Technology', 4.5)
        studentManagement.add_grade('1', 'Language', 3.5)
        studentManagement.add_grade('1', 'Math', 4.0)
        studentManagement.add_grade('1', 'Language', 4.5)
        studentManagement.add_grade('1', 'Math', 3.5)

        self.assertEqual(studentManagement.avg_all_grades('1'), 3.9642857142857144)