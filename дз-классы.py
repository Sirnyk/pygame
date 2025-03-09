class Student:
    def __init__(self, age, grades):
        self.age = age
        self.grades = list(grades)
    def add_grade(self, grade):
        return self.grades.append(grade)
    def get_avaerage_grade(self):
        return sum(self.grades)/len(self.grades)
    def display_info(self):
        return self.age, self.grades

Student1 = Student(15, [3, 7, 5, 9])

Student1.add_grade(5)
print(Student1.get_avaerage_grade())
print(Student1.display_info())


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        P = (self.a + self.b)*2
        return P
    def area(self):
        p = P / 2
        return p*(p - a)*(p - b)*(p - c)

tr = Triangle(3,4,5)
print(tr.perimeter())
