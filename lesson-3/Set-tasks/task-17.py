a = set(map(int, input().split()))
odds = set()

for i in a:
    if i % 2:
        odds.add(i)
print(odds)