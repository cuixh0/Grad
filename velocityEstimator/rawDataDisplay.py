"""
Project: smartphoneVelocityEstimator
Author: Cui

This file: Display velocity chart according to the rawDataFile in the filePath. 

Usage: python velocityCalculator.py subfilePath1 subfilePath2. For example python rawDataDisplay.py swing data1
"""

import os 
import sys
import pandas as pd
import matplotlib.pyplot as plt

def saveRawData(filePath):

    # 读取CSV文件
    df = pd.read_csv(os.path.join(filePath, 'Accelerometer.csv'))

    # 提取所需的列数据
    seconds_elapsed = df['seconds_elapsed']
    x = df['x']
    y = df['y']
    z = df['z']

    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.plot(seconds_elapsed, x, label='X')
    plt.plot(seconds_elapsed, y, label='Y')
    plt.plot(seconds_elapsed, z, label='Z')

    # 添加标签和标题
    plt.xlabel('Seconds Elapsed')
    plt.ylabel('Value')
    plt.title('XYZ Data Over Time')

    # 添加图例
    plt.legend()

    # 保存图片
    plt.savefig(os.path.join(filePath, 'rawData.png'))

    # 显示图表
    # plt.show()

if __name__ == "__main__":
    # 读取CSV文件
    df = pd.read_csv(os.path.join('./sensorData', sys.argv[1], sys.argv[2], 'Accelerometer.csv'))

    # 提取所需的列数据
    seconds_elapsed = df['seconds_elapsed']
    x = df['x']
    y = df['y']
    z = df['z']

    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.plot(seconds_elapsed, x, label='X')
    plt.plot(seconds_elapsed, y, label='Y')
    plt.plot(seconds_elapsed, z, label='Z')

    # 添加标签和标题
    plt.xlabel('Seconds Elapsed')
    plt.ylabel('Value')
    plt.title('XYZ Data Over Time')

    # 添加图例
    plt.legend()

    # 显示图表
    plt.show()