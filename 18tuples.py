tup = ( 1, 5 ,6 ,45 ,534, "vansh" , True )
# tup[0] = 90 #can't change
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-4])
print(tup[2])

if 45 in tup:
    print("Yes")
tup2 = tup[1:5]
print(tup2)