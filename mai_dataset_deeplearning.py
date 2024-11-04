# -*- coding: utf-8 -*-
"""MAI_dataset_DeepLearning.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sQ-N4WHKU5s4qymEJcB4URhfaySF7nvR
"""

from google.colab import drive
from tensorflow.keras.layers import Conv2D, BatchNormalization, Activation, MaxPool2D, Conv2DTranspose, Concatenate, Input, Flatten,Dense
from tensorflow.keras.models import Model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

drive.mount("/content/drive")

cd /content/drive/MyDrive/MAI_dataset/open/

drive_path = "/content/drive/MyDrive/"
source_file_path = drive_path + "MAI_dataset/open/"

test_file = "test/"
train_file = "file/"
test_df = pd.read_csv('test.csv')
train_df = pd.read_csv('train.csv')

train_df.head()

train_df.columns

train_df[['ID','AL645608.7','HES4']]

import seaborn as sns
from matplotlib.ticker import MaxNLocator
fig=plt.figure(figsize=(10,3), dpi=100)
ax1=fig.subplots()
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
sns.lineplot(data = train_df, x='ID', y = 'AL645608.7', ci = None, ax = ax1)
ax1.legend(bbox_to_anchor=(1.02,1), loc=2)

column_index = train_df.columns.get_loc('AL645608.7')

id_column_index = 0
max_value = train_df['AL645608.7'].max()
max_row = train_df[train_df['AL645608.7'] == max_value]

for index, row in max_row.iterrows():
  print(f"ID: {row[id_column_index]}, AL645608.7: {row['AL645608.7']}")
# AL645608.7 열의 최댓값과 그 최댓값을 갖고 있는 ID를 출력해주는 코드

top_100_al645608 = train_df.nlargest(100, 'AL645608.7')

for index, row in top_100_al645608.iterrows():
  print(f"ID: {row[id_column_index]}, AL645608.7: {row['AL645608.7']}")
  #AL645608.7의 최댓값 100개를 보여주는 코드

top_100_HES4 = train_df.nlargest(100, 'HES4')
for index, row in top_100_HES4.iterrows():
  print(f"ID:{row[id_column_index]}, HES4: {row['HES4']}")
  #HES4의 최댓값 100개를 보여주는 코드

common = pd.merge(top_100_al645608, top_100_HES4, on='ID', suffixes=('_al645608', '_HES4'))  # suffixes를 사용하여 열 이름 변경 방지

for index, row in common.iterrows():
    print(f"ID: {row['ID']}, AL645608.7: {row['AL645608.7_al645608']}, HES4: {row['HES4_HES4']}") # 수정된 열 이름 사용

# 결과 상 둘다 TOP 100에 들어가는 경우는 1번의 불과함 -> 상관관계 낮다? 확인해봐야함

correlation = train_df[['AL645608.7','HES4']].corr().iloc[0,1]
print(f"Correlation between AL645608.7 and HES4:{correlation}")
#상관관계 0.023686481934577088

correlation = train_df[['AL645608.7','TNFRSF18']].corr().iloc[0,1]
print(f"Correlation between AL645608.7 and TNFRSF18:{correlation}")
#상관관계 -0.0012670017685664746

# 모든 열 간의 상관관계 계산
correlation_matrix = train_df.drop(columns=['ID','path']).corr()

print("Correlation matrix:")
print(correlation_matrix)

correlation_matrix_10 = correlation_matrix.iloc[:10,:10]
# 마스크 생성: 주 대각선 위치를 True로 설정
np.fill_diagonal(correlation_matrix_10.values, np.nan)
sns.heatmap(correlation_matrix_10, annot=True, fmt=".4f", cmap = 'coolwarm', square=True)
plt.title('correlation Matrix')
plt.show()
