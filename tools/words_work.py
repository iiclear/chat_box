#coding:utf8
def txt_to_list(filename):
    list = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            list.append(line.strip())
    return list


