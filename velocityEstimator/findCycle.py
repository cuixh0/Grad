# import stumpy
# import numpy as np
# import matplotlib.pyplot as plt

# # 生成示例时间序列数据
# np.random.seed(42)
# time_series = np.random.rand(100)

# # 使用 stumpy 中的 stump 函数计算 Matrix Profile
# m = 10  # 子序列长度
# matrix_profile = stumpy.stump(time_series, m)

# # 从 Matrix Profile 中找到最相似的子序列索引
# motif_idx = np.argmin(matrix_profile[:, 0])

# # 可视化原始时间序列和找到的最相似子序列
# plt.plot(time_series, label='Original Time Series')
# plt.plot(range(motif_idx, motif_idx + m), time_series[motif_idx:motif_idx + m], label='Motif', linewidth=2)
# plt.legend()
# plt.show()



import stumpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 从CSV文件导入时间序列数据
# 假设CSV文件的第三列是时间序列数据
file_path = './sensorData/swing/data1/Accelerometer.csv'  # 请替换为你的CSV文件路径
df = pd.read_csv(file_path)
time_series = df.iloc[:, 2].values  # 假设第三列是时间序列数据

# 使用 stumpy 中的 stump 函数计算 Matrix Profile
m = 100  # 子序列长度
matrix_profile = stumpy.stump(time_series, m)

# 从 Matrix Profile 中找到最相似的子序列索引
motif_idx = np.argmin(matrix_profile[:, 0])

# 可视化原始时间序列和找到的最相似子序列
plt.plot(time_series, label='Original Time Series')
plt.plot(range(motif_idx, motif_idx + m), time_series[motif_idx:motif_idx + m], label='Motif', linewidth=2)
plt.legend()
plt.show()

