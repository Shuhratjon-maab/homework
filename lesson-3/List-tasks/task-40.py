lis = input().split()
unique = []

for i in lis:
    if lis.count(i) == 1:
        unique.append(i)

print(unique)