"""
Project: smartphoneVelocityEstimator
Author: Cui

This file: Display velocity chart according to the rawDataFile in the filePath. 

Usage: python velocityCalculator.py subfilePath1 subfilePath2. For example python frequencySpectrum.py swing data1
"""

import os 
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def saveFrequencySpectrum(filePath):
    # 读取CSV文件
    df = pd.read_csv(os.path.join(filePath, 'Accelerometer.csv'))

    # 筛选seconds_elapsed值大于2的数据
    df_filtered = df[(df['seconds_elapsed'] > 2) & (df['seconds_elapsed'] < 14)]

    # 分别计算x、y、z方向的加速度
    acceleration_x = df_filtered['x']
    acceleration_y = df_filtered['y']
    acceleration_z = df_filtered['z']

    # 对x、y、z方向的加速度分别进行傅里叶变换
    dt = df_filtered['seconds_elapsed'].diff().mean()

    # x方向
    n_x = len(acceleration_x)
    freq_x = np.fft.fftfreq(n_x, d=dt)
    fft_values_x = np.fft.fft(acceleration_x)

    # y方向
    n_y = len(acceleration_y)
    freq_y = np.fft.fftfreq(n_y, d=dt)
    fft_values_y = np.fft.fft(acceleration_y)

    # z方向
    n_z = len(acceleration_z)
    freq_z = np.fft.fftfreq(n_z, d=dt)
    fft_values_z = np.fft.fft(acceleration_z)

    # 绘制频率谱图
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    plt.plot(freq_x[:n_x // 2], np.abs(fft_values_x)[:n_x // 2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum - X Direction')

    plt.subplot(3, 1, 2)
    plt.plot(freq_y[:n_y // 2], np.abs(fft_values_y)[:n_y // 2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum - Y Direction')

    plt.subplot(3, 1, 3)
    plt.plot(freq_z[:n_z // 2], np.abs(fft_values_z)[:n_z // 2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum - Z Direction')
    plt.tight_layout()
    plt.savefig(os.path.join(filePath, 'frequencySpectrum.png'))
    # plt.show()


if __name__ == "__main__":
     # 读取CSV文件
    df = pd.read_csv(os.path.join('./sensorData', sys.argv[1], sys.argv[2], 'Accelerometer.csv'))

    # 筛选seconds_elapsed值大于2的数据
    df_filtered = df[(df['seconds_elapsed'] > 2) & (df['seconds_elapsed'] < 14)]

    # 分别计算x、y、z方向的加速度
    acceleration_x = df_filtered['x']
    acceleration_y = df_filtered['y']
    acceleration_z = df_filtered['z']

    # 对x、y、z方向的加速度分别进行傅里叶变换
    dt = df_filtered['seconds_elapsed'].diff().mean()

    # x方向
    n_x = len(acceleration_x)
    freq_x = np.fft.fftfreq(n_x, d=dt)
    fft_values_x = np.fft.fft(acceleration_x)

    # y方向
    n_y = len(acceleration_y)
    freq_y = np.fft.fftfreq(n_y, d=dt)
    fft_values_y = np.fft.fft(acceleration_y)

    # z方向
    n_z = len(acceleration_z)
    freq_z = np.fft.fftfreq(n_z, d=dt)
    fft_values_z = np.fft.fft(acceleration_z)

    # 绘制频率谱图
    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    plt.plot(freq_x[:n_x // 2], np.abs(fft_values_x)[:n_x // 2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum - X Direction')

    plt.subplot(3, 1, 2)
    plt.plot(freq_y[:n_y // 2], np.abs(fft_values_y)[:n_y // 2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum - Y Direction')

    plt.subplot(3, 1, 3)
    plt.plot(freq_z[:n_z // 2], np.abs(fft_values_z)[:n_z // 2])
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Frequency Spectrum - Z Direction')
    plt.tight_layout()
    plt.show()