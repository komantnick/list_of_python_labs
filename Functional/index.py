from functools import reduce
#сопостовляет каждой штуке оценку. в зависимости от резульатат оценка. собрать список тюплов. избавитьс яот пременных. на вызво функции
def resultList(list_object,max):
    # for a in list:
    #     print(a)
    getlist = map(lambda x: x[0] if x[0] > max/2 else x[0], list)
    # for a in getlist:
    #     print(a)
    # getlist=map(lambda x:(x[0],"5") if float(x[0]/max_item[1])<=1 and float(x[0]/max_item[1])>0.8 else
    # ((x[0],"4") if float(x[0]/max_item[1])<=0.8 and float(x[0]/max_item[1])>0.6
    # else ((x[0],"3") if float(x[0]/max_item[1])<=0.6 and float(x[0]/max_item[1])>0.4 else (x[0],"2"))),list)
    return getlist
def getMax(list_object):

    max_item = max(list_object, key=lambda item: item[1])
    print(max_item)

    return max_item[1]
    # max_var=max_item[1]
    #
    # resultList(list_copy,max_var)



def getPoints(list_object):
    pr_1 = map(lambda z: z[0], list_object)
    #pr_1=list(map(lambda z: z[0], list))
    #print(type(pr_1))
    # pr_2 = list(map(lambda a: a[1:][0], list))
    # print("LS",type(pr_2))
    #как не использовать костыли в данном случае???
    unique = reduce(lambda l, x: l + [x] if x not in l else l, pr_1, [])
    print(unique)
    getPoints = list(map(lambda x: (x,sum(n for _, n in list_object if _ == x)), unique))
    return getPoints
    #mylist = [u'nowplaying', u'PBS', u'PBS', u'nowplaying', u'job', u'debate', u'thenandnow']
    #unique = reduce(lambda l, x: (l[0] + [x[0]],l[1]+[x[1]]) if x[0] not in l[0] else l[0], list, [])
    #print(list)


list_input=[('Мат. Анализ', [('Иванов', 15), ('Петров', 13), ('Сидоров', 2), ( 'Васильев', 10), ('Жуков', 6)]),
('Алгебра', [('Петров', 24), ( 'Иванов', 20),( 'Васильев', 11),( 'Жуков', 12)]),
('Логика', [('Иванов', 10), ('Петров', 15), ('Сидоров', 6), ('Жуков', 15)])]
lambda_list=list(map(lambda a: a[1:][0], list_input))
#print(type(lambda_list))
lambda_list=reduce(lambda x,y: x+y,lambda_list)
l=getPoints(lambda_list)
#print(type(l))
getMax(l)
# list_output=getMax(l)
# for l in list_output:
#     print(l)


#z=getMax(l)
#print(lambda_list)


