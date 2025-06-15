nums = list(map(int, input().split()))

sum_of_negative = 0
for i in nums:
    if i < 0:
        sum_of_negative += i

print('Sum of negative numbers:', sum_of_negative)

# alternative way
s = 0
for i in nums:
    s += i * (i < 0)
print(s)