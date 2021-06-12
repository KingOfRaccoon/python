def getThreeMin(data = [], ost = 0):
    mins = []
    for i in data:
        if len(mins) < 3:
            if i % 3 == ost:
                mins.append(i)
        else:
            break
    return sorted(mins)

with open("27-B.txt") as file:
    data = file.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    size = data.pop(0)
    data.sort()
    mins_zero = getThreeMin(data)
    mins_one = getThreeMin(data, 1)
    mins_two = getThreeMin(data, 2)
    sum_zero = 0
    for i in mins_zero:
        sum_zero += i
    sum_one = 0
    for i in mins_one:
        sum_one += i
    sum_two = 0
    for i in mins_two:
        sum_two += i
    sum_last = mins_zero[0] + mins_one[0] + mins_two[0]
    print(sum_zero)
    print(sum_one)
    print(sum_two)
    print(sum_last)
    print()
    print(mins_zero)
    print(mins_one)
    print(mins_two)