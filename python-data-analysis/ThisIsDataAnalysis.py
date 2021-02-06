import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 144, 77, 578, 973]
custom = [1, 5, 25, 13, 23232]

BabyDataSet = list(zip(names, births))
df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

df.head()

## pandas ##

df.dtypes
# Names  Births
# 0      Bob     968
# 1  Jessica     144
# 2     Mary      77
# 3     John     578
# 4      Mel     973

df.index
#RangeIndex(start=0, stop=5, step=1)

df.columns
#Index(['Names', 'Births'], dtype='object')

df['Names']
# 0        Bob
# 1    Jessica
# 2       Mary
# 3       John
# 4        Mel
# Name: Names, dtype: object

df[0:3]
#     Names  Births
# 0      Bob     968
# 1  Jessica     144
# 2     Mary      77

df[df['Births'] > 100]
# 0,1,3,4

df.mean()
# Births    548.0
#dtype: float64

## numpy ##

arr1 = np.arange(15).reshape(3, 5)
arr1
# array([[ 0,  1,  2,  3,  4],
#        [ 5,  6,  7,  8,  9],
#        [10, 11, 12, 13, 14]])

arr1.shape
# (3,5)
arr1.dtype
# dtype('int32')
arr3 = np.zeros((3, 4))
arr3
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])
arr4 = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.float64)

arr5 = np.array([
    [7, 8, 9],
    [10, 11, 12]
], dtype=np.float64)

print(arr4+arr5, "\n")
# [[ 8. 10. 12.]
#  [14. 16. 18.]]
print(arr4-arr5, "\n")
# [[-6. -6. -6.]
#  [-6. -6. -6.]]
print(arr4*arr5, "\n")
# [[ 7. 16. 27.]
#  [40. 55. 72.]]
print(arr4/arr5, "\n")
# [[0.14285714 0.25       0.33333333]
#  [0.4        0.45454545 0.5       ]]

## Matplotlib ##

# %matplotlib inline
y = df['Births']
x = df['Names']

plt.bar(x, y)  # 막대 그래프 객체 생성
plt.xlabel('Nmaes')  # x축 제목
plt.ylabel('Births')  # y축 제목
plt.title('Bar plot')  # 그래프 제목
plt.show()  # 그래프 출력

np.random.seed(19920613)

x = np.arange(0.0, 100.0, 5.0)
y = (x * 1.5) + np.random.rand(20) * 50

plt.scatter(x, y, c="b", alpha=0.5, label="scatter point")
plt.xlabel
plt.ylabel
plt.legend(loc='upper left')
plt.title('Scatter plot')
plt.show()

# ========================Cp 1=============================
