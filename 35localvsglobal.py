x = 4 #global variable
print(x)

def hello():
    x =5 #local variable
    print(F"The local x is {x}")
    print("Hello vansh")
print(F"The global x is {x}")
hello()
x = 5
print(f"The global x is {x}")

def my_function():
    global x
    x = 10 # this will change the variable of global
    y = 5 #local

my_function()
print(x)