fruits={"Apple","Mango",True,20.4}

fruits.add("Pineapple")
fruits.remove("Apple") #fruits.discard("Apple")
#fruits.clear()  #Clears set
popped=fruits.pop()
print(f"Popped element{popped}")

for i in fruits:
    print(i)    







a={20,45,30}
b={20,32,46}
union=a.union(b) #a|b
intersect=a.intersection(b) #Gives element which is common in both #a&b
diff=a.difference(b) #Gives one sets elements removing duplicate  #a-b
symm=a.symmetric_difference(b) #Gives both sets elements removing duplicates #a^b



#User input for these structures
print("--------------Lists-----------")
my_l=[]
for i in range(5):
    val=int(input("Enter numbers: "))
    my_l.append(val)

print(my_l)



print("--------------Sets------------")
emp=set()
for i in range(5):
    val=input("Enter fruits: ")
    emp.add(val)

print(emp)


print("--------------Tuple-----------")
my_t=()
l_t=list(my_t)
for i in range(5):
    val=int(input("Enter numbers: "))
    my_l.append(val)

my_t=tuple(l_t)
print(my_t)


print("--------------Dictionary-----------")
my_d={}
for i in range(3):
    key=input("Enter key: ")
    val=input("Enter value: ")
    my_d[key]=val

print(my_d)
