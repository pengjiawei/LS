import matplotlib.pyplot as plt
import numpy as np
import random
import time


def get_a(x):
    a = 0.0
    for i in x:
        a = a + (i * i)
    return a


def get_b(x):
    a = 0.0
    for i in x:
        a = a + i
    return a


def get_c(x, y):
    a = 0.0
    for i in range(len(x)):
        a = a + x[i] * y[i]
    return a


def get_d(y):
    a = 0.0
    for i in y:
        a = a + i
    return a


def get_random():
    return random.uniform(0, 10)


def print_list(ilist):
    for i in ilist:
        print(i, ",", end="")
    print("\n")
plt.figure()
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
listx = [1, 3, 3, 5, 6]
listy = [1, 2, 2, 4, 5]

# x in range(0,5)
# plt.axis([0, 5, 0, 10])
plt.grid(True)
# generate 10 points in 0~5 randomly
x = np.linspace(0, 10, 10)

times = 0
while(1):
    # time.sleep(1)
    print(times)
    times = times + 1
    xt = get_random()
    yt = get_random()
    listx.append(xt)
    listy.append(yt)
    plt.clf()
    A = get_a(listx)
    B = get_b(listx)
    C = get_c(listx, listy)
    D = get_d(listy)
    n = len(listx)
    a = (B*D-C*n)/(B*B-n*A)
    b = (B*C-D*A)/(B*B-n*A)
    print_list(listx)
    print_list(listy)
    plt.scatter(listx, listy)
    plt.plot(x, a * x + b, 'g-')
    plt.pause(1)
