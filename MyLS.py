import matplotlib.pyplot as plt
import numpy as np


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


plt.figure()
plt.title('single variable')
plt.xlabel('x')
plt.ylabel('y')
listx = [1,3,3,5,6]
listy = [1,2,2,4,5]
# x in range(0,5)
# plt.axis([0, 5, 0, 10])
plt.grid(True)
# generate 10 points in 0~5 randomly
x = np.linspace(0, 10, 10)
plt.scatter(listx,listy)

A = get_a(listx)
B = get_b(listx)
C = get_c(listx, listy)
D = get_d(listy)
n = len(listx)
a = (B*D-C*n)/(B*B-n*A)
b = (B*C-D*A)/(B*B-n*A)

plt.plot(x, a * x + b, 'g-')
plt.show()
