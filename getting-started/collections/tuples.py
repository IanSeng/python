# tuple is immmutable sequences of arbitrary objects 
t = ("Norway", 4.953, 3)
print(t[0])
print(len(t))

for item in t:
    print(item)


print(t + (338.0, 123e9))
print(type(t))
