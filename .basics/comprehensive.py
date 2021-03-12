d1 = {1:'a',2:'x',3:'y'}
print(d1)

d2 = {'a':1,'x':2,'y':3}
print(d2)

print(d2['a'])
print(d2.get('a'))
print(d2.get('y'))
print(d2.get('t'))
#print(d2['t']) # this produces an error instead of returning a None like the function .get(<key>)

d = {'c':5, 'a':1, 'b': 2, 'd':1}