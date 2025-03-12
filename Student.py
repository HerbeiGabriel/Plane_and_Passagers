class Student:
    def __init__(self, first_name, second_name, grade):
        self.first_name = first_name
        self.second_name = second_name
        self.grade = grade

    def get_first_name(self):
        return self.first_name

    def get_second_name(self):
        return self.second_name

    def get_grade(self):
        return self.grade

    def set_first_name(self, name):
        self.first_name = name

    def set_second_name(self, name):
        self.second_name = name

    def set_grade(self, grade):
        self.grade = grade

    def check_str_first_name(self, t):
        if self.first_name.startswith(t):
            return True
        return False

    def check_str_first_name_and_last(self, t):
        if self.first_name.find(t) != -1 or self.second_name.find(t) != -1:
            return True
        return False

    def check_for_pass_that_has_the_round_grade(self, g):
        if int(self.grade) == g:
            return True
        else:
            return False

    def __str__(self):
        p = 'The student ' + self.first_name + ' ' + self.second_name + ' with the grade ' + str(self.grade)
        return p
