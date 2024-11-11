from student import Student

class TooMuchStudentError(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
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