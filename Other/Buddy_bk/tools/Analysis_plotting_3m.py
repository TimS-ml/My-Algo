# https://matplotlib.org/examples/color/named_colors.html
# https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import MultipleLocator


def calc(df, block=False):
    stat = {}
    # average working hour in a month
    if block:
        # df[5, :] is mix, first 6 day is -1, -1, -1
        # so just start with df[6, :]
        stat['avgTotalTime'] = round(df[:, 3].mean(), 2)
        stat['avgMorning'] = round(df[6:, 0].mean(), 2)
        stat['avgNoon'] = round(df[6:, 1].mean(), 2)
        stat['avgNight'] = round(df[6:, 2].mean(), 2)
        stat['stdMorning'] = np.std(df[6:, 0], dtype=int)
        stat['stdNoon'] = np.std(df[6:, 1], dtype=int)
        stat['stdNight'] = np.std(df[6:, 2], dtype=int)
        stat['avgJob'] = round(df[:, 4].mean(), 2)
        stat['avgJob_impt'] = round(df[:, 5].mean(), 2)
    else:
        stat['avgTotalTime'] = round(df[:, 4].mean(), 2)
        stat['avgMorning'] = round(df[:, 1].mean(), 2)
        stat['avgNoon'] = round(df[:, 2].mean(), 2)
        stat['avgNight'] = round(df[:, 3].mean(), 2)
        stat['stdMorning'] = np.std(df[:, 1], dtype=int)
        stat['stdNoon'] = np.std(df[:, 2], dtype=int)
        stat['stdNight'] = np.std(df[:, 3], dtype=int)
        stat['avgJob'] = round(df[:, 5].mean(), 2)
        stat['avgJob_impt'] = round(df[:, 6].mean(), 2)
    return stat


# Only last 3 month data
# Daily Time + Morning/Noon/Night Time
def plotting_3m(df, df2, style=0, timerage=''):
    stat = calc(df)
    day = df[:, 0].astype('U')
    # print(day)

    # plot part
    gs = gridspec.GridSpec(2, 1)

    if style == 0:
        plt.style.use('ggplot')
    if style == 1:
        plt.style.use('seaborn-pastel')
    if style == 2:
        plt.style.use('fivethirtyeight')

    # fig 1
    ax1 = plt.subplot(gs[0, :])
    # ax1 = plt.subplot(gs[0, 0])
    ax1.bar(day, df[:, 4], label='Total time per day', alpha=0.9)
    ax1.plot(day,
             df2[:, 0],
             linestyle='-',
             linewidth=4,
             label='7 days of SMA',
             color='saddlebrown',
             alpha=0.7)
    ax1.axhline(stat['avgTotalTime'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    ax1.set(ylabel='Time(min)')
    # ax1.tick_params(axis='x', labelrotation=45)
    ax1.set_title('Avg Time (min): {}'.format(stat['avgTotalTime']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    if timerage == '3m':
        ax1.xaxis.set_major_locator(MultipleLocator(10))
    elif timerage == '1b':
        ax1.xaxis.set_major_locator(MultipleLocator(1))
    elif timerage == 'all':
        ax1.xaxis.set_major_locator(MultipleLocator(50))
    ax1.legend()

    # fig 2
    ax2 = plt.subplot(gs[1, :])
    ax2.plot(day[:, ],
             df[:, 1],
             # linestyle=':',
             linewidth=4,
             color='salmon',
             label='Morning',
             alpha=0.6)
    ax2.plot(day[:, ],
             df[:, 2],
             # linestyle='-.',
             linewidth=3,
             color='wheat',
             label='Noon',
             alpha=0.7)
    ax2.plot(day[:, ],
             df[:, 3],
             # linestyle='--',
             linewidth=3,
             color='peru',
             label='Night',
             alpha=0.6)
    ax2.set(ylabel='Time(min)')
    # ax2.tick_params(axis='x', labelrotation=45)
    ax2.set_title('Avg Time (min): Morning-{} / Noon-{} / Night-{}'.format(
        stat['avgMorning'], stat['avgNoon'], stat['avgNight']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    if timerage == '3m':
        ax2.xaxis.set_major_locator(MultipleLocator(10))
    elif timerage == '1b':
        ax2.xaxis.set_major_locator(MultipleLocator(1))
    elif timerage == 'all':
        ax2.xaxis.set_major_locator(MultipleLocator(50))
    ax2.legend()

    plt.tight_layout()
    plt.show()
