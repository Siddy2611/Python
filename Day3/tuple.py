tup=(20,34,56,34,True)
print(type(tup))

for i in range(len(tup)):
    print(tup[i])

print("Index: ",tup.index(34))
print("Count: ",tup.count(34))