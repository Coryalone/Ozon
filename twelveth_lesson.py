import random


# задание 1

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        print(self.name, self.surname)

student = Person('Иван', 'Иванов')
studentka = Person('Вася', 'Булочкин')
student.__str__()
studentka.__str__()
print()

# задание 2

class Student(Person):
    def __init__(self, name, surname, group_number):
        super().__init__(name, surname)       
        self.gn = group_number
        self.lm = []

    def set_test_score(self, mark):                
        self.mk = mark 
        self.lm.append(self.mk) 

    def __str__(self):        
        print(f'Студент: {self.name} {self.surname}, группа {self.gn}, оценки {self.lm}')

ivan = Student('Иван', 'Иванов', 'ГР-01')
vasen = Student('Вася', 'Булочкин', 'ГР-01')
ivan.set_test_score(5)
vasen.set_test_score(5)
ivan.__str__()
vasen.__str__()
print()

# задание 3

class Professor(Person):
    def __init__(self, name, surname, cours):
        super().__init__(name, surname)
        self.cours = cours

    def test_students(self, list_of_stud):
        for i in list_of_stud:
            i.set_test_score(random.randint(0, 10))

    def __str__(self):        
        print(f'Преподаватель: {self.name} {self.surname}, читает курс {self.cours}')

semen = Professor('Семен', 'Семенов','ООП')
semen.__str__()
list_of_stud = [ivan, vasen]
semen.test_students(list_of_stud)
semen.test_students(list_of_stud)
ivan.__str__(), vasen.__str__()
