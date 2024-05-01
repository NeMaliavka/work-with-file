def read_txt_file(name_file):
    lst = []
    with open(name_file, 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(line.strip())
    lst.append(name_file)
    return lst


for_1_txt = read_txt_file('1.txt')
for_2_txt = read_txt_file('2.txt')
for_3_txt = read_txt_file('3.txt')

lst = [for_1_txt, for_2_txt, for_3_txt]
lst.sort(reverse=True)
for i in lst:
    print(i[-1])
    print(len(i)-1)
    for j in range(len(i)-1):
        print(i[j])


