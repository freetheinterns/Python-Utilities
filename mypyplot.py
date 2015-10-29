# Created By: Theodore Tenedorio
# Date 10/29/2015
# Requires: Python2.7, matplotlib

# The following line is for ipython notebooks only.
#% matplotlib inline

import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import MinuteLocator, HourLocator, DayLocator, WeekdayLocator, MonthLocator, YearLocator, DateFormatter

# Dynamically scales a plot to depict data over a time range
def plot_date_range(dates, data, linefmt=['k','b','r'], figsize=(15, 10)):
    delta = max(dates) - min(dates)
    
    # Determine date range scale
    if abs(delta.days) > 2*365:
        major = YearLocator()
        minor = MonthLocator()
        fmt = DateFormatter('%Y')
    elif abs(delta.days) > 60:
        major = MonthLocator()
        minor = DayLocator()
        fmt = DateFormatter('%b \'%y')
    elif abs(delta.days) > 0:
        major = DayLocator()
        minor = HourLocator()
        fmt = DateFormatter('%a %b %d')
    elif abs(delta.seconds) > 0:
        major = HourLocator()
        minor = MinuteLocator()
        fmt = DateFormatter('%I%p')
    else:
        print 'ERROR: Expected date range > 0'
        return

    fig, ax = plt.subplots(figsize=figsize)
    for x in range(len(data)):
        ax.plot_date(dates, data[x], linefmt[x])
    ax.xaxis.set_major_locator(major)
    ax.xaxis.set_major_formatter(fmt)
    ax.xaxis.set_minor_locator(minor)
    ax.autoscale_view()
    ax.grid(True)

    fig.autofmt_xdate()

    plt.show()