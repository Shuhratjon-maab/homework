a = set(input().split())
b = set(input().split())

c = a ^ b # a.symmetric_difference(b)

print(c)