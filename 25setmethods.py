s1 = {1,2,5,6}
s2 ={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
c1 ={"shamli" , "delhi" , "goa" , "agra"}
c2 ={"shamli" ," patna" ,"meerut", "karnal"}
print(c1.isdisjoint(c2)) #if shamli2 then true 
print(c1.issuperset(c2))
print(c1.issubset(c2))
c1.add("baraut")
print(c1)
c1.remove("goa")
print(c1)

c1.discard("goa")
print(c1)
item = c1.pop()
print(c1)
