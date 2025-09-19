# Factorial(7) = 7*6*5*4*3*2*1
# Factorial(6) = 6*5*4*3*2*1
# Factorial(5) = 5*4*3*2*1
# Factorial(4) = 4*3*2*1
# Factorial(0) = 1

# Factorial(n) = n * factorial (n-1)
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
    
# print(factorial(5))
# print(factorial(4))
# print(factorial(2))

# fibonacci sequence 
# f(0)=0
# f(1)=1
# f(2)=f1+f0
# f(n)=f(n-1)+f(n-2) 

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(15))

