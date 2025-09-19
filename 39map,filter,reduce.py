# MAP
def cube(x):
    return x*x*x 
print(cube(5))

l = [1,2,3,5,7,8,3]
newl = []
for item in l:
    newl.append(cube(item))

newl = list(map(cube,l))
print(newl)

#FILTER
def filter_function(a):
    return a<6
newnewl = list(filter(filter_function,l))
print(newnewl)


#REDUCE
from functools import reduce
num = [1,2,3,4,5]

def mysum(x,y):
    return x+y
sum = reduce(mysum,num)
print(sum)