def countOnNumber(data=[], number=0):
    summary = 0
    counter = 0
    for i in data:
        if summary + i <= number:
            counter += 1
            summary += i
    return summary, counter


with open("27888.txt") as file:
    data = file.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    size = data.pop(0)
    quantity = data.pop(0)
    data.sort()
    print(countOnNumber(data, size))
    print(data[600])
    print(size)
    print(data)
