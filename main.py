from Student import Student
from Classroom import Classroom
from Utils import bubble_sort
from School import School
from Utils import combine

"""#1"""
student1 = Student('Gabi', 'Herbei', 10)
student2 = Student('Mary', 'Nkd', 2.5)
student3 = Student('perkikj', 'oerik', 9)
classroom1 = Classroom('Gigel Laba', '25')
classroom1.add_a_student1(student1)
classroom1.add_a_student1(student2)
classroom1.add_a_student1(student3)
"""#2"""
student4 = Student('Mario', 'Tate', 4)
student5 = Student('Andrew', 'Tate', 2.6)
student6 = Student('Ma', 'robot', 0.2)
student7 = Student('Foca', 'David', 1.54)
student8 = Student('Maie', 'Petrica', 4.89)
classroom2 = Classroom('Matica Mue', '17')
classroom2.add_a_student1(student4)
classroom2.add_a_student1(student5)
classroom2.add_a_student1(student6)
classroom2.add_a_student1(student7)
classroom2.add_a_student1(student8)
"""#3"""
student9 = Student('Din', 'Limba', 9.56)
student10 = Student('Tino', 'Coacaze', 2)
student11 = Student('Akonga', 'David', 6)
student12 = Student('Suleiman', 'Magnificul', 9)
student13 = Student('Mata', 'tuge', 3)
student14 = Student('Tactu', 'kdsk', 5.4)
classroom3 = Classroom('Mitu Pitu', '90')
classroom3.add_a_student1(student9)
classroom3.add_a_student1(student10)
classroom3.add_a_student1(student11)
classroom3.add_a_student1(student12)
classroom3.add_a_student1(student13)
classroom3.add_a_student1(student14)
"""#4"""
student15 = Student('Tuti', 'Valea', 6.8)
classroom4 = Classroom('Elena Crin', '25')
classroom4.add_a_student1(student15)
School = School()
School.add_class(classroom1)
School.add_class(classroom2)
School.add_class(classroom3)
School.add_class(classroom4)

for i in classroom2.backtrack1(3):
    print("\n")
    for j in i:
        print(j.__str__())
"""l = [1, 2, 3, 4, 5, 6, 7]
print(combine(l, 2))"""