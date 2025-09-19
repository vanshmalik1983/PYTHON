marks = [3, 5 , 6 , "vansh", True , 4, 6,9,10 ]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #Negative inedex
print(marks[len(marks)-3]) #Positive index
print(marks[5-3])
print(marks[2])

if 6 in marks:
    print("Yes")
else:
    print("No")

    if "array" in "vansh":
        print("Yes")
    
print(marks)
print(marks[1:8]) 
print(marks[1:8:2]) 

lst = [i for i in range(10)]
print(lst)
lst = [i+1 for i in range(10) if i%2==0]
print(lst)