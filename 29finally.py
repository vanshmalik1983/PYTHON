def func1():
    try:
        l=[1,3,5,66,7]
        i = input("enter inder: ")
        print(l[i])
        return 1
    except:
        print("error occur")
        return 0

    finally:
        print("always executed")

x=func1()
print(x)