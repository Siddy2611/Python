def hello():
    print("Good Morning")

hello()


def greet(name="Siddharth"):
    print(f"I am {name}")

greet()#default arguments
greet("Sid") #positional arguments

def details(name,age):
    print(f"I am {name} and my age is {age}")

details(12,"Siddharth")
details(age=21,name="Sid") #Keyword arguments