from tools.Analysis import *
# from tools.Analysis_plotting import *
from tools.Analysis_plotting_3m import plotting_3m


# Normal report
def report():
    # df, df2 = analysis(open_file('Tim.md'), timerage='all')
    # plotting_3m(df, df2, style=0, timerage='all')
    df, df2 = analysis(open_file('Tim.md'), timerage='3m')
    plotting_3m(df, df2, style=0, timerage='3m')
    df, df2 = analysis(open_file('Tim.md'), timerage='1b')
    plotting_3m(df, df2, style=1, timerage='1b')
    # plotting(df, df2)
    # plotting_2(df, df2)
    # plotting_3(df, df2)

# This is abandoned
# def report_block():
#     # block, block2 = analysis_block(gen_buffer=True)
#     block, block2 = analysis_block()
#     plotting_block(block, block2)

# Update Buffer csv
def gen_buffer():
    analysis(open_file('./Tim.md'),
             use_buffer=True,
             gen_buffer=True)


report()
# report_block()
# gen_buffer()
