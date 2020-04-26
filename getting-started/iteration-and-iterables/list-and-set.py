from math import factorial

words = "Why someties I belived as many as six impossible things before breakfast".split()
print([len(word) for word in words])

print([len(str(factorial(x))) for x in range(20)])
