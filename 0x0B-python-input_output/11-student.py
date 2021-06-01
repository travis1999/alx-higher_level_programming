#!/usr/bin/python3
"""student to json"""


class Student:
    """class def of a student"""

    def __init__(self, first_name, last_name, age):
        """student init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        if not attrs:
            return self.__dict__
        return {attr: value for attr, value in self.__dict__.items() if attr in attrs}

    def reload_from_json(self, json):
        """reloads data from json"""
        self.__dict__.update(json)


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
