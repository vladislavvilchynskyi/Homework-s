from student import Student
from group import Group, TooMuchStudentError

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')


gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
except TooMuchStudentError as e:
    print(e)

print(f'Old group:{gr}\n-----------------------------')

assert gr.find_student('Jobs') == st1, 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'

gr.delete_student('Taylor')
print(f'New group:{gr}')