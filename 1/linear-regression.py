# coding : utf-8
import numpy as np
import pandas as pd
from sympy import *

# select a column as y
def setY(df, columnname):
    df.insert(len(df.columns), 'y', df[columnname])
    del df[columnname]

# return arg symbols
def initArg(n, tag='x'):
    if tag == 'x':
        string = ""
    else:
        string = tag + "0"
    for i in range(n):
        string += " " + tag + str(i + 1)
    return symbols(string)

# return the linear regression
def initFunc(tas, xs):
    func = tas[0]
    for i in range(len(xs)):
        func = func + tas[i + 1] * xs[i]
    return func

# return the single line J(theta)
def initSingleJta(func, y):
    return (func - y) ** 2

# calculate the J(theta)'s differential coefficient in tai
def calcDiffCoe(singleJta, xs, tas_v, y, i, df, alfa=1):
    m = len(df)
    n = len(df.columns)
    lists = [calcSingCoe(singleJta, xs, tas_v, y, i, df.iloc[j]) for j in range(m)]
    sumvalue = sum(lists)
    return alfa * sumvalue / (2 * m)

def calcSingCoe(singleJta, xs, tas_v, y, i, arr):
    Jta_coe = diff(singleJta, tas_v[i][0])
    # replace arguments
    for x_v in zip(xs, arr):
        # print x_v[1]
        Jta_coe = Jta_coe.subs(x_v[0], x_v[1])
    for ta_v in tas_v:
        Jta_coe = Jta_coe.subs(ta_v[0], ta_v[1])
    Jta_coe = Jta_coe.subs(y, arr[-1])
    return float(Jta_coe)

if __name__ == '__main__':
    tas = initArg(4, 'ta')
    xs = initArg(4)
    y = Symbol('y')
    hta_x = initFunc(tas, xs)
    jta_x = initSingleJta(hta_x, y)

    df = pd.read_csv("1.csv")
    setY(df, 'm')
    for i in range(5):
        print "Theta" + str(i), "is:", 0 - calcDiffCoe(jta_x, xs, zip(tas, np.zeros(5, float)), y, i, df)