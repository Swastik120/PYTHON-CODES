# Program to print the factorial of a given number.

def fact(num):
    facto = 1
    for i in range(1,num+1,1):
        facto *= i
    return facto

num = int(input("Enter any number: "))
print(fact(num))
