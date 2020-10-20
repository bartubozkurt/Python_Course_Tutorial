class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return ("Hi, my name is {}".format(self.name)) 

# Create a new instance with a name of your choice
some_person = Person("Bartu Bozkurt")
print(some_person)

''' 
OUTPUT:
Hi, my name is Bartu Bozkurt
'''
