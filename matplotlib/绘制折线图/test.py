# 绘制10点到12点的气温
from matplotlib import pyplot as plt
import random

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 调整x轴的刻度
_x = list(x)[::20]
plt.xticks(_x, ["hello,{}".format(i) for i in _x])
plt.plot(x, y)
plt.show()
