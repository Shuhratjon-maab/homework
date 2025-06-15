tup = tuple(input().split())

lis = []

for i in tup:
    if tup.count(i) == 1:
        lis.append(i)

new_unique_tup = tuple(lis)

print(new_unique_tup)