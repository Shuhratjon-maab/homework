lis = input().split()
delta = int(input())

new = []

start = 0
while start < len(lis):
    new.append(lis[start : start + delta])
    start += delta

print(new)