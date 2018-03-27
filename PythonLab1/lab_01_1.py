import csv
list=[]
#добавить оценки! выделить список оценок по отдельности! не заменять список групп!
with open('file_input.csv',encoding='utf-8-sig') as file:
    reader=csv.reader(file,delimiter=';',quotechar='"')
    for row in reader:
        row=[x for x in row if x]
        list.append(row)
list = [[int(element) if element.isdigit() else element for element in sublist] for sublist in list]
for row in list:
    average = row[2:] + [2] * (5-len(row[2:]))
    # while (len(average) < 5):
    #     average.append(2)
    #     row.append(2)
    average = average[0:5]
    # while (len(row)>7): #чтобы считало первые 5 оценок
    #     del row[-1]
    #     del average[-1]
    av = float(sum(average)) / len(average)
    row.append(av)
d ={}
for sub in list:
    key = sub[1]
    sub[1]=sub[-1]
    if key not in d: d[key] = []
    d[key].append(sub[:-1])
    #вывод
for row in d:
    print("Группа "+row+":")
    res=sorted(d[row], key=lambda x: x[1],reverse=True) #сортировка массива
    for value in res:
        for partval in value:
            print(partval,end=' ')
        print('\b')
#выделить список оценок
#csv не достает оценок
#не заменять группы. только оценки
