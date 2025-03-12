import unittest
from Student import Student


class Test_Student(unittest.TestCase):

    def setUp(self):
        self.student1 = Student('Herbei', 'Gabriel', 10)
        self.student2 = Student('Lupu', 'George', 9.5)
        self.student3 = Student('Popa', 'Jhonatan', 6.8)
        self.student4 = Student('Lili', 'Tijay', 8.3)

    def test_get_first_name(self):
        self.assertEqual(self.student1.get_first_name(), 'Herbei')
        self.assertEqual(self.student2.get_first_name(), 'Lupu')
        self.assertEqual(self.student3.get_first_name(), 'Popa')

    def test_get_last_name(self):
        self.assertEqual(self.student3.get_second_name(), 'Jhonatan')
        self.assertEqual(self.student4.get_second_name(), 'Tijay')

    def test_get_grade(self):
        self.assertEqual(self.student1.get_grade(), 10)
        self.assertEqual(self.student2.get_grade(), 9.5)
        self.assertEqual(self.student3.get_grade(), 6.8)

    def test_set_first_name(self):
        self.student1.set_first_name('Papa')
        self.student2.set_first_name('Emil')
        self.student4.set_first_name('Titel')
        self.assertEqual(self.student1.get_first_name(), 'Papa')
        self.assertEqual(self.student2.get_first_name(), 'Emil')
        self.assertEqual(self.student4.get_first_name(), 'Titel')

    def test_set_second_name(self):
        self.student1.set_second_name('Papa')
        self.student2.set_second_name('Emil')
        self.student4.set_second_name('Titel')
        self.assertEqual(self.student1.get_second_name(), 'Papa')
        self.assertEqual(self.student2.get_second_name(), 'Emil')
        self.assertEqual(self.student4.get_second_name(), 'Titel')

    def test_set_grade(self):
        self.student1.set_grade(5)
        self.student2.set_grade(9.4)
        self.student4.set_grade(8)
        self.assertEqual(self.student1.get_grade(), 5)
        self.assertEqual(self.student2.get_grade(), 9.4)
        self.assertEqual(self.student4.get_grade(), 8)
    if __name__ == "__main__":
        unittest.main()
