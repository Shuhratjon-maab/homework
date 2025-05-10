s = input()
hasnodigit = 1
for i in s:
    if i.isdigit():
        hasnodigit = 0
        break
print(f'{s} has {'no' * hasnodigit} digit.')

# osonroq yo'li

s = input()
print(f" {s} has { 'no' * all(not i.isdigit() for i in s) } digit. ")

# bir qatorda

print((lambda s: f" {s} has { 'no' * all(not i.isdigit() for i in s) } digit. ")(input()))
