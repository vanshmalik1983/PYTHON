desh = ("India" , "china" , "france", "england" , "germany")
temp = list(desh)
temp.append("Russia")      #add item
temp.pop(3)                #remove item 
temp[2] = "finland"        #change item
desh = tuple(temp)
print(desh)

desh = ("India" , "pakistan")
desh2 = ("england" , "russia")
earth = desh + desh2 
print(earth)

tup = (0,1,2,3,2,31,1,3,2,3)
res = tup.count(2)
res = tup.index(2)
res = tup.index(2,2,9)
print("count is :", res)