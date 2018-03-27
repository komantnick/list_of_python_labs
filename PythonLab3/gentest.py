def calc():
    history = []
    while True:
        x, y = (yield)
        if x == 'h':
            print(history)
            continue
        result = x + y
        #print (result)
        yield result
        history.append(result)

c = calc()

print(type(c)) # <type 'generator'>

next(c) # Необходимая инициация. Можно написать c.send(None)
list=c.send((1,2)) # Выведет 3
print(list)
c.send((100, 30)) # Выведет 130
c.send((666, 0)) # Выведет 666
c.send(('h',0)) # Выведет [3, 130, 666]
c.close() # Закрывем генератор


#generator of rectangles
# def GetRectangle(event):
#     #global inf
#     #print(x2)
#     ev = event
#
#     #event=yield
#     ev = event
#     while True:
#
#         try:
#             print("A")
#
#             inf = bounding_box(rectangle_list)
#             x_border1 = inf[0]
#             x_border2 = inf[1]
#             y_border1 = inf[2]
#             y_border2 = inf[3]
#             # print("LL")
#
#
#
#             # print("LL")
#             #ev=(yield event)
#             x1 = random.randrange(x_border1, x_border2)
#             y1 = random.randrange(y_border1, y_border2)
#             x2 = x1 + random.randrange(0, x_border2 - x1)
#             y2 = y1 + random.randrange(0, y_border2 - y1)
#             # if (event):
#             #     x1 = event.x
#             #     y1 = event.y
#             #     x_border1 = 0
#             #     x_border2 = width
#             #     y_border1 = 0
#             #     y_border2 = height
#             # else:
#             #     #print("A")
#             #     x_border1 = inf[0]
#             #     x_border2 = inf[1]
#             #     y_border1 = inf[2]
#             #     y_border2 = inf[3]
#             #     x1 = random.randrange(x_border1, x_border2)
#             #     y1 = random.randrange(y_border1, y_border2)
#             x2 = x1 + random.randrange(0, x_border2 - x1)
#             y2 = y1 + random.randrange(0, y_border2 - y1)
#             yield [x1, y1, x2, y2]
#
#
