fruits=["Apple","Mango","Pineapple",40.5,40.5,True] #allows duplicate and different datatypes

numbers=[20,25,74,65,26,32]

numbers.append(34) #Adds at the end
numbers.insert(4,54) #Adds at 4th index
#numbers.extend(fruits) #Adds multiple elements or another list at the end
#numbers.remove(40.5)#Removes first occurence of 40.5
numbers.pop(2)#Removes element at 2nd index
#numbers.index("Mango")#finds the index of Mango
numbers.count(40.5) #counts how many times it occured
numbers.sort()
numbers.reverse()
new_numb=numbers.copy()
numbers.clear() #clears list

# for i in range(len(numbers)):
#     print(numbers[i])


#Questions

numb=[20,3,-45,67,98,12,-65,74]

print("Positive numbers are: ")
for i in range(len(numb)):
    if numb[i]>0:
        print(numb[i])

print("Negative numbers are: ")
for i in range(len(numb)):
    if numb[i]<0:
        print(numb[i])

sum=0
for i in range(len(numb)):
    sum+=numb[i]
print(f"Mean of List: {sum/len(numb)}")


largest=numb[0]
second=numb[0]

for i in range(len(numb)):
    if numb[i]>largest:
        second=largest
        largest=numb[i]
    elif numb[i]>second:
        second=numb[i]
print(f"Largest number is {largest}")
print(f"Second Largest number is {second}")



sort=[12,45,67,75]
for i in range(len(sort)-1):
    if sort[i]<sort[i+1]:
        continue
    else:
        print("Not sorted")
        break
else:
    print("Sorted list")