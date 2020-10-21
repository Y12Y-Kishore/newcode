#HELLO NEW WORLD
# 1.Python programme add two numbers.
def add(x,y):
    return x+y
result=add(2,3)
print(result)
# 2.Maximum of two numbers in Python
def maxi(x,y):
    print(max(x,y))
    if x>y:
        return x
    else:
        return y
result=maxi(20,15)
#HELLO INDIA hello TATA
#HELLO WORLD
# 3.Python Program for factorial of a number
import math
print(math.factorial(10))
x=10
fact=1
for i in range(10,0,-1):
    fact=fact*i
print(fact)
#4.Check given number is armstrong number or not
import math
u=153
x=str(u)
n=len(x)   #Power
result=0
for i in x:
    y=int(i)
    sum=y**n

    result=result+sum
if u==result:
    print("Given number armstrong")
else:
    print("Given numner is not arstrong")
# 5.prime number in an interval
start=2
end=10
for i in range(start,end):
    if i>1:
        for x in range(2,i):
            if i%x==0:
                break
        else:
            print(i)
# 6.Python program to check whether a number is Prime or not
def prime_or_not(x):
    for i in range(2,x):
        if x%i==0:
            return "not prime"
        else:
            return "Its prime"
print(prime_or_not(5))
# 7.Fibonaci series
def fib(n):
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return b
    elif n<0:
        return "Enter positive numbers"
    if n>1:
        for i in range(2,n):

            c = a + b
            a = b
            b = c
        return b
print(fib(9))
# 8.Check given number is fibonaci or not # formula is (5*n^2+4) or (5*n^2-4)
# python program to check if x is a perfect square
import math


# A utility function that returns true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x
#
#
# # Returns true if n is a Fibinacci Number, else false
def isFibonacci(n):
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perferct square
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)

print(isFibonacci(10))
# 9.Python Program for Sum of squares of first n natural numbers
x=5
sum=0
for i in range(1,x+1):
    sum=sum+(i**3)
print(sum)

















