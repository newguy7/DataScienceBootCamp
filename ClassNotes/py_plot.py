#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

#Two  lines to make our compiler able to draw:
# plt.savefig(sys.stdout.buffer)
plt.show()
plt.savefig('output.png')
sys.stdout.flush()

# plt.plot(df.colX, df.colY)
# plt.figure() = resize chart
# plt.xticks(fontsize=14) = configure xaxis
# plt.yticks
# plt.xlabel('Date',fontsize=) = add text to x-axis
# plt.ylabel()
# plt.ylim(0,100) = set lower and upper bound
# plt.xlim=(df.Release_Date.min(), df.Release_Date.max())
# plt.show()
# plt.legend()
