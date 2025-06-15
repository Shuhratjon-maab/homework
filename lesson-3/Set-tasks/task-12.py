a = set(input().split())
b = input()

if b not in a:
    a.add(b)

print(a)