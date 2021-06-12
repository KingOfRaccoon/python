def count(data=[]):
    counter = 0
    for i in data:
        if i % 2 == 0:
            counter += 1
        else:
            counter -= 1
    return counter


with open("27-B(1).txt") as file:
    data = file.readlines()
    size = int(data.pop(0))
    print(size)
    for i in range(len(data)):
        temp = data[i].split()
        data[i] = [int(temp[0]), int(temp[1])]
    print(data)
    summary = 0
    number = []
    defs = []
    for i in data:
        number.append(min(i[0], i[1]))
        summary += min(i[0], i[1])
        defi = abs(i[0] - i[1])
        if defi == 101:
            print(i)
        defs.append(defi)
    defs.sort()
    for i in range(len(defs)):
        if i < 5:
            print(defs[i])
    print(summary+101)
    print(number)
    print(count(number))
