num=int(input("Enter: "))

try:
    print(10/num)
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print(f"{TypeError}")
except Exception as err:
    print(f"Error occured due to {err}")

else:
    print("Runs when there are no exceptions")
finally:
    print("Will run no matter what")




#Raise Exception
age=int(input("Enter your age: "))
try:
    if age>18:
        print("Eligible to vote")
    elif age<18 and age>0:
        print("Not eligible")
    else:
        raise ValueError("Age cannot be negative")
except Exception as err:
    print(f"ERROR: {err}")