class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, I am {}!".format(self.name)

name = input()
person = Person(name)
greeting = person.greet()
print(greeting)
