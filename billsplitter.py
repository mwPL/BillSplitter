import random

guests = {}
print('Enter the number of friends joining (including you):')
num = int(input())
if num < 1:
    print('No one is joining for the party')
    exit()
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(num):
        guests[input()] = 0
print('Enter the total bill value:')
bill = int(input())
perguest = round((bill / num), 2)
for i in guests:
    guests[i] = perguest
print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
decision = input()
if decision == 'Yes':
    lucky = random.choice(list(guests.keys()))
    print(f'{lucky} is the lucky one!')
    perguest = round(bill/(num - 1), 2)
    for i in guests:
        guests[i] = perguest
    guests[lucky] = 0
elif decision == 'No':
    print('No one is going to be lucky')
print(guests)