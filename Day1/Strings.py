Alphabet='A'
Num=65

print(ord(Alphabet)) #unicode of A = 65
print(chr(Num)) #unicode 65 = A

name="Siddharth"
print(name[5:-2]) #first value inclusive and last value exclude
print(name[0::2]) #start point: stop point(if empty includes whole): step(increment)

print(type(str(Num))) #Explicit Conversion

print(type(Num/5)) #Implicit Conversion

#input generally are of str datatype
age=int(input("Enter your age: "))
print(f"My name is {name} and I am {age} yrs old.") #formatted string