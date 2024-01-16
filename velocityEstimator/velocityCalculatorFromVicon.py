import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('your_file.csv')

df['vx'] = df['x'].diff() / df['时间'].diff()
df['vy'] = df['y'].diff() / df['时间'].diff()
df['vz'] = df['z'].diff() / df['时间'].diff()

plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.plot(df['时间'], df['vx'], label='vx')
plt.legend()
plt.title('X轴速度')

plt.subplot(3, 1, 2)
plt.plot(df['时间'], df['vy'], label='vy', color='orange')
plt.legend()
plt.title('Y轴速度')

plt.subplot(3, 1, 3)
plt.plot(df['时间'], df['vz'], label='vz', color='green')
plt.legend()
plt.title('Z轴速度')

plt.tight_layout()
plt.show()
