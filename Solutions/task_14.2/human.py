class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name



    def __str__(self):
        return f"Name: {self.last_name} {self.first_name}\nAge: {self.age}\nGender: {self.gender}"