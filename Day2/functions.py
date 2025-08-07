# def hello():
#     print("Good Morning")

# hello()


# def greet(name="Siddharth"):
#     print(f"I am {name}")

# greet()#default arguments
# greet("Sid") #positional arguments

# def details(name,age):
#     print(f"I am {name} and my age is {age}")

# details(12,"Siddharth")
# details(age=21,name="Sid") #Keyword arguments



def reverse(str):
    rev=""
    for i in range(len(str)-1,-1,-1):
        rev+=str[i]

    if(rev==str):
        print("It is Palindrome")
    else:
        print("It is not Palindrome")

word=input("Enter word: ")
reverse(word)
