from tkinter import *
import random

rectangle_list=[]

def bounding_box(list): #заменить на список прямоуголньиков в виде tuple и отдает рамку вне зависимости
  min_x=list[0][0] #сравнить с нулевым эелментом!!!!!!
  min_y=list[0][1]
  max_x=list[0][2]
  max_y=list[0][3]
  if len(list)<3:
      return [0,width,0,height]
  else:
      for coords in list:
          coords_x = coords[0::2]
          coords_y = coords[1::2]
          for item in coords_x:
              if item < min_x:
                  min_x = item
              if item > max_x:
                  max_x = item
          for item in coords_y:
              if item < min_y:
                  min_y = item
              if item > max_y:
                  max_y = item
      return [min_x,min_y,max_x, max_y]

root = Tk()
file = "file.txt"
number = 0

#генератор прямоугольника на основе заданной вершины
def GetRectangle(left:tuple=None):
    points=None
    while True:

        if points is not None:
            left = yield tuple(points)
        inf = bounding_box(rectangle_list)
        border_box = [0, 0, width, height]
        if left is not None:
            border_box[0] = left[0]
            border_box[1] = left[1]
        else:
            if len(rectangle_list) >= 3:
                if inf:
                    border_box = inf
        if left is not None:
            x1=border_box[0]
            y1=border_box[1]
            # x_border2=border_box[2]
            # y_border2=border_box[3]
        else:
            print(border_box)
            x1 = random.randrange(border_box[0], border_box[2])
            y1 = random.randrange(border_box[1], border_box[3])
        x2 = x1 + random.randrange(0, border_box[2] - x1)
        y2 = y1 + random.randrange(0, border_box[3] - y1)
        points=[x1,y1,x2,y2]

def RandomRects(event):
    lst=next(g)
    canv.create_rectangle(lst[0], lst[1], lst[2], lst[3])
    rectangle_list.append(lst)

def RightClickRandomRects(event):
    lst=g.send((event.x,event.y))
    canv.create_rectangle(lst[0], lst[1], lst[2], lst[3])
    rectangle_list.append(lst)

#функция для определения наложений
#Vertical filling of crossed rectangle
def VerticalColor(event_list,fill,color=None):
    x1=event_list[0]+fill
    x2=event_list[1]
    x3=event_list[2]
    x4=event_list[3]
    while x1<x3:
        canv.create_line(x1,x2,x1,x4,fill=color)
        x1+=fill

#Horizontal filling of crossed rectangle
def HorizontalColor(event_list,fill,color=None):
    x1=event_list[0]
    x2=event_list[1]+fill
    x3=event_list[2]
    x4=event_list[3]
    while x2<x4:
        canv.create_line(x1,x2,x3,x2,fill=color)
        x2+=fill

#Coloring of Python
def Coloring(event,color=None,type=None):
    fill=4
    event_list=Crossing(event)
    #print(event_list)
    if event_list[0]>=0 and event_list[1]>=0 :
        if type==None:
            canv.create_rectangle(event_list[0], event_list[1], event_list[2], event_list[3], fill=color)
        elif type=="Vertical":
            canv.create_rectangle(event_list[0], event_list[1], event_list[2], event_list[3])
            VerticalColor(event_list,fill,color)
        elif type=="Horizontal":
            canv.create_rectangle(event_list[0], event_list[1], event_list[2], event_list[3])
            HorizontalColor(event_list,fill,color)

#построение прямоугольников из файла

def Crossing(event): #генератор не нужен!!!!!!!
    event_list = [-1, -1, width + 1, height + 2]
    x = event.x
    y = event.y
    for string in rectangle_list:
        if (x >= string[0] and x <= string[2] and y >= string[1] and y <= string[3]):
            # пересечения прямоугольников и заливка идет отдельно-разделить! сделать независим от лишних вещей. rectangle list-глобальный.остальное исправить
            # рамка глобалньая не нужна!
            if (string[0] > event_list[0]):
                event_list[0] = string[0]
            if (string[2] < event_list[2]):
                event_list[2] = string[2]
            if (string[1] > event_list[1]):
                event_list[1] = string[1]
            if (string[3] < event_list[3]):
                event_list[3] = string[3]
    return event_list #можно и tuple вернуть


with open(file,'r') as f:
    first_line = f.readline()
    first_line=[elt.strip() for elt in first_line.split(',')]
    width = int(first_line[0])
    height = int(first_line[1])
    canv = Canvas(root, width=width, height=height,  bg='white')
    for line in f:
        elem_list = [elt.strip() for elt in line.split(',')]
        elem_list = [int(i) for i in elem_list if int(i)>=0]
        if (len(elem_list)==4):
            rectangle_list.append(elem_list)
            inf = bounding_box(rectangle_list)
            if (elem_list[0]>width or elem_list[1]>height or  elem_list[2]>width or elem_list[3]>height):
                raise ValueError('Error: at least one of coordinates out of range')
            else:
                canv.create_rectangle(elem_list[0], elem_list[1], elem_list[2], elem_list[3])
        else:
            raise ValueError('Very bad thing. There is no 4 symbols')

        #number+=1
color="red"
type="Vertical"
#type="gray50"
inf = bounding_box(rectangle_list)
canv.bind("<Button-1>",RandomRects)
canv.bind("<Button-3>",RightClickRandomRects)
canv.bind("<Button-2>",lambda event:Coloring(event,color=color,type=type))
g=GetRectangle()

canv.pack()
root.mainloop()
#print(number)
#генератор, независимые функции, рамка независмо от всего остального. плюс заливка руками!
