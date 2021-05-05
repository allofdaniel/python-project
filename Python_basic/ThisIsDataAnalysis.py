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

# -*- coding: utf-8 -*-


# read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.
file_path = '../data/chipotle.tsv'
chipo = pd.read_csv(file_path, sep='\t')
print(chipo.shape)
print("------------------------------------")
print(chipo.info())

# (4622, 5)
# ------------------------------------
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4622 entries, 0 to 4621
# Data columns (total 5 columns):
#  #   Column              Non-Null Count  Dtype
# ---  ------              --------------  -----
#  0   order_id            4622 non-null   int64
#  1   quantity            4622 non-null   int64
#  2   item_name           4622 non-null   object
#  3   choice_description  3376 non-null   object
#  4   item_price          4622 non-null   object
# dtypes: int64(2), object(3)
# memory usage: 180.7+ KB
# None

# 4622 column & 5 features. choice_description : 3376 non0null object = 1246 null objects


# chipo 라는 Dataframe에서 순서대로 10개의 row 데이터를 보여줍니다.
chipo.head(10)

# result


print(chipo.columns)
print("------------------------------------")
print(chipo.index)

# Index(['order_id', 'quantity', 'item_name', 'choice_description',
#        'item_price'],
#       dtype='object')
# ------------------------------------
# RangeIndex(start=0, stop=4622, step=1)


# 가장 많이 주문한 item : top 10을 출력합니다.
item_count = chipo['item_name'].value_counts()[:10]
for idx, (val, cnt) in enumerate(item_count.iteritems(), 1):
    print("Top", idx, ":", val, cnt)

# Top 1 : Chicken Bowl 726
# Top 2 : Chicken Burrito 553
# Top 3 : Chips and Guacamole 479
# Top 4 : Steak Burrito 368
# Top 5 : Canned Soft Drink 301
# Top 6 : Steak Bowl 211
# Top 7 : Chips 211
# Top 8 : Bottled Water 162
# Top 9 : Chicken Soft Tacos 115
# Top 10 : Chips and Fresh Tomato Salsa 110


# item당 주문 개수를 출력합니다.
order_count = chipo.groupby('item_name')['order_id'].count()
order_count[:10]  # item당 주문 개수를 출력합니다.


# item당 주문 총량을 출력합니다.
item_quantity = chipo.groupby('item_name')['quantity'].sum()
item_quantity[:10]  # item당 주문 총량을 출력합니다.


# data visualization
%matplotlib inline

item_name_list = item_quantity.index.tolist()
x_pos = np.arange(len(item_name_list))
order_cnt = item_quantity.values.tolist()

plt.bar(x_pos, order_cnt, align='center')
plt.ylabel('ordered_item_count')
plt.title('Distribution of all orderd item')

plt.show()

# mini quiz : what is difference between pandas.value_count() and pandas.unique()??

print(chipo['item_name'].value_counts()[:10])

# Chicken Bowl                    726
# Chicken Burrito                 553
# Chips and Guacamole             479
# Steak Burrito                   368
# Canned Soft Drink               301
# Steak Bowl                      211
# Chips                           211
# Bottled Water                   162
# Chicken Soft Tacos              115
# Chips and Fresh Tomato Salsa    110
# Name: item_name, dtype: int64

print(type(chipo['item_name'].value_counts()))

# <class 'pandas.core.series.Series'>

print(chipo['item_name'].unique()[:10])

# ['Chips and Fresh Tomato Salsa' 'Izze' 'Nantucket Nectar'
#  'Chips and Tomatillo-Green Chili Salsa' 'Chicken Bowl' 'Side of Chips'
#  'Steak Burrito' 'Steak Soft Tacos' 'Chips and Guacamole'
#  'Chicken Crispy Tacos']
# In [16]:

print(type(chipo['item_name'].unique()))

# <class 'numpy.ndarray'>

# value_counts는 series. unique는 ndarray. (vc는 각 변수에 맞는 값을 보여주고, un는 각 변수들을 나열해 준다.)

# 데이터 전처리
print(chipo.info())
print('-------------')
chipo['item_price'].head()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 4622 entries, 0 to 4621
# Data columns (total 5 columns):
# order_id              4622 non-null object
# quantity              4622 non-null int64
# item_name             4622 non-null object
# choice_description    3376 non-null object
# item_price            4622 non-null object
# dtypes: int64(1), object(4)
# memory usage: 180.6+ KB
# None
# -------------
# Out[17]:
# 0     $2.39
# 1     $3.39
# 2     $3.39
# 3     $2.39
# 4    $16.98
# Name: item_price, dtype: object

# column 단위 데이터에 apply 함수로 전처리를 적용합니다.( $를 없애기 위해 appy(lambda.. 함수 이용하여, 뒤의 함수만 적용.))
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
chipo.describe()
