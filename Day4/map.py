numb=[1,4,8,12]
square=map(lambda x:x**2,numb)
print(list(square))


numbs=[1,3,4,5,6,9,10]
evens=filter(lambda x: x%2==0,numbs)
print(list(evens))