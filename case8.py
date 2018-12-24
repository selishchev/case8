import numpy as np
import matplotlib.pyplot as plt
import pylab
import math
import pylab
from matplotlib import mlab

def _1():
    currency = []
    date = []
    day = 1
    with open('usd9.txt') as f:
        for item in f:
            currency.append(float(item))
            date.append(day)
            day += 1
    plt.plot(date, currency)
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

def _3():
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
    plt.title('USD-Rubles and EURO-Rubles in 2018')
    plt.xlabel('Days')
    plt.ylabel('Rubles for USD and EURO')
    selected_x1 = 232
    selected_y1 = 78.133
    pylab.annotate(u'EURO',
                   xy=(selected_x1, selected_y1))
    selected_x2 = 232
    selected_y2 = 68
    pylab.annotate(u'USD',
                   xy=(selected_x2, selected_y2))
    plt.plot(date, currency, currency_e)
    plt.grid(True)
    plt.show()


def _4():
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

    pylab.subplot(1,2,1)
    plt.plot(date, currency)
    pylab.title('USD')
    plt.grid(True)

    pylab.subplot(1,2,2)
    plt.plot(date, currency_e)
    pylab.title('EURO')
    plt.grid(True)

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
    currency = []
    with open('usd5.txt') as f_in:
        for item in f_in:
            st = item.split(" ")
            st2 = st[1].replace('\n', '')
            currency.append(float(st2))
    dx = 1
    xmin = 1
    pylab.ion()
    ylist = []
    for n in range(len(currency)):
        pylab.clf()
        ylist.append(currency[n])
        xlist = mlab.frange(xmin, len(ylist), dx)
        pylab.plot(xlist, ylist)
        pylab.draw()
        pylab.pause(0.05)
    pylab.pause(30)
pylab.close()


def _11():
    currency = []
    date = []
    with open('usd5.txt') as f_in:
        for item in f_in:
            st = item.split(" ")
            date.append(st[0])
            currency.append(float(st[1]))
    y_pos = np.arange(len(date))
    plt.bar(y_pos, currency, align='center', alpha=0.5)
    plt.xticks(y_pos, date)
    plt.ylabel('Currency')
    plt.title('Date')
    plt.show()


def _12():
    date = "17.01.2017"
    rub_usd = 59.6067  # курс доллара по даннам ЦБ на дату
    rub_eur = 63.2308  # курс евро по даннам ЦБ на дату
    v_rub = 157301000000  # общий объем валютных сделок в  руб.
    v_usd = 1036400000  # своп USD/RUB в долларах
    v_eur = 1500000000  # своп EUR/RUB в евро
    v_usd_rub = v_usd * rub_usd
    v_eur_rub = v_eur * rub_eur
    v_other = v_rub - (v_usd_rub + v_eur_rub)
    data = [v_other, v_usd_rub, v_eur_rub]
    plt.figure(num=1, figsize=(3, 3))
    plt.axes(aspect=1)
    plt.title('Currency swap on ' + date + '\n' + 'Total volume: ' + str(v_rub) + ' RUB', size=14)
    plt.pie(data, labels=('Other: ' + str(v_other) + ' RUB', 'USD: ' + str(v_usd_rub) + ' RUB\n(' + '$' + str(v_usd) + ")", 'EUR: ' + str(v_eur_rub) + ' RUB\n(' + str(v_eur) + ' EUR)'))
    plt.show()


def _13():
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib import cm
    currency = []
    with open('usd5.txt') as f_in:
        for item in f_in:
            st = item.split(" ")
            st2 = st[1].replace('\n', '')
            currency.append(float(st2))
    dx = 1
    xmin = 1
    xmax = len(currency)+1
    x = np.arange(xmin, xmax, dx)
    y = np.arange(xmin, xmax, dx)
    mlim = np.array(currency)
    xgrid, ygrid = np.meshgrid(x, y)
    zg = mlim + (xgrid*ygrid)/(xgrid*ygrid) - 1
    fig = pylab.figure()
    axes = Axes3D(fig)
    axes.plot_surface(xgrid, ygrid, zg, rstride=4, cstride=4, cmap=cm.jet)
    pylab.show()

n = int(input('Choose:'))
if n == 1:
    _1()
elif n == 2:
    _2()
elif n == 3:
    _3()
elif n == 4:
    _4()
elif n == 5:
    _5()
elif n == 6:
    print('we did not do this one')
elif n == 7:
    print('we did not do this too')
elif n == 8:
    _8()
elif n == 9:
    _9()
elif n == 10:
    _10()
elif n == 11:
    _11()
elif n == 12:
    _12()
elif n == 13:
    _13()