# class Name:
#     names="Siddharth Sarkar"

#     def __init__(self,name):
#         self.name=name
#         print(f"I am 21 yrs old and my name is {self.name}")


# s=Name("Sid")
# # print(s.names)


#Inheritance

# class Parent:
#     def __init__(self,name):
#         self.name=name

# class Child(Parent):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age=age

#     def disp(self):
#         print(f"My name is {self.name} and I am {self.age} years old.")

# c=Child("Sid",21)
# c.disp()


#Multiple inheritance

# class father:
#     def hello(self):
#         print("I am father")

# class mother:
#     def hello(self):
#         print("I am mother")

# class child(father,mother):
#     def disp(self):
#         print("I am the child")

# c=child()
# c.disp()
# c.hello()
# print(child.mro()) #Shows order



#Multilevel inheritance

class Grandparent:
    def name(self):
        print("I am the grandparent")
        

class Parent(Grandparent):
    def name(self):
        print("I am the son of my father")
        super().name()

class child(Parent):
    def name(self):
        print("I am the son of my father's father")
        super().name()

c=child()
c.name() 

#Different types of access levels
# class Type:
#     def __init__(self):
#         self.name="Sid"
#         self._age=21 #Protected
#         self.__height=167 #Private
    
#     def disp(self):
#         print("Public: ",self.name)
#         print("Protected: ",self._age)
#         print("Private: ",self.__height)


# t=Type()
# t.disp()
