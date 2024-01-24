"""
Project: smartphoneVelocityEstimator
Author: Cui

This file: Display velocity chart according to the rawDataFile in the filePath. 

Usage: python velocityCalculator.py subfilePath1 subfilePath2. For example python velocityCalculator.py swing data1
"""

import os 
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def saveVelocity(filePath):
    # 读取CSV文件
    df = pd.read_csv(os.path.join(filePath, 'Accelerometer.csv'))

    # 筛选seconds_elapsed值大于2的数据
    df_filtered = df[df['seconds_elapsed'] > 2 & (df['seconds_elapsed'] < 14)]

    # 计算速度（通过对加速度积分）
    dt = df_filtered['seconds_elapsed'].diff()
    vx = df_filtered['x'].cumsum() * dt
    vy = df_filtered['y'].cumsum() * dt
    vz = df_filtered['z'].cumsum() * dt

    # 绘制速度图表
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtered['seconds_elapsed'], vx, label='Vx')
    plt.plot(df_filtered['seconds_elapsed'], vy, label='Vy')
    plt.plot(df_filtered['seconds_elapsed'], vz, label='Vz')

    # 添加标签和标题
    plt.xlabel('Seconds Elapsed')
    plt.ylabel('Velocity')
    plt.title('Velocity Over Time')

    # 添加图例
    plt.legend()

    plt.savefig(os.path.join(filePath, 'velocity.png'))

    # 显示图表
    # plt.show()



# 未消除误差累积
# if __name__ == "__main__":

#     # filePath = './sensorData/'
#     # 读取CSV文件
#     df = pd.read_csv(os.path.join('./sensorData', sys.argv[1], sys.argv[2], 'Accelerometer.csv'))

#     # 筛选seconds_elapsed值大于2的数据
#     df_filtered = df[df['seconds_elapsed'] > 2 & (df['seconds_elapsed'] < 14)]

#     # 计算速度（通过对加速度积分）
#     dt = df_filtered['seconds_elapsed'].diff()
#     vx = df_filtered['x'].cumsum() * dt
#     vy = df_filtered['y'].cumsum() * dt
#     vz = df_filtered['z'].cumsum() * dt

#     # 绘制速度图表
#     plt.figure(figsize=(10, 6))
#     plt.plot(df_filtered['seconds_elapsed'], vx, label='Vx')
#     plt.plot(df_filtered['seconds_elapsed'], vy, label='Vy')
#     plt.plot(df_filtered['seconds_elapsed'], vz, label='Vz')

#     # 添加标签和标题
#     plt.xlabel('Seconds Elapsed')
#     plt.ylabel('Velocity')
#     plt.title('Velocity Over Time')

#     # 添加图例
#     plt.legend()

#     # 显示图表
#     plt.show()



## 消除误差累积
# if __name__ == "__main__":
#     # filePath = './sensorData/'
#     # 读取CSV文件
#     df = pd.read_csv(os.path.join('./sensorData', sys.argv[1], sys.argv[2], 'Accelerometer.csv'))
#     # df = pd.read_csv(os.path.join('./velocityEstimator/sensorData/swing/data1/', 'Accelerometer.csv'))

#     # 筛选seconds_elapsed值大于2的数据
#     df_filtered = df[(df['seconds_elapsed'] > 3) & (df['seconds_elapsed'] < 15)]

#     # 初始化速度为零
#     vx = 0
#     vy = 0
#     vz = 0

#     # 存储极小值点的索引
#     minima_indices_x = []
#     minima_indices_y = []
#     minima_indices_z = []

#     # 存储每一步的速度
#     velocities_x = []
#     velocities_y = []
#     velocities_z = []

#     vxindex = 0
#     # 逐行处理数据
#     pret = 0
#     flag = 1   # 1 +, 0 -
#     for index, row in df_filtered.iterrows():
#         # 计算时间差异
#         dt = row['seconds_elapsed']
#         if vxindex == 0:
#             vxindex = index + 1
#             pret = dt
#             continue 
#         # 速度积分
#         vx += row['x'] * (dt - pret)
#         vy += row['y'] * (dt - pret)
#         vz += row['z'] * (dt - pret)
#         pret = dt

#         # 判断是否达到速度的极小值
#         if index > 0 and index < len(df_filtered) - 1:
#             if len(velocities_x) > 1:
#                 if vx < velocities_x[index - vxindex - 1] and velocities_x[index - vxindex - 1] > velocities_x[index - vxindex - 2]:
#                     vx = 0
#                     minima_indices_x.append(index)

#                 if vy > velocities_y[index - vxindex - 1] and velocities_y[index - vxindex - 1] < velocities_y[index -vxindex - 2]:
#                     vy = 0
#                     minima_indices_y.append(index)

#                 if vz < velocities_z[index - vxindex - 1] and velocities_z[index - vxindex - 1] > velocities_z[index - vxindex - 2]:
#                     vz = 0
#                     minima_indices_z.append(index)

#         velocities_x.append(vx)
#         velocities_y.append(vy)
#         velocities_z.append(vz)

#     velocities_x.append(0)
#     velocities_y.append(0)
#     velocities_z.append(0)

#     # 将生成的消除误差累积的数据保存到文件
#     csv_file_name = './noCumulativeErrorvelocityData.csv'

#     # 将数据写入 CSV 文件
#     with open(csv_file_name, 'w', newline='') as csvfile:
#         # 创建 CSV 写入器
#         csv_writer = csv.writer(csvfile)

#         # 写入数据头
#         csv_writer.writerow(['seconds_elapsed', 'velocities_x', 'velocities_y'])

#         # 写入数据
#         for time, valuex, valuey in zip(df_filtered['seconds_elapsed'], velocities_x, velocities_y):
#             csv_writer.writerow([time, valuex, valuey])

#     # 绘制速度图表
#     plt.figure(figsize=(10, 6))
#     plt.plot(df_filtered['seconds_elapsed'], velocities_x, label='Vx')
#     plt.plot(df_filtered['seconds_elapsed'], velocities_y, label='Vy')
#     plt.plot(df_filtered['seconds_elapsed'], velocities_z, label='Vz')

#     # 标记极小值点
#     # plt.scatter(df_filtered['seconds_elapsed'].iloc[minima_indices_x], np.zeros(len(minima_indices_x)), c='red', marker='o', label='Minima Vx')
#     # plt.scatter(df_filtered['seconds_elapsed'].iloc[minima_indices_y], np.zeros(len(minima_indices_y)), c='blue', marker='o', label='Minima Vy')
#     # plt.scatter(df_filtered['seconds_elapsed'].iloc[minima_indices_z], np.zeros(len(minima_indices_z)), c='green', marker='o', label='Minima Vz')

#     # 添加标签和标题
#     plt.xlabel('Seconds Elapsed')
#     plt.ylabel('Velocity')
#     plt.title('Velocity Over Time')

#     # 添加图例
#     plt.legend()
#     plt.ylim(-10, 10)
#     # 显示图表
#     plt.show()
































class RealTimeVelocityPlot:
    def __init__(self):
        self.timeValues = []
        self.velocity = []
        self.smoothVelocity1 = []
        self.smoothVelocity2 = []
        # 初始化图形
        plt.ion()  # 打开交互模式
        self.fig, self.ax = plt.subplots()
        #self.velocityLine, = self.ax.plot([], [], label='Realtime velocity Wave')
        self.smoothVelocityLine1, = self.ax.plot([], [], label='Velocity Wave1')
        #self.smoothVelocityLine2, = self.ax.plot([], [], label='Velocity Wave2')
        self.ax.legend()


    def update_plot(self, newTime, newVelocity, newSmoothVelcity1, newSmoothVelcity2):

        # 添加新数据点
        self.timeValues.append(newTime)
        self.velocity.append(newVelocity)
        self.smoothVelocity1.append(newSmoothVelcity1)
        self.smoothVelocity2.append(newSmoothVelcity2)

        # 更新图形
        #self.velocityLine.set_data(self.timeValues, self.velocity)
        self.smoothVelocityLine1.set_data(self.timeValues, self.smoothVelocity1)
        #self.smoothVelocityLine2.set_data(self.timeValues, self.smoothVelocity2)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.flush_events()


if __name__ == "__main__":
    velocityPlot = RealTimeVelocityPlot()
    df = pd.read_csv(os.path.join('./sensorData', sys.argv[1], sys.argv[2], 'Accelerometer.csv'))
    df_filtered = df[(df['seconds_elapsed'] > 2) & (df['seconds_elapsed'] < 14)]
    
    # filepath to save velocity
    # 提取列数据

    dt = df_filtered['seconds_elapsed'].diff().values.tolist()
    vy = (df_filtered['y'].cumsum() * dt).tolist()
    time = 0

    flag = 0
    pretime = 0
    prevy = 0
    k = 0.1    # 斜率
    sub = 0

    vy2 = 0

    csv_file_name = './noCumulativeErrorvelocityData.csv'




            

    with open(csv_file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['time', 'rawVelocities','velocities_y1', 'velocities_y2'])
        
        for i in range(1, len(dt)):

            csv_writer.writerow([time, vy[i], vy[i] - sub - k * (time - pretime), vy[i] - sub])
        
            velocityPlot.update_plot(time, vy[i], vy[i] - sub - k * (time - pretime), vy[i] - sub)
            time += dt[i]

            if i > 2 and i < len(dt) - 1 and time - pretime > 0.1 and vy[i] < vy[i + 1] and vy[i] < vy[i - 1]:
                k = (vy[i] - prevy) / (time - pretime)
                prevy = vy[i]
                pretime = time
                sub = vy[i]

            # plt.pause(0.01)  # 暂停一段时间，模拟实时更新

        plt.ioff()
        plt.show()












    



