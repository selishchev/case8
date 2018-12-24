import numpy as np
import matplotlib.pyplot as plt
import pylab
from matplotlib import mlab


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


def _9():
    currency = []
    date = []
    day = 1
    with open('usd9.txt') as f_in:
        for item in f_in:
            currency.append(float(item))
            date.append(day)
            day += 1
    plt.plot(date, currency, marker='*')
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

_13()
