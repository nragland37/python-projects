class Parent_1:
    def __init__(self):
        print("Parent_1")

class Parent_2:
    def __init__(self):
        print("Parent_2")

# super() will only access
# the first parent in the list
class Child(Parent_1, Parent_2):   
    def __init__(self):
        super().__init__()
        print("Child ")

obj = Child()
print(obj)
print(Child.mro())

'''

Parent_1
Child 
<__main__.Child object at 0x104d4c090>
[<class '__main__.Child'>, <class '__main__.Parent_1'>, <class '__main__.Parent_2'>, <class 'object'>]


'''

# super() will access Parent_2
# because it next in the MRO
# of the Child class
class Parent_1:
    def __init__(self):
        super().__init__()  
        print("Parent_1")

class Parent_2:
    def __init__(self):
        print("Parent_2")

# order of parents dictats the order of the MRO (method resolution order)
# super() will access the next parent in the list
class Child(Parent_1, Parent_2):   
    def __init__(self):
        super().__init__()
        print("Child ")

obj = Child()

# prints Parent_2 first
# because its the last parent in the list
print(obj)
print(Child.mro())

'''

Parent_2
Parent_1
Child 
<__main__.Child object at 0x101134a10>
[<class '__main__.Child'>, <class '__main__.Parent_1'>, <class '__main__.Parent_2'>, <class 'object'>]

'''


# While this seems like a good idea.. 
# What if classes pass multiple arguments to __init__ ?

# ** is the unpacking operator 
# kwargs is a dictionary of keyword arguments
# kwargs = {"param1": 1, "param2": 2}
# **kwargs = param1=1, param2=2
class Parent_1:
    def __init__(self, param1, **kwargs):
        super().__init__(**kwargs)  
        self.param1 = param1
        print(f"Parent_1: {param1}")

class Parent_2:
    def __init__(self, param2, **kwargs):
        self.param2 = param2
        print(f"Parent_2: {param2}")

# param1=1, param2=2 are passed to Parent_1 and Parent_2
class Child(Parent_1, Parent_2):   
    def __init__(self, param1, param2, param3):
        super().__init__(param1=param1, param2=param2) 
        self.param3 = param3
        print(f"Child: {param3}")

obj = Child(1, 2, 3)
print(obj)

'''

Parent_2: 2
Parent_1: 1
Child: 3
<__main__.Child object at 0x104ab2790>

'''


# using explicit class names
# much more readable
class Parent_1:
    def __init__(self, param1):
        self.param1 = param1
        print(f"Parent_1: {param1}")
        
class Parent_2:
    def __init__(self, param2):
        self.param2 = param2
        print(f"Parent_2: {param2}")
        
class Child(Parent_1, Parent_2):
    def __init__(self, param1, param2, param3):
        Parent_1.__init__(self, param1)
        Parent_2.__init__(self, param2)
        self.param3 = param3
        print(f"Child: {param3}")
        
obj = Child(1, 2, 3)
print(obj)

'''

Parent_1: 1
Parent_2: 2
Child: 3
<__main__.Child object at 0x104ab2890>

'''

  
# notice the different orders of the print statements
# the super() method prints Parent_2 first because its 
# the at the top of the MRO

# 