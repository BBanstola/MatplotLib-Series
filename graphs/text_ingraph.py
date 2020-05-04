import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib.request

style.use('fivethirtyeight')


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)

    def bytesconverter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytesconverter


def graph_data(stock):

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0,0))

    stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'

    source_code = urllib.request.urlopen(stock_price_url).read().decode()

    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source[1:]:
        stock_data.append(line)

    date, openp, highp, lowp, closep, adjusted_close, volume = np.loadtxt(stock_data, delimiter=',', unpack=True,
                                                                      converters={0: mdates.bytespdate2num('%Y-%m-%d')})

    x= 0
    y = 250 #len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x += 1

    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_locator(mticker.MaxNLocator(5))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    ax1.grid(True)

    ax1.annotate('Bad News!', (date[9], highp[9]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops=dict(facecolor='grey', color='grey'))

    font_dict = {'family' : 'serif', 'color' : 'darkred', 'size' : 15}

    ax1.text(date[10], closep[1], 'Text Example', fontdict = font_dict)

    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.title('Practicing Candle light')
    #plt.legend()
    plt.subplots_adjust(left=0.09, right=0.94, bottom=0.20, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('YAHOO')

