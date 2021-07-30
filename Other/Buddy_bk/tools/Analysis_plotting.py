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
        stat['avgMorning'] = round(df[66:, 1].mean(), 2)
        stat['avgNoon'] = round(df[66:, 2].mean(), 2)
        stat['avgNight'] = round(df[66:, 3].mean(), 2)
        stat['stdMorning'] = np.std(df[66:, 1], dtype=int)
        stat['stdNoon'] = np.std(df[66:, 2], dtype=int)
        stat['stdNight'] = np.std(df[66:, 3], dtype=int)
        stat['avgJob'] = round(df[:, 5].mean(), 2)
        stat['avgJob_impt'] = round(df[:, 6].mean(), 2)
    return stat


# Default
# Daily Time + Morning/Noon/Night Time
def plotting(df, df2):
    stat = calc(df)
    day = df[:, 0].astype('U')
    # print(day)

    # plot part
    gs = gridspec.GridSpec(2, 1)
    plt.style.use('ggplot')

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
    ax1.tick_params(axis='x', labelrotation=45)
    ax1.set_title('Avg Time (min): {}'.format(stat['avgTotalTime']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    ax1.xaxis.set_major_locator(MultipleLocator(7))
    ax1.legend()

    # fig 2
    ax2 = plt.subplot(gs[1, :])
    ax2.plot(day[66:, ],
             df[66:, 1],
             linestyle=':',
             linewidth=4,
             label='Morning',
             alpha=0.7)
    ax2.plot(day[66:, ],
             df[66:, 2],
             linestyle='-.',
             linewidth=3,
             label='Noon',
             alpha=0.7)
    ax2.plot(day[66:, ],
             df[66:, 3],
             linestyle='--',
             linewidth=3,
             label='Night',
             alpha=0.7)
    ax2.plot(day[66:, ],
             df[66:, 4] / 3,
             linestyle='-',
             linewidth=3,
             label='Avg',
             color='saddlebrown',
             alpha=0.5)
    ax2.set(ylabel='Time(min)')
    ax2.tick_params(axis='x', labelrotation=45)
    ax2.set_title('Avg Time (min): Morning-{} / Noon-{} / Night-{}'.format(
        stat['avgMorning'], stat['avgNoon'], stat['avgNight']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    ax2.xaxis.set_major_locator(MultipleLocator(4))
    ax2.legend()

    plt.tight_layout()
    plt.show()


# Morning / Noon / Night Separately
def plotting_2(df, df2):
    stat = calc(df)
    day = df[:, 0].astype('U')
    # print(day)

    # plot part
    gs = gridspec.GridSpec(3, 1)
    plt.style.use('ggplot')

    # fig 1
    ax1 = plt.subplot(gs[0, :])
    ax1.plot(day[66:, ],
             df[66:, 1],
             linewidth=4,
             label='Morning {}\n std {}'.format(stat['avgMorning'], stat['stdMorning']),
             alpha=0.7)
    ax1.set(ylabel='Time(min)')
    ax1.tick_params(axis='x')
    ax1.axhline(stat['avgMorning'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    # ax1.tick_params(axis='x', labelrotation=45)
    ax1.xaxis.set_major_locator(MultipleLocator(12))
    ax1.legend()

    # fig 2
    ax2 = plt.subplot(gs[1, :])
    ax2.plot(day[66:, ],
             df[66:, 2],
             linewidth=3,
             label='Noon {}\n std {}'.format(stat['avgNoon'], stat['stdNoon']),
             alpha=0.7)
    ax2.set(ylabel='Time(min)')
    ax2.tick_params(axis='x')
    ax2.axhline(stat['avgNoon'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    # ax2.tick_params(axis='x', labelrotation=45)
    ax2.xaxis.set_major_locator(MultipleLocator(12))
    ax2.legend()

    # fig 3
    ax3 = plt.subplot(gs[2, :])
    ax3.plot(day[66:, ],
             df[66:, 3],
             linewidth=3,
             label='Night {}\n std {}'.format(stat['avgNight'], stat['stdNight']),
             alpha=0.7)
    ax3.set(ylabel='Time(min)')
    ax3.tick_params(axis='x')
    ax3.axhline(stat['avgNight'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    # ax3.tick_params(axis='x', labelrotation=45)
    ax3.xaxis.set_major_locator(MultipleLocator(12))
    ax3.legend()

    plt.tight_layout()
    plt.show()


# Job Count
def plotting_3(df, df2):
    stat = calc(df)
    day = df[:, 0].astype('U')
    # print(day)

    # plot part
    gs = gridspec.GridSpec(1, 1)
    plt.style.use('ggplot')

    ax1 = plt.subplot(gs[0, 0])
    ax1.bar(day, df[:, 5], label='Job per day', alpha=0.9)
    ax1.bar(day, df[:, 6], label='Impt Job per day', color='goldenrod')
    ax1.plot(day,
             df2[:, 1],
             linestyle='-',
             linewidth=4,
             label='7 days SMA',
             color='saddlebrown',
             alpha=0.7)
    ax1.plot(day,
             df2[:, 2],
             linestyle='-',
             linewidth=4,
             label='7 days SMA of Impt',
             color='saddlebrown',
             alpha=0.7)
    ax1.axhline(stat['avgJob'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    ax1.axhline(stat['avgJob'],
                linewidth=2.0,
                linestyle='--',
                color='chocolate',
                alpha=0.5)
    ax1.set(ylabel='job counts')
    ax1.tick_params(axis='x', labelrotation=45)
    ax1.set_title('Avg Job: {} / Avg Impt Job: {}'.format(
        stat['avgJob'], stat['avgJob_impt']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    ax1.xaxis.set_major_locator(MultipleLocator(6))
    ax1.legend()

    plt.tight_layout()
    plt.show()


# Job Count Block
def plotting_block(df, df2):
    stat = calc(df, block=True)
    NO = np.arange(len(df))

    # plot part
    # gs = gridspec.GridSpec(1, 1)
    gs = gridspec.GridSpec(2, 1)
    plt.style.use('ggplot')

    ax1 = plt.subplot(gs[0, 0])
    ax1.bar(NO, df[:, 4], label='Avg job per 12 days', alpha=0.9)
    ax1.bar(NO, df[:, 5], label='Avg impt job per 12 days', color='goldenrod')
    ax1.axhline(stat['avgJob'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    ax1.axhline(stat['avgJob'],
                linewidth=2.0,
                linestyle='--',
                color='chocolate',
                alpha=0.5)
    ax1.set(ylabel='job counts')
    ax1.tick_params(axis='x', labelrotation=45)
    ax1.set_title('Avg Job: {} / Avg Impt Job: {}'.format(
        stat['avgJob'], stat['avgJob_impt']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    # ax1.xaxis.set_major_locator(MultipleLocator(6))
    ax1.legend()

    # fig 2
    ax2 = plt.subplot(gs[1, 0])
    ax2.bar(NO, df[:, 3], label='Avg total time per 12 days', alpha=0.9)
    ax2.plot(NO,
             df2[:, 0],
             linestyle='-',
             linewidth=4,
             label='3 block of SMA',
             color='saddlebrown',
             alpha=0.7)
    ax2.axhline(stat['avgTotalTime'],
                linewidth=2.0,
                linestyle='--',
                color='orangered',
                alpha=0.5)
    ax2.set(ylabel='Time(min)')
    ax2.tick_params(axis='x', labelrotation=45)
    ax2.set_title('Avg Time (min): {}'.format(stat['avgTotalTime']),
                  fontsize=12,
                  fontweight='bold',
                  color='saddlebrown')
    # ax2.xaxis.set_major_locator(MultipleLocator(6))
    ax2.legend()

    plt.tight_layout()
    plt.show()
