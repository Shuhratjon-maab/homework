a = set(input().split())
b = set(input().split())

check = a in b or b in a
# check = a.issubset(b) or b.issubset(a)

print(check)