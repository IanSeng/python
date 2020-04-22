r = [1, -4, 8, 10, 15]
print(r[-1])
print(r[-2])

# slicing
s = [3, 10, 4, 5, 1023, 4309]
print(s[1:3])
print(s[1:-1])
print(s[2:])
print(s[:2])

# way to copy
t = s
print(t is s)
r = s[:]
print(r is s)
print(r == s)
u = s.copy()
print(u is s)

# count
w = "the abc fox is the agd is a big aaa".split()
print(w.index('fox'))
print(w.count("the"))

print(37 in [1, 32, 54, 53, 37])
print(37 not in [1, 32, 54, 53, 37])

# remove an element
u = "aaa bbb ccc ddd".split()
del u[3]
print(u)
u.remove('aaa')
print(u)

# insert
a = "aaa bbb ccc zzz ddd eee".split()
a.insert(2, "hello")
print(a)
print(' '.join(a))

# reverse and sort
g = [1, 2, 3]
g.reverse()
print(g)
d = [ 10, 324, 1, -3]
d.sort()
print(d)
d.sort(reverse=True)
print(d)