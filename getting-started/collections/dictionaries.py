# dictionary contain key and value
a = dict(a='aaa', b='bbb', c='ccc')
print(a)

#copy 
d = dict(aa=123, bb=1234, cc=1223)
e = d.copy()
print(e)

u = e.update(a)
print(u)

#iterate 
for key in a:
    print(f"{key} = {a[key]}")

for value in a.values():
    print(value)

print('aaa' in a)
print('a' in a)