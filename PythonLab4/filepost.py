import csv
import random
import string
from datetime import datetime
list=[]
transaction=[]
with open('bankaccount.csv',encoding='utf-8-sig') as file:
    reader=csv.reader(file,delimiter=';',quotechar='"')
    for row in reader:
        row=[x for x in row if x]
        list.append(row)
    with open('transaction.csv', encoding='utf-8-sig') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        for row in reader:
            print("B")
            row = [x for x in row if x]
            transaction.append(row)
#print(list)
for row in transaction:
    print(row)
def check(a,b):
    user_id=None
    for row in list:
        if (row[0]==a and row[1]==b):
            user_id=row[2]
    if user_id is None:
        user_id= ''.join([random.choice(string.digits) for n in range(6)])
        account_id = ''.join([random.choice(string.digits) for n in range(10)])
        return (user_id,account_id)
def activate(a,b,c,d,e):
    list.append([a,b,c,d,e])
    write_account()
        # configure writer to write standard csv file
def write_account():
    with open('bankaccount.csv', 'w', newline='', encoding='utf-8-sig') as outcsv:
        outcsv.truncate()
        writer = csv.writer(outcsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for item in list:
            # Write item to outcsv
            writer.writerow([item[0], item[1], item[2], item[3], item[4]])
def write_transaction():
    with open('transaction.csv', 'w', newline='', encoding='utf-8-sig') as outcsv:
        outcsv.truncate()
        writer = csv.writer(outcsv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for item in transaction:
            # Write item to outcsv
            writer.writerow([item[0], item[1], item[2], item[3],item[4]])
def getallcash():
    summ=sum(int(row[4]) for row in list)
    return summ
def listofaccounts():
    return list
def checkuser(a):
    for row in list:
        if row[3]==a:
            result=row
    try:
        tuple=(result[0], result[1], result[2], result[4])
    except Exception as e:
        print(e)
        print("Не существует такого счета. Введите другой номер")
    return tuple
#transaction to another bill
def transate(a,b,c,code=0):
    list1=(row[3] for row in list)
    list2=(row[3] for row in list)
    if (a in list1 and b in list2):
        transaction.append([a,b,c,str(datetime.now()),code])
        for row in list:
            if row[3] == a:
                row[4] = int(row[4])-int(c)
            if row[3] == b:
                row[4] = int(row[4])+int(c)
    else:
        print("Неправильно введены данные!")
    write_transaction()
    write_account()
def history(a):
    list_history_a=[]
    list_history_b = []
    for row in transaction:
        if row[0]==a:
            list_history_a.append(row)
        if row[1]==a:
            list_history_b.append(row)
    return [list_history_a,list_history_b]

#activate("A","B",222223,222222,0)
