n=int(input("Enter number: "))
o_n=n
# while n<=20:
#     if n%2==0:
#         print(n)
#     n+=1



# while n>0:
#     print(n%10) #extracts last digit
#     n//=10 #removes last digit

# rev=0
# while n>0:
#     rev=rev*10+n%10 #extracts last digit
#     n//=10 #removes last digit
# print(rev)

# rev=0
# while n>0:
#     rev=rev*10+n%10 #extracts last digit
#     n//=10 #removes last digit

# if rev==o_n:
#     print("Palindrome")
# else:
#     print("Not palindrome")


import random

tries=0
num=random.randint(1,11)
while True:
    guess=int(input("Enter your guess: "))
    if guess==num:
        tries+=1
        print(f"Correct guess in {tries} tries")
        break
    else:
        tries+=1
        print("Incorrect guess, Try again")