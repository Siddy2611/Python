# # - Accept an integer and Print hello world n times
n=int(input("Enter number: "))
# for i in range(n):
#     print("Hello World")

# # - Print natural number up to n
# for i in range(1,n):
#     print(i)
# # - Reverse for loop. Print n to 1
# for i in range(n,0,-1):
#     print(i)

# # - Sum up to n terms
# sum=0
# for i in range(n):
#     sum+=n
# print(sum)

# # - Factorial of a number
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("Factorial: ",fact)

# # - Print the sum of all even & odd numbers in a range
# # separately
# odd_sums=0
# even_sums=0
# for i in range(n):
#     if(i%2!=0):
#         odd_sums+=i
#     else:
#         even_sums+=i
# print("Odd sums: ",odd_sums)
# print("Even sums: ",even_sums)

# - Print all the factors of a number
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# - Accept a number and check if it a perfect number or not.  A number whose sum of factors is equal to the number itself
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if sum==n:    
#     print(f"{n} is perfect number")


# - Check wether the number is prime or not
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime")

# - Reverse a string without using in build functions. and Check string is Pallindrome or not
name=input("Type something: ")
b=""
for i in range(len(name)-1,-1,-1):
    b+=name[i]
print(b)

if b==name:
    print("It is palindrome")

# - Count all letters, digits, and special symbols from a given
# string
#  Given: str1 = "P@#yn26at^&i5ve"
#  Expected Outcome:
#  Total counts of chars, digits, and symbols
#  Chars = 8
#  Digits = 3
#  Symbol = 4

str1 = "P@#yn26at^&i5ve"
chars=0
digits=0
symbols=0
for i in str1:
    if i.isalpha():
        chars+=1
    elif i.isdigit():
        digits+=1
    else:
        symbols+=1

print(chars," ",digits," ",symbols)
