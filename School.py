from Classroom import Classroom
from Utils import bubble_sort
from Utils import search
class School:

    def __init__(self):
        self.Class_lst = []

    def add_class(self, clas):
        self.Class_lst.append(clas)

    def sort_by_grade2(self):
        key = lambda x: x.get_grade2()
        bubble_sort(self.Class_lst, key)
        return self.Class_lst

    def sort_by_grade2_and_name(self, t):
        key = lambda x: x.number_of_students_with_str(t)
        bubble_sort(self.Class_lst, key)
        return self.Class_lst

    def search_for_pass_that_has_the_round_grade(self, g):
        key = lambda x: x.check1_for_pass_that_has_the_round_grade(g)
        t = search(self.Class_lst, key)
        return t

    def search_for_second_name(self, second_name):
        key = lambda x: x.check1_given_name(second_name)
        t = search(self.Class_lst, key)
        return t
    def __str__(self):
        p = "The school with the classes :"
        p = p + "\n"
        for i in range(len(self.Class_lst)):
            p = p + str(i+1) + "."
            p = p + self.Class_lst[i].__str__()
            p = p + "\n"
        return p
