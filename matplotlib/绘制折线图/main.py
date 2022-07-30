from matplotlib import pyplot as plt

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)
x = range(2, 26, 2)

y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 绘图
plt.plot(x, y)
# 设置x轴的刻度
plt.xticks(ticks=range(2, 25))
# plt.savefig("ccc.svg")

# 展示图形
plt.show()
