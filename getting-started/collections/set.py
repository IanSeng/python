p = {1, -10, 4, 4, 5, 52, 2}
print(p)
type(p)

for x in p:
    print(x)

p.add(12345)
print(p)

set_a = {'aa', 'bb', 'cc'}
set_b = {'dd', 'bb', 'gg'}
set_c = { 'bb', 'cc'}
set_d = {'aa', 'bb','gg'}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))
print(set_c.issubset(set_a))