l = [11 , 45 , 1 , 2 , 4 , 6]
print(l)
l.append(10)
l.sort(reverse = True)
l.reverse()
print(l.index(6))
print(l.count(2))
m = l.copy() #m=l
m[0] = 0
print(l)
l.insert(2,899)
m = [900 , 1000, 1100]
k = l + m 
print(k)
l.extend(m)
print(l)