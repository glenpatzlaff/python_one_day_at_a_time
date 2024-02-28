class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 0 < value < 120:
            self.__age = value
        else:
            print("Invalid age.")

# Test the encapsulation
person = Person("John Doe", 30)
print(person.age)  # 30
person.age = 35
print(person.age)  # 35
person.age = -5    # Invalid age.
