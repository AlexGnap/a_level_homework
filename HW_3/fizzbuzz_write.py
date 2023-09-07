with open('file.txt','r') as f:
    with open('output.txt', 'w') as file:
        for line in f:
            line = [int(num) for num in line.split()]

            fizz, buzz, fizzbuzz = line[0], line[1], line[2]

            lst = []
            for i in range(1, fizzbuzz + 1):
                if i % fizz == 0 and i % buzz == 0:
                    lst.append('FB')
                elif i % fizz == 0:
                    lst.append('F')
                elif i % buzz == 0:
                    lst.append('B')
                else:
                    lst.append(i)
            # print(lst)
            output = str(lst)
            file.write(output + '\n')

