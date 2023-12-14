import openpyxl
import random as r
import threading
from threading import Thread, BoundedSemaphore,currentThread
from time import sleep



lit = openpyxl.open("Spisok_gruppy.xlsx", read_only=True)
prep = openpyxl.open("Prepodavatel.xlsx", read_only=True)


b = lit.active
a = prep.active


max_connections = 3
pool = BoundedSemaphore(value=max_connections)



c = 0
k = 0


def f():

    for j in range(3, 4):
        for m in range(1,31,3):

            c = r.randint(2, 5)

            print(b[m][0].value + " сдает экзамен " + a[j][0].value + " и получает " + str(c)+ ' ')
            sleep(1)

            if c < 3:
                k = r.randint(3, 4)

                print(b[m][0].value + " пересдает экзамен " + a[j][0].value + " и получает " + str(k)+ ' ')
                sleep(3)



def x():

    for j in range(2,3):
        for z in range(2,31,3):

            c = r.randint(2, 5)

            print(b[z][0].value + " сдает экзамен " + a[j][0].value + " и получает " + str(c)+' ')
            sleep(3)

            if c < 3:
                k = r.randint(3, 4)

                print(b[z][0].value + " пересдает экзамен " + a[j][0].value + " и получает " + str(k) + ' ')
                sleep(1)


def p():

    for j in range(4,5):
        for i in range(3,31,3):

            c = r.randint(2, 5)

            print(b[i][0].value + " сдает экзамен " + a[j][0].value + " и получает " + str(c)+' ')
            sleep(3)

            if c < 3:
                k = r.randint(3, 4)

                print(b[i][0].value + " пересдает экзамен " + a[j][0].value + " и получает " + str(k) + ' ')
                sleep(1)





def test():
    with pool:

        t1 = threading.Thread(target=f)
        t1.start()

        t2 = threading.Thread(target=x)
        t2.start()

        t3 = threading.Thread(target=p)
        t3.start()


test()

