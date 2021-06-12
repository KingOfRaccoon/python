with open("27989_B.txt") as file:
    data = file.read().split()
    for i in range(len(data)):
        data[i] = int(data[i])
    size = data.pop(0)
    print(size)
    print(data)
    dels2 = []
    dels13 = []
    dels26 = []
    for i in data:
        if i % 26 == 0:
            dels26.append(i)
        elif i % 13 == 0:
            dels13.append(i)
        elif i % 2 == 0:
            dels2.append(i)
    print(dels2)
    print(dels13)
    print(dels26)
    print(len(dels26) * (len(data) - len(dels26)) + len(dels2) * len(dels13) + len(dels26) * (len(dels26) -1))