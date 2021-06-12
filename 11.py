def countOnNumber(data = [], number = 0):
    summary = 0
    counter = 0
    if number == 0:
        for i in data:
            temp = i.split()
            counter += 1
            for x in range(int(temp[1])):
                summary += int(temp[0])
    else:
        for i in data:
            temp = i.split()
            for x in range(int(temp[1])):
                if summary + int(temp[0]) <= number:
                    summary += int(temp[0])
                    counter += 1
                else:
                    break
    return summary, counter


with open("26.txt") as file:
    data = file.readlines()
    quantity = int(data[0].split()[0])
    size = int(data.pop(0).split()[1])
    a = []
    b = []
    for i in data:
        if i.split()[2] == 'A':
            a.append(i)
        else:
            b.append(i)
    size_a, quantity_a = countOnNumber(a)
    print(size_a, quantity_a)
    size -= size_a
    quantity -= quantity_a
    print(size, quantity)
    b.sort(key=lambda i: int(i[0]) * int(i[1]))
    print(countOnNumber(b, size))