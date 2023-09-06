"""
객체지향

__init__ 생성자
__del__ 소멸자
__repr__ 프린팅 (print custom)
__add__
__if__

"""

class People:
    gender = ''


class User(People):
    name = ''
    age = 0

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getUser(self):
        return f"name: {self.name}, gender: {self.gender} age: {self.age}"


user = User('Krong', 'Man', 20)

print(user.getUser())
