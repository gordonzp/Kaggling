### import data from internet by pandas
import matplotlib.pyplot as plt
import pandas
from pandas.tools.plotting import scatter_matrix
url = "https://goo.gl/vhm1eU"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

data = pandas.read_csv(url, names=names)

print(type(data)) #<class 'pandas.core.frame.DataFrame'>

print(data[:10])

#   preg  plas  pres  skin  test  mass   pedi  age  class
#0     6   148    72    35     0  33.6  0.627   50      1
#1     1    85    66    29     0  26.6  0.351   31      0
#2     8   183    64     0     0  23.3  0.672   32      1
#3     1    89    66    23    94  28.1  0.167   21      0
#4     0   137    40    35   168  43.1  2.288   33      1
#5     5   116    74     0     0  25.6  0.201   30      0
#6     3    78    50    32    88  31.0  0.248   26      1
#7    10   115     0     0     0  35.3  0.134   29      0
#8     2   197    70    45   543  30.5  0.158   53      1
#9     8   125    96     0     0   0.0  0.232   54      1

#scatter_matrix(data)
plt.show()
