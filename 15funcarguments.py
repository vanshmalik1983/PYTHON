def average(a,b=6,c=1):
    print("The average is",(a + b + c)/2)

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum +  i
    print("Average is:",sum/len(numbers))
    return sum/len(numbers)

# average(b =6)

d = average(5,6,6.21,100)
print(d)