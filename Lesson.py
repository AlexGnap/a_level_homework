with open('text.txt') as file:
    for line in file:
        l = line.split(' ')
        d = {}
        for word in l:
            if word in d:
                d[word] = d.get(word) + 1
            else:
                d[word] = 1
        # print(d)

        print(sorted(d.items(), key=lambda x: x[1], reverse=True))
