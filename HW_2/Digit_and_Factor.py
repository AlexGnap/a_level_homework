#Ввести число, вивести його розряди та їх множники

numb = input('Insert number: ')

length = len(numb) -1

for i in numb:
    print('Digit: ' + str(i) + ' Factor:' + ' 10^' + str(length))
    length -= 1

