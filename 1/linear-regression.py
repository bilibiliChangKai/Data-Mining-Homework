# coding : utf-8
import numpy as np
import pandas as pd
from sympy import *

def normalize(df):
    newdf = pd.DataFrame()
    for f in df.columns:
        newdf[f] = map(lambda x: float(x - df[f].mean()) / (df[f].max() - df[f].min()), df[f])
    return newdf

class LinearRegression:
    def __init__(self, df, n):
        self.df = df
        self.tas_v0 = zip(initArg(4, 'ta'), np.zeros())
        self.xs = LinearRegression.initArg(4)
        self.y = Symbol('y')
        self.hta_x = LinearRegression.initFunc(tas, xs)
        self.jta_x = LinearRegression.initSingleJta(hta_x, y)

    # select a column as y
    def setY(self, columnname):
        self.df.insert(len(self.df.columns), 'y', self.df[columnname])
        del self.df[columnname]

    # return arg symbols
    @staticmethod
    def initArg(n, tag='x'):
        if tag == 'x':
            string = ""
        else:
            string = tag + "0"
        for i in range(n):
            string += " " + tag + str(i + 1)
        return symbols(string)

    # return the linear regression
    @staticmethod
    def initFunc(tas, xs):
        func = tas[0]
        for i in range(len(xs)):
            func = func + tas[i + 1] * xs[i]
        return func

    # return the single line J(theta)
    @staticmethod
    def initSingleJta(func, y):
        return (func - y) ** 2

    # calculate the J(theta)'s differential coefficient in tai
    def calcDiffCoe(self, singleJta, xs, tas_v, y, ta, df, alfa=1):
        m = len(df)
        n = len(df.columns)
        lists = [calcSingCoe(singleJta, xs, tas_v, y, ta, df.iloc[j]) for j in range(m)]
        sumvalue = sum(lists)
        return alfa * sumvalue / (2 * m)

    def calcSingCoe(self, singleJta, xs, tas_v, y, ta, arr):
        Jta_coe = diff(singleJta, ta)
        # replace arguments
        for x_v in zip(xs, arr):
            # print x_v[1]
            Jta_coe = Jta_coe.subs(x_v[0], x_v[1])
        for ta_v in tas_v:
            Jta_coe = Jta_coe.subs(ta_v[0], ta_v[1])
        Jta_coe = Jta_coe.subs(y, arr[-1])
        return float(Jta_coe)

    def cal

    def thetaIteration(tas_v)
        return map(lambda x : (x[0], x[1] - calcDiffCoe(jta_x, xs, tas_v0, y, x[0], nordf)), tas_v0)

if __name__ == '__main__':


    df = pd.read_csv("1.csv")
    setY(df, 'm')
    nordf = normalize(df)

    print "Q1:"
    tas_v1 = 
    print "Theta1 :", tas_v1
    
    print "Q2:"
