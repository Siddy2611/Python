a=int(input("Enter value: "))
b=int(input("Enter value: "))

#Arithmetic Operators
print("------------------------------")
print("Addition",a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Modulus",a%b) #Gives remainder
print("Flow Division",a//b) #removes decimal value
print("Power",a**2)

#Assignment Operators(Made up of arithmetic operators only)
print("------------------------------")

# a+=20
# a-=2
# a*=2
# a/=3
print(a)

#Comparison Operators
print("------------------------------")
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical Operators
print("------------------------------")

print(a>b and a!=b)
print(a>b or a==b)
print(not a==b)