import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


class RealTimeVelocityPlot:
    def __init__(self):
        self.timeValues = []
        self.velocity = []
        self.smoothVelocity = []
        # 初始化图形
        plt.ion()  # 打开交互模式
        self.fig, self.ax = plt.subplots()
        self.velocityLine, = self.ax.plot([], [], label='Realtime velocity Wave')
        self.smoothVelocityLine, = self.ax.plot([], [], label='Smooth velocity Wave')
        self.ax.legend()


    def update_plot(self, newTime, newVelocity, newSmoothVelcity):

        # 添加新数据点
        self.timeValues.append(newTime)
        self.velocity.append(newVelocity)
        self.smoothVelocity.append(newSmoothVelcity)

        # 更新图形
        self.velocityLine.set_data(self.timeValues, self.velocity)
        self.smoothVelocityLine.set_data(self.timeValues, self.smoothVelocity)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.flush_events()



if __name__ == "__main__":
    velocityPlot = RealTimeVelocityPlot()
    df = pd.read_csv('./noCumulativeErrorVelocityData.csv')
    
    # 提取列数据
    seconds_elapsed = df['time']
    velocities_y1 = df['velocities_y1']

    # 默认初始值
    smoothV, a = 2, 0
    cycle = carry = period = curdis = dis = 0.
    curStart = seconds_elapsed[0]
    maxV = 0

    flag = 0

    for i in range(1, len(velocities_y1) - 1):
        velocityPlot.update_plot(seconds_elapsed[i], velocities_y1[i], smoothV)
        curdis += velocities_y1[i] * (seconds_elapsed[i + 1] - seconds_elapsed[i])
        maxV = max(maxV, velocities_y1[i])
        if velocities_y1[i] < velocities_y1[i - 1] and velocities_y1[i] < velocities_y1[i + 1]:
            if dis != 0:
                dis = (dis + curdis) / 2
            else:
                dis = curdis
            curPeriod = seconds_elapsed[i] - curStart
            curStart = seconds_elapsed[i]
            carry = curdis - (smoothV * curPeriod + a * curPeriod * curPeriod / 2)
            curdis = 0
            if period != 0:
                period = (period + curPeriod) / 2
            else:
                period = curPeriod
            a = 2 * (dis + carry - smoothV * period) / (period * period)
        if a > 0:
            a = min(a, 1.8)
        elif a < 0:
            a = max(a, -1.8)
        if a > 0 and smoothV < maxV * 0.8 or a < 0 and smoothV > maxV * 0.1:
            smoothV += a * (seconds_elapsed[i] - seconds_elapsed[i - 1])
            
        flag += 1
        plt.pause(0.05)  # 暂停一段时间，模拟实时更新

    plt.ioff()
    plt.show()





