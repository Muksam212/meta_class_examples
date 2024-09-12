#Meta Class

#Meta Class is itself the class of class.

'''
The main purpose of using MetaClass is 

a) Create your own class dynamically or modify class creation: 
With a metaclass, you can control how classes are constructed. 
This includes automatically adding attributes, methods, 
or modifying class properties during the class creation process.

b)Define custom behavior: 
You can use a metaclass to define custom behaviors for classes. 
This could be enforcing certain coding rules, 
ensuring specific methods exist, or altering how instances of the class are created or behave.


In Order to Use Meta Class we need to extend the 'Type'.
'''

class VerboseMetaClass(type):
    def __new__(cls, class_name, class_parents, class_dict):
        print("Creating a new class named: ", class_name)
        new_class = super().__new__(cls, class_name, class_parents, class_dict)
        return new_class
    

class Spam(metaclass = VerboseMetaClass):
    def info(self):
        print("Insert Some elements")


obj = Spam()
obj.info()