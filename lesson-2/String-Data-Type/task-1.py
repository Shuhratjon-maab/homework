name = input()
birthyear = int(input())

print('{}, your age is {}'.format(name.capitalize(), 2025 - birthyear))

# keyingi yilda ham ishlaydigan holat:

from datetime import date

currentyear = int(str(date.today()).split('-')[0]) # qo'lbola
currentyear = date.today().year # osonroq

print('{}, your age is {}'.format(name.capitalize(), currentyear - birthyear))