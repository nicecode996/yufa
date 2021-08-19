#! usr/bin/env python3
# coding=utf-8
'''
sum = 0
for i in range(1, 101):
    sum = sum + i
    print(sum)

total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if ((i != j) and (i != k) and (j != k)):
                print(i, j, k)
                total += 1

    print(total)
    '''
'''
    for i in range(4):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        time.sleep(1)

points = int(input('输入分数： '))
if points > 90:
    print('A')
elif points > 80:
    print('B')
else:
    print('C')


print(datetime.date.today())
print(datetime.date(2333, 2, 3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day = datetime.date(1111, 2, 3)
day = day.replace(year=day.year + 22)
print(day)


peach=1
for i in range(9):
    peach=(peach+1)*2
print(peach)

print(random.uniform(10, 20))

if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=300, height=300, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    x0 = 150
    y0 = 100
    canvas.create_oval(x0 - 10, y0 - 10, x0 + 10, y0 + 10)
    canvas.create_oval(x0 - 20, y0 - 20, x0 + 20, y0 + 20)
    canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
    import math

    B = 0.809
    for i in range(16):
        a = 2 * math.pi / 16 * i
        x = math.ceil(x0 + 48 * math.cos(a))
        y = math.ceil(y0 + 48 * math.sin(a) * B)
        canvas.create_line(x0, y0, x, y, fill='red')
    canvas.create_oval(x0 - 60, y0 - 60, x0 + 60, y0 + 60)

    for k in range(501):
        for i in range(17):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 + math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
        for j in range(51):
            a = (2 * math.pi / 16) * i + (2 * math.pi / 180) * k - 1
            x = math.ceil(x0 + 48 * math.cos(a))
            y = math.ceil(y0 + 48 * math.sin(a) * B)
            canvas.create_line(x0, y0, x, y, fill='red')
    mainloop()
if __name__ == '__main__':
    from tkinter import *

    x = 360
    y = 160
    top = y - 30
    bottom = y - 30

    canvas = Canvas(width=400, height=600, bg='white')
    for i in range(20):
        canvas.create_oval(250 - top, 250 - bottom, 250 + top, 250 + bottom)
        top -= 5
        bottom += 5
    canvas.pack()
    mainloop()
'''
if __name__ == ' __mian__':
    person = {"li": 10, "wang": 50, "zhang": 20}
    max = 0
    for i in person:
        if person[i] > max:
            name, max = i, person[i]
    print(name, max)

#  print('%s,%d' % (m.person[m]))
