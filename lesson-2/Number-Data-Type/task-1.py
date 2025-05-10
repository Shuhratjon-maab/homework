a = float(input())
print(f'Via format: {a:.2f}') # format orqali yaxlitlash

print('Via round:', round(a, 2)) # round - a sonni b xonagacha yaxlitlash (verguldan o'ng tomonda)

# format vs round
# format: 2.993 -> 2.99  2.995 -> 3.00
# round:  2.993 -> 2.99  2.995 -> 3.0


# alternatives:

# print(round(float(input()), 2))

# a = float(input('Enter a float number: '))
# b = int(input('Rounding to: '))

# print(round(a, b))