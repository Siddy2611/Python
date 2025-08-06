print("Positive increment")
for i in range(10,20,2):  #starting: ending(exclusive):step(increment)
    print(i)

print("Negative decrement")
for i in range(20,10,-2):
    print(i)

#continue statement
for i in range(0,21,2):
    if(i==14):
        continue
    print(i)

#break statement
for i in range(0,21,2):
    if(i==14):
        break
    print(i)



# - Take a number as input and print its table
num=int(input("Enter your preffered number: "))
print(f"Multipication table of {num}")
for i in range(num,num*10+1,num):
    print(f"{num} * {i//num} = {i}") #i//num (0/5=0  5/5=1) 