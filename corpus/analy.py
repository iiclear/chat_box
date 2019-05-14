def Fileanaly(filename):
    list = []
    with open(filename, 'r') as f:
        line = f.readlines()
        for i in line:
            list.append(i.strip())
    return list

a = Fileanaly('E:\python学长\qa.txt')
print(a)