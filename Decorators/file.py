from datetime import datetime,date
import re
import csv
import io

list_of_person_csv=[]
list_of_person_xml=[]


def str_decorator(min,max):
    def decorator(func):
        def wrapper(*args):
            if not min < len(args[1]) < max:
                raise ValueError("Строка не подходит по длине")
            return func(*args)
        return wrapper
    return decorator

def int_decorator(min,max):
    def decorator(func):
        def wrapper(*args):
            value=args[1]
            if value<min or value>max:
                raise ValueError("Значение не входит в указанный промежуток")
            return func(*args)
        return wrapper
    return decorator

def date_decorator(min):
    max = datetime.now()
    def decorator(func):
        def wrapper(*args):
            value=args[1]
            #print(type(max))
            if value<datetime.date(min) or value>datetime.date(max):
                raise ValueError("Значение не входит в указанный промежуток дат")
            return func(*args)
        return wrapper
    return decorator

def dict2xml(dict,className):
    #print(dict)
    str_res="<"+className+">"
    for keys, values in dict.items():
        #print("A")
        str_res=str_res+"<"+keys+">"+str(values)+"</"+keys+">"
    str_res+="</"+className+">"
    return str_res

def write_to_csv(list_of_person_csv):
    with open('file_import.csv', 'w') as file_handler:
        for item in list_of_person_csv:
            file_handler.write(item)

def write_to_xml(list_of_person_xml):
    with open('file_import.xml', 'w') as file_handler:
        for item in list_of_person_xml:
            file_handler.write("{}\n".format(item))
class DescriptCsv:
    def __init__(self, *attrs):
        self.__attrs = attrs
        #print("A")

    def __get__(self, instance, owner=None):
        output = io.StringIO()
        csvdata = [getattr(instance,attr) for attr in self.__attrs]
        # csvdata = [getattr(instance,self.__attrs[0]), getattr(instance,self.__attrs[1]),
        #            getattr(instance,self.__attrs[2])]
        writer = csv.writer(output, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(csvdata)
        csvstring = output.getvalue()
        return csvstring


#
class DescriptXml:
    def __init__(self, *attrs):
        self.__attrs = attrs
    def __get__(self, instance, owner):
        dict={}
        dict={attr:getattr(instance,attr) for attr in self.__attrs}
        # dict['name']=getattr(instance,self.__attrs[0])
        # dict['passport_number']=getattr(instance,self.__attrs[1])
        # dict['birthday']=getattr(instance,self.__attrs[2])
        xml=dict2xml(dict,owner.__name__)
        #print(xml)
        return xml


class Person(object):
    csv_desc = DescriptCsv("name", "passport_number", "birthday","surname")
    xml_desc = DescriptXml("name", "passport_number", "birthday","surname")
    # print(csv_desc.__dict__)

    def __init__(self,name,passport_number,birthday,surname):
        self.name = name
        self.passport_number = passport_number
        self.birthday = birthday
        self.surname=surname


    @property
    def name(self):
        return self.__name

    @name.setter
    @str_decorator(1,20)
    def name(self, name):
        self.__name = name

    @property
    def passport_number(self):
        return self.__passport_number

    @passport_number.setter
    @int_decorator(100000,999999)
    def passport_number(self,passport_number):
        self.__passport_number=passport_number

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    @date_decorator(datetime(1900,1,1))
    def birthday(self,birthday):
        self.__birthday=birthday



with open('file.csv',encoding='utf-8-sig') as file:
    reader=csv.reader(file,delimiter=',',quotechar='"')
    for file_number, row in enumerate(reader):
        file_number+=1
        name=row[0]
        passport_number=int(row[1])

        date_row=datetime.strptime(row[2], '%Y-%m-%d')
        # print(row[2])
        # print(date_row)
        birthday=datetime.date(date_row)
        surname="VV"
        #print(name)
        try:
            k = Person(name, passport_number, birthday,surname)

        except ValueError as e:
            k="Ошибка в строке"+str(file_number)
            print(e)
            print(k)
            continue
        # print("CSV")
        # #print(k.name)
        #print(k.csv_desc)
        list_of_person_csv.append(k.csv_desc)
        # print("XML")
        # print(k.xml_desc)
        list_of_person_xml.append(k.xml_desc)
        #print(k)

        #print(k.csv_desc)
        # list_of_person_csv.append(k.csv_desc)
        # print(list_of_person_csv)
        # list_of_person_xml.append(k.xml_desc)

        #print(list_of_person_csv)
# print(list_of_person_csv)
write_to_csv(list_of_person_csv)
write_to_xml(list_of_person_xml)
