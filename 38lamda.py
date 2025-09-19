# def double(x):
#     return x*2

def appl(fx,value):
    return 6 + fx(value)


double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y,z:(x+y+z)/3

print(double(22))
print(cube(22))
print(avg(22,8,10))
print(appl(cube, 5))
print(appl(lambda x: x*x*x ,10))