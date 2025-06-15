a = set(input().split())
b = set(input().split())

hasnocommon = a.isdisjoint(b)

print(hasnocommon)