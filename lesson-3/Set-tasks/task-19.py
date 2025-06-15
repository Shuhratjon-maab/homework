a = input().split()
b = input().split()

c = a.copy()
c.extend(b)
c = list(set(c))

print(c)