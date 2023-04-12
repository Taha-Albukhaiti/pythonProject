import unittest
import studis


class TestStudis(unittest.TestCase):
    def setUp(self):
        self.s1 = studis.Student("Taha", 25)
        self.s2 = studis.Student("Ali", 23)
        self.s3 = studis.Student("Max", 23)

    def test_1(self):
        expected_output = "Student Name: Taha, Age: 25, Courses: []\n" \
                          "Student Name: Ali, Age: 23, Courses: []\n" \
                          "Student Name: Max, Age: 23, Courses: []\n"
        self.assertEqual(studis.Student.get_all_students(), expected_output)

    def test_2(self):
        self.assertEqual(self.s1.course, [])
        self.assertEqual(self.s2.course, [])
        self.assertEqual(self.s3.course, [])


class TestStudisCourse(unittest.TestCase):
    def setUp(self):
        self.s1 = studis.Student("Taha", 25)
        self.s2 = studis.Student("Ali", 23)
        self.s3 = studis.Student("Max", 23)
        self.s1.enroll("Programmierung", "Datenbanken", "TI", "Mathe")

    def test_3(self):
        expected_output = "Student Name: Taha, Age: 25, Courses: ['Programmierung', 'Datenbanken', 'TI', 'Mathe']\n" \
                          "Student Name: Ali, Age: 23, Courses: []\n" \
                          "Student Name: Max, Age: 23, Courses: []\n"
        self.assertEqual(studis.Student.get_all_students(), expected_output)


class TestStudisParticipants(unittest.TestCase):
    def setUp(self):
        self.s1 = studis.Student("Taha", 25)
        self.s2 = studis.Student("Ali", 23)
        self.s3 = studis.Student("Max", 23)
        self.s1.enroll("Programmierung", "Datenbanken", "TI", "Mathe")
        self.s2.enroll("Python", "Datenbanken", "TI", "Mathe")
        self.s3.enroll("Algebra", "Datenbanken", "TI", "Python")

    def test_4(self):
        expected_output = [
            "Student Name: Ali, Age: 23, Courses: ['Python', 'Datenbanken', 'TI', 'Mathe']",
            "Student Name: Max, Age: 23, Courses: ['Algebra', 'Datenbanken', 'TI', 'Python']"
        ]
        self.assertEqual(studis.Student.get_course_participants("Python"), expected_output)

if __name__ == '__main__':
    unittest.main()
