n=int(input("Enter any number : "))

if n>0:
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("Factorial of",n,"is",fact)
else:
    print("Factorial is not defined for negative numbers.")