from Student import Student
from Utils import bubble_sort
from Utils import search
from Utils import combine
class Classroom:
    def __init__(self, professor, grade2):
        self.professor = professor
        self.grade2 = grade2
        self.students_lst = []

    def get_professor(self):
        return self.professor

    def get_grade2(self):
        return self.grade2

    def set_professor(self, professor):
        self.professor = professor

    def set_grade2(self, grade):
        self.grade2 = grade

    def get_all_students(self):
        return self.students_lst

    def get_a_student(self, i):
        return self.students_lst[i]

    def number_of_students_with_str(self, t):
        key = lambda x: x.check_str_first_name(t)
        p = search(self.students_lst, key)
        return len(p)

    def check1_for_pass_that_has_the_round_grade(self, g):
        for i in range(len(self.students_lst)):
            if self.students_lst[i].check_for_pass_that_has_the_round_grade(g):
                return True
        return False

    def check1_str_first_name_and_last(self, t):
        key = lambda x: x.check_str_first_name_and_last(t)
        p = search(self.students_lst, key)
        return p

    def check1_given_name(self, second_name):
        for i in self.students_lst:
            if i.second_name == second_name:
                return True
        return False

    def add_a_student(self, first_name, second_name, grade):
        student1 = Student(first_name, second_name, grade)
        self.students_lst.append(student1)

    def add_a_student1(self, student1):
        self.students_lst.append(student1)

    def sort_name(self):
        key = lambda x: x.get_second_name()
        bubble_sort(self.students_lst, key)
        return self.students_lst

    def backtrack1(self, k):
        t = combine(self.students_lst, k)
        for i in range(len(t)-1, -1,  -1):
            s = True
            for j in range(0, len(t[i])-1):
                for p in range(j+1, len(t[i])):
                    if t[i][j].get_second_name() == t[i][p].get_second_name():
                        s = False
            if not s:
                t.pop(i)
        return t







    def __str__(self):
        p = 'The classroom with the professor ' + self.professor + ' and the grade ' + self.grade2 + ' and with the students '
        p = p + ("\n")
        for i in range(len(self.students_lst)):
            p = p + self.students_lst[i].__str__()
            p = p + ("\n")
        return p
