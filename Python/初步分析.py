import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']
np1 = np.genfromtxt('D:/Database/Python_CKHS/Python_CKHS/資料檔案/總共事故數.csv', delimiter=',')
np2 = np.genfromtxt('D:/Database/Python_CKHS/Python_CKHS/資料檔案/死亡車禍總數.csv', delimiter=',')
a = np.linspace(102, 109, 8)
plt.plot(a, np1, label = '總事故數')
plt.plot(a, np2, label = '無死亡事件總數')
plt.xlabel('年分')
plt.ylabel('事故數')
plt.title('初步分析表')
plt.grid()
plt.legend(loc='upper left')
plt.show()