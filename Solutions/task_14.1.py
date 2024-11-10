class TooMuchStudentError(Exception):
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name



    def __str__(self):
        return f"Name: {self.last_name} {self.first_name}\nAge: {self.age}\nGender: {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}\nRecord book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >=10:
            raise TooMuchStudentError(f"Bro I`m sorry, but capacity this grou is over :(")
        self.group.add(student)

    def delete_student(self, last_name):
        self.group = {student for student in self.group if student.last_name != last_name}

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return (f'\nNumber:{self.number}\n{all_students} ')

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'Jim', 'Beam', '789')
st4 = Student('Female', 23, 'Jill', 'Valentine', '101')
st5 = Student('Male', 24, 'Jack', 'Daniels', '102')
st6 = Student('Female', 25, 'Jen', 'Aniston', '103')
st7 = Student('Male', 26, 'Joe', 'Black', '104')
st8 = Student('Female', 27, 'Jessica', 'Alba', '105')
st9 = Student('Male', 28, 'James', 'Bond', '106')
st10 = Student('Female', 29, 'Julia', 'Roberts', '107')
st11 = Student('Male', 30, 'Jason', 'Statham', '108')


gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!