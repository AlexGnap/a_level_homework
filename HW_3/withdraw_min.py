#Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри

atm_amount = [10, 20, 50, 100, 200, 500, 1000]

withdraw_amount = int(input('Enter desired amount of money to withdraw: '))


for i in atm_amount:
    if withdraw_amount // i != 0:
        count = 9
    else:
        count = 10
    while withdraw_amount > 0 and count != 0:
        withdraw_amount -= i
        count -= 1
        print('Here is you money ', i)


#потрібно допрацювати. частина яка відповідає за корнеркейси, суми де потрібно видавати не 10 а 9 купюр,
#як наприклад 110, 250 - працює не зовсім правильно.
#буду вдячний за підказки

