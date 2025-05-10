s = input()
u = 0

for i in s:
    if i in "aeiou":
        u += 1
    # u += (i in "aeiou")

for j in "unli":
    u += s.count(j)

print('unli:  ', )
print('undosh:', len(s) - u)