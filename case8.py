import numpy as np
import matplotlib.pyplot as plt
import pylab
import math
import pylab
from matplotlib import mlab

def _1():
    cy = []
    dat = []
    day = 1
    with open('usd9.txt') as f:
        for item in f:
            cy.append(float(item))
            dat.append(day)
            day += 1
    plt.plot(day, cy)
    plt.show()

def _2():
    currency = []
    currency_e = []
    date = []
    day = 1
    with open('euro1.txt') as f_in1:
        for char in f_in1:
            currency_e.append(float(char))
    with open('usd9.txt') as f_in:
        for item in f_in:
            currency.append(float(item))
            date.append(day)
            day += 1
    plt.plot(date, currency, currency_e)
    plt.show()


def _5():
    cy = []
    dat = []
    day = 1
    with open('usd9.txt') as f_in:
        for item in f_in:
            cy.append(float(item))
            dat.append(day)
            day += 1
    plt.subplot(111, polar=True)
    plt.plot(dat, cy, lw=2)
    plt.show()


def _8():
    currency = []
    date = []
    day = 1
    with open('usd9.txt') as f_in:
        for item in f_in:
            currency.append(float(item))
            date.append(day)
            day += 1
    plt.title('USD-Rubles in 2018')
    plt.xlabel('Days')
    plt.ylabel('Rubles for USD')
    plt.plot(date, currency)
    plt.axis([0, 250, 55, 72])
    plt.grid(True)
    plt.show()


def _9():
    currency = []
    currency_e = []
    date = []
    day = 1
    with open('euro1.txt') as f_in1:
        for char in f_in1:
            currency_e.append(float(char))
    with open('usd9.txt') as f_in:
        for item in f_in:
            currency.append(float(item))
            date.append(day)
            day += 1
    plt.plot(date, currency, marker='*')
    plt.plot(date, currency_e, marker='o')
    plt.show()


def _10():
    xmin = 0
    xmax = 250

    dx = 1
    xlist = mlab.frange(xmin, xmax, dx)
    currency = []
    date = []
    day = 1
    with open('usd9.txt') as f_in:
        for item in f_in:
            currency.append(float(item))
            date.append(day)
            day += 1

    pylab.ion()

    for n in range(240):
        ylist = [n for x in xlist]
        pylab.clf()
        pylab.plot(xlist, ylist)
        pylab.draw()
        pylab.pause(0.01)

    pylab.close()

_1()