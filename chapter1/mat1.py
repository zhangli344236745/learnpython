import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# n = 10
# xs = np.linspace(0,100,n)
# ys = np.linspace(100,200,n)
# zs = xs + ys
# fig,ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.scatter(xs,ys,zs,color="r")
# ax.plot(xs,ys,zs)
# plt.show()

xs = np.arange(-10, 10, 0.5)
ys = np.arange(-10, 10, 0.5)
xs, ys = np.meshgrid(xs, ys)  #生成网格坐标
zs = xs * (ys**3) - ys * (xs**3)

fig ,ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(xs,ys,zs)
plt.show()