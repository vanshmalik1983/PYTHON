a = input("Enter the number: ")
print(f"Multiplication table of {a} is : ")
try:
    for i in range (1,11): #agar error aaya to next lines print krdega 
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalid input!")


print("some imp lines of code")
print("end of program")

try:
    num=int(input("enter an integer: "))
    a=[5,7]
    print(a[num])
except ValueError:
    print("num entered is not an integer")

except IndexError:
    print("Index error")