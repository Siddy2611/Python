age=int(input("Enter your age: "))

if(age>=18):
    print("Eligible to vote")
elif(age<18 and age>0):
    print("Not eligible to vote")
else:
    print("Invalid age")


#Even-odd question
num=int(input("Enter number: "))
if(num%2==0):
    print(f"{num} is even")
elif(num%2!=0):
    print(f"{num} is odd")
else:
    print("Invalid number")


#Leap Year question

year=int(input("Enter year: "))
if((year%4==0 and year%100 !=0) or year%400==0):
    print("Leap Year")
else:
    print("Not a leap year")


#Country Climate Question

temp=int(input("Enter temprature: "))

if(temp<0):
    print("Freezing Cold")
elif(temp>0 and temp<10):
    print("Very Cold")
elif(temp>10 and temp<20):
    print("Cold")
elif(temp>20 and temp<30):
    print("Pleasant")
elif(temp>30 and temp<40):
    print("Hot")
else:
    print("Very Hot")