txt = 'LMaasleitbtui'

print('1-car:', txt[::2])
print('2-car:', txt[1::2])

# albatta bu xususiy hol uchun !

# agar text berilsa va uni ichida mashina nomi mavjudligi aniqlanishi kerak bo'lsa:
'''
def isin(x, t):
    if x in t:
        return 1
    for i in x:
        if i not in t:
            return 0
    return 1

txt = input('Enter text: ')
cars = []

for j in range(1, int(input('Number of cars: '))+1):
    cars.append(input(f'{j}-car: '))

for car in cars:
    if isin(car, txt):
        print(f'{car} is in {txt}')
    else:
        print(f'{car} is not in {txt}')
'''