name = input('please input a name: ')
amount = 0
for i in name:
    if i == 'A':
        print(i)
        amount = amount + 1

if amount == 0:
    print('Theres no As in your name')



