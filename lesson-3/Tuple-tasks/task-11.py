t = tuple(input().split())
x = input()
indices_of_x = []

for i in range(len(t)):
    if t[i] == x:
        indices_of_x.append(i)

indices_of_x = tuple(indices_of_x)