# Class:
# A class is a user-defined blueprint or prototype from which objects are created. 
# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Properties and Methods form a central entity called Class
# Class is an abstraction of some entity which contains common set of properties and methods

# Example : Human is a class, 
#           Name, Gender, Occupation are properties
#           They perform some kind of work like speaking , do work , sleeping . So this speaking , do work , sleeping are the methods

# Object : Its a specific instance of a class

class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name , "plays tennis")
        elif self.occupation == "actor":
            print(self.name , "shoots film")
    
    def speaks(self):
        print(self.name,"says how are you ?")


tom = Human("tom cruise" , "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova" , "tennis player")
maria.do_work()
maria.speaks()



