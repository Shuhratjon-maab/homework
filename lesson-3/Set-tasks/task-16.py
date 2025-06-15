a = set(map(int, input().split()))
evens = set()

for i in a:
    if i % 2 == 0:
        evens.add(i)
print(evens)