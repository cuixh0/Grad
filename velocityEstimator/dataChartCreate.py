"""
Project: smartphoneVelocityEstimator
Author: Cui

This file: Save velocity, rawData and frequencySpectrum charts of all files in sensorData directory
sensorData struct:
    ./sensorData
        - browse
            - data1
                - Accelerometer.csv
                - AccelerometerUncalibrated.csv
                - Metadata.csv
        - call 
            - data1
        - pocket
            - data1
        - swing 
            - data1

Usage: 
    - python dataChartCreate.py        save charts of all files in sensorData
    or
    - python dataChartCreate.py subfilePath1 subfilePath2.     save charts of sensorData/subfilePath1/subfilePath2/Accelerometer.csv

"""

import os
import sys
from velocityCalculator import saveVelocity
from frequencySpectrum import saveFrequencySpectrum
from rawDataDisplay import saveRawData

def saveChart(filePath):
    saveVelocity(filePath)
    saveFrequencySpectrum(filePath)
    saveRawData(filePath)

def processSensorData():
    # 遍历sensorData目录下的4个子目录
    for category in ['swing', 'browse', 'pocket', 'call']:
        category_path = os.path.join('./sensorData', category)

        # 遍历每个子目录
        for data_folder in os.listdir(category_path):
            data_folder_path = os.path.join(category_path, data_folder)

            # 检查是否是目录
            if os.path.isdir(data_folder_path):
                # 获取data文件夹下文件数量
                num_files = len(os.listdir(data_folder_path))

                # 如果文件数量等于3，则处理该文件夹
                if num_files < 7:
                    saveChart(data_folder_path)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        filePath = os.path.join('./sensorData', sys.argv[1], sys.argv[2])
        saveVelocity(filePath)
        saveFrequencySpectrum(filePath)
        saveRawData(filePath)
    else:
        processSensorData()