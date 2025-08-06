# - Accept an integer and Print hello world n times
n=int(input("Enter number: "))
for i in range(n):
    print("Hello World")

# - Print natural number up to n
for i in range(1,n):
    print(i)
# - Reverse for loop. Print n to 1
for i in range(n,0,-1):
    print(i)

# - Sum up to n terms
sum=0
for i in range(n):
    sum+=n
print(sum)

# - Factorial of a number
fact=1
for i in range(1,n+1):
    fact*=i
print("Factorial: ",fact)

# - Print the sum of all even & odd numbers in a range
# separately
odd_sums=0
even_sums=0
for i in range(n):
    if(i%2!=0):
        odd_sums+=i
    else:
        even_sums+=i
print("Odd sums: ",odd_sums)
print("Even sums: ",even_sums)
# - Print all the factors of a number
# - Accept a number and check if it a perfect number or not.

#  A number whose sum of factors is equal to the number itself


#  Ex - 6 = 1, 2, 3 = 
# - Check wether the number is prime or not
# - Reverse a string without using in build functions.4
# - Check string is Pallindrome or not
# - Count all letters, digits, and special symbols from a given
# string

#  Given: str1 = "P@#yn26at^&i5ve"

#  Expected Outcome:

#  Total counts of chars, digits, and symbols

#  Chars = 8

#  Digits = 3

#  Symbol = 4