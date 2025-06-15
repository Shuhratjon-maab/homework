a = set(input().split())
b = input()

if b in a:
    a.remove(b)

print(a)