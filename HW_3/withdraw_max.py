atm_amount = [10, 20, 50, 100, 200, 500, 1000]

withdraw_amount = int(input('Enter desired amount of money to withdraw: '))

while withdraw_amount != 0:
    lst = []
    for i in atm_amount:
        count = 0
        if withdraw_amount // i > count:
            count = i
        lst.append(count)
    print('Here is your', max(lst), 'UAH')
    withdraw_amount = withdraw_amount - (max(lst))

