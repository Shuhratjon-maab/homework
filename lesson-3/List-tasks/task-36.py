nums = list(map(int, input().split()))

sum_of_positive = 0
for i in nums:
    if i > 0:
        sum_of_positive += i

print('Sum of postive numbers:', sum_of_positive)

# alternative way
s = 0
for i in nums:
    s += i * (i > 0)
print(s)