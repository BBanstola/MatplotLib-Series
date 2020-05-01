import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import matplotlib.dates as mdates
import datetime as dt

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
    split_source =  source_code.split('\n')

    for line in split_source[1:]:
        stock_data.append(line)

    date, openp, highp, lowp, closep, adjusted_close, volume = np.loadtxt(stock_data, delimiter=',', unpack=True,
                                                                      converters={0: mdates.bytespdate2num('%Y-%m-%d')})
    #for unix time
    # date_conv = np.vectorize(dt.datetime.fromtimestamp)
    # date = date_conv(date)


    #    plt.plot_date(date,openp,'-', label='price')

    ax1.plot_date(date, openp, '-', label='price')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax1.grid(True, color='g', linestyle='-')

    plt.xlabel('Date')
    plt.ylabel('Price')

    plt.title('Loading Data from Internet')
    plt.legend()
    plt.subplots_adjust(left=0.09, right=0.94, bottom=0.20, top=0.90, wspace=0.2, hspace=0)
    plt.show()


graph_data('TWTR')

