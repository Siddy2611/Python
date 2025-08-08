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