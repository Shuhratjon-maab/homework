a = input().split()
b = input().split()

# print(sorted(a + b))

# a.extend(b)
# a.sort()

c = []
#c = a + b

c = a.copy()
c.extend(b)
c.sort()

print(c)

# Merge-Sort:

a.sort()
b.sort()

i = 0
j = 0

while (i < len(a) or j < len(b)):
    if (a[i] > b[j]):
        i += 1