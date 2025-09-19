ep1 ={122:45 , 123:89 , 645:32 , 567:69}
ep2 ={222:67 ,566:99}

ep1.update(ep2)
print(ep1)
ep1.clear()
print(ep1)

ep1.pop(122)
print(ep1)

ep1.popitem() #last item delete
print(ep1)