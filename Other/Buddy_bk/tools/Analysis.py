import os
from pathlib import Path
import numpy as np


job_impt_li = ['Paper', 'Math', 'Info', 'Jogging', 'Workout']

# open file Tim.md
def open_file(n):
    curPATH = Path(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    PATH = curPATH.parent
    # print(curPATH, PATH)
    os.chdir(PATH)
    file = open(n, mode='r', encoding='utf-8')
    return file


def moving_average(data_set, periods=3, block=False):
    weights = np.ones(periods) / periods
    SMA = np.convolve(data_set, weights, mode='valid')
    if block:
        SMA = np.pad(SMA, (2, 0))
    else:
        # SMA = np.insert(SMA, [0, 0, 0, 0, 0, 0], 0)
        SMA = np.pad(SMA, (6, 0), mode='constant')
    return SMA


def grouped_avg(df, N=12):
    res = np.cumsum(df, 0)[N - 1::N] / float(N)
    res[1:] = res[1:] - res[:-1]
    return res


def analysis(file, use_buffer=True, gen_buffer=False, gen_SMA=True, timerage='1b'):
    # header = [
    #     "Day", "Morning", "Noon", "Night", "totalTime",
    #     "jobCount", "jobCount_impt"
    # ]
    #     "SMA_Time", "SMA_Job", "SMA_Job_impt"

    if use_buffer:
        # df = np.genfromtxt('./tools/buffer.csv', delimiter=',', skip_header=1)
        df = np.genfromtxt('./tools/buffer.csv', delimiter=',')
        df = df.astype('int32')
    else:
        df = np.empty((0, 7))

    for line in file:
        if '##' in line:
            Day = line.split(' ')[1]
            Day = Day.split('\n')[0]
            # print(Day)
            jobCount = 0
            jobCount_impt = 0
            isEmpty = False

        elif 'Time of Study:' in line and 'min' in line:
            rawTime = line.split(' ')[3]
            rawTime = rawTime.split('+')
            # print(rawTime, len(rawTime), type(rawTime))
            # if rawTime[-2:] == '\n':
            #     rawTime = rawTime.split('\n')[0]
            if rawTime[-1] == 'xxx':
                isEmpty = True

        elif not isEmpty:
            if '[x]' in line:
                jobCount += 1
                if any(item in line for item in job_impt_li):
                    jobCount_impt += 1

            elif 'Random thoughts' in line:
                try:
                    Morning = int(rawTime[0])
                    Noon = int(rawTime[1])
                    Night = int(rawTime[2])
                    totalTime = Morning + Noon + Night
                    df = np.append(df,
                                   np.array([[
                                       Day, Morning, Noon, Night, totalTime,
                                       jobCount, jobCount_impt
                                   ]]),
                                   axis=0)
                    isEmpty = True

                    # if len(rawTime) == 4:
                    #     totalTime = int(rawTime[-1])
                    #     df = np.append(
                    #         df,
                    #         np.array(
                    #             [[Day, 0, 0, 0, totalTime, jobCount, jobCount_impt]]),
                    #         axis=0,
                    #     )
                    # else:
                    #     Morning = int(rawTime[0])
                    #     Noon = int(rawTime[1])
                    #     Night = int(rawTime[2])
                    #     totalTime = Morning + Noon + Night
                    #     df = np.append(df,
                    #                    np.array([[
                    #                        Day, Morning, Noon, Night, totalTime,
                    #                        jobCount, jobCount_impt
                    #                    ]]),
                    #                    axis=0)
                except:
                    print('Error!', Day, rawTime)
        else:
            continue

    # print(df[-5:])

    if gen_buffer:
        df = df.astype('int32')
        # np.savetxt('./tools/buffer_.csv', df, delimiter=",")
        with open("./tools/buffer_.csv", "wb") as f:
            np.savetxt(f, df.astype(int), fmt='%i', delimiter=",")

    if gen_SMA:
        # We want SMA of last 3M, we need prior data (90+12 is enough)
        # We want SMA of last 1B, we need prior data (12+12 is enough)
        if timerage == '3m':
            df = df[-110:, :]
        if timerage == '1b':
            df = df[-30:, :]
        # SMA
        df = df.astype('int32')
        # print(df)

        SMA_Time = moving_average(df[:, 4], 7)
        SMA_Job = moving_average(df[:, 5], 7)
        SMA_Job_impt = moving_average(df[:, 6], 7)

        df2 = np.concatenate((SMA_Time[:, None], SMA_Job[:, None]), axis=1)
        df2 = np.concatenate((df2, SMA_Job_impt[:, None]), axis=1)
        # print(df2)
        if timerage == '3m':
            df = df[-90:, :]
            df2 = df2[-90:, :]
        if timerage == '1b':
            df = df[-12:, :]
            df2 = df2[-12:, :]
        return df, df2
    else:
        if timerage == '3m':
            df = df[-90:, :]
        if timerage == '1b':
            df = df[-12:, :]
        return df


def analysis_block(use_buffer=False, gen_buffer=False, gen_SMA=True):
    # header = [
    #     "Day", "Morning", "Noon", "Night", "totalTime",
    #     "jobCount", "jobCount_impt"
    # ]

    df = analysis(open_file('Tim.md'), gen_SMA=False)
    df = df[:, 1:].astype('int32')
    block = grouped_avg(df)

    if gen_buffer:
        # block = block.astype('int32')
        # block = block.astype('float')
        with open("./tools/buffer_block_.csv", "wb") as f:
            np.savetxt(f, block.astype(int), fmt='%i', delimiter=",")

    if gen_SMA:
        # SMA
        # block = block.astype('int32')
        # block = block.astype('float')
        SMA_Time = moving_average(block[:, 3], 3, block=True)
        SMA_Job = moving_average(block[:, 4], 3, block=True)
        SMA_Job_impt = moving_average(block[:, 5], 3, block=True)

        block2 = np.concatenate((SMA_Time[:, None], SMA_Job[:, None]), axis=1)
        block2 = np.concatenate((block2, SMA_Job_impt[:, None]), axis=1)
        return block, block2
    else:
        return block
