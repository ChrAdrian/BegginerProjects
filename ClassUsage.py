# Script created by Chiriac Adrian Stefan (chr.adrian@yahoo.com)
# Brief : script exemplify the usage of classes


# Example
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


# s1 = Student("Adi", 19, 95)
# s2 = Student("Tim", 20, 90)
# s3 = Student("Jill", 21, 85)
#
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student((s3)))
# print(course.get_average_grade())


# Inheritance ( when classes have common methods or atributes a larger class object is created )
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")

    def speak(self):        # If there are the same functions in all classes the result is
        print("Something")  # overwritten by the function from the respective class

class Cat(Pet):     # Class Cat inherits class Pet methods
    def __init__(self, name, age, color):  # If we want to add a new variable to a subclass
        super().__init__(name,age)         # call super to inherit the parent class variables
        self.color = color                 # then add the variable you want for this class

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color} color")

class Dog(Pet):     # Class Dog inherits class Pet methods
    def speak(self):
        print("Bark")


# p = Pet("Tim", 19)
# p.speak()
# c = Cat("Bill", 34, "red")
# c.show()
# d = Dog("Jill", 12)
# d.speak()


# Class atributes
class Person:
    number_of_people = 0        # Class atribute - is available for all methods in the class

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

# p1 = Person("Tim")
# print(Person.number_of_people)
# p2 = Person("Adi")
# print(Person.number_of_people)


# Class methods
class Person:
    number_of_people = 0        # Class atribute - is available for all methods in the class

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod        # Defining a class method - acts on the class
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

# p1 = Person("Adi")
# print(Person.number_of_people_())


# Static methods
class Math:
    @staticmethod       # Defining a static method
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("Run")

# print(Math.add5(6))