#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import pandas as pd
import matplotlib.pyplot as plt


#pd.set_option('display.max_rows', None)
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.count())

# print(df.groupby(by='TAG').sum())
# print(df.groupby(by='TAG').sum().sort_values(by='POSTS', ascending=False).head(1))
# print(df.groupby(by=['TAG']).count())

#df['DATE'] = pd.to_datetime(df['DATE'][1])

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.index = pd.to_datetime(reshaped_df.index)
# print(reshaped_df)
# print(reshaped_df.shape)
# print(reshaped_df.columns)
# print(reshaped_df.count())

roll_df = reshaped_df.rolling(window=3).mean()


# plt.figure(figsize=(14, 8))
# plt.xticks(fontsize=20)
# plt.yticks(fontsize=20)
# plt.xlabel('Date', fontsize=20)
# plt.ylabel('Numbers of Posts', fontsize=20)
# plt.ylim(0, 35000)
# for column in roll_df.columns:
#     plt.plot(
#         roll_df.index,
#         roll_df[column],
#         linewidth=3,
#         label=reshaped_df[column].name)
# plt.legend(fontsize=15)  # place legend
# plt.show()


# find the most popular programming language from 2008 to 2012 by the number of posts
reshaped_df.insert(0, 'year', pd.DatetimeIndex(reshaped_df.index).year)
filter1 = reshaped_df['year'] >= 2008
filter2 = reshaped_df['year'] <= 2012
print(reshaped_df.where(filter1 & filter2).dropna().sum().sort_values(ascending=False).head(1))


