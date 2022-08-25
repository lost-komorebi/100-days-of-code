#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

import numpy as np
import pandas as pd

df = pd.read_csv('payscale_data.csv')
pd.set_option('display.max_columns', None)  # display all columns
pd.set_option('display.max_rows', None)  # display all rows

print(df.head())  # get the first five rows
print(df.tail())  # get the last five rows
print(df.shape)  # get row_num, column_num of df
print(df.columns)  # get column labels

print(df.isna())  # check if any Nan exists
cleaned_df = df.dropna()  # clean the data
print(cleaned_df.shape)  # get rows and columns of cleaned_df

print(cleaned_df["Major"])  # get single column
print(cleaned_df[["Major", "Degree Type"]])  # get multiple columns

print(cleaned_df["Major"][100])  # get cell
print(cleaned_df["Major"].loc[100])


def clean_currency(x):
    if isinstance(x, str):
        return int(x.replace('$', '').replace(',', ''))


def clean_percentage(x):
    if isinstance(x, str):
        x = x.replace('%', '')
        if x == '-':
            return np.NaN
        return int(x)


def add_currency(x):
    if isinstance(x, int):
        return '${:,.0f}'.format(x)


print(cleaned_df["Early Career Pay"].max())  # get max value
print(cleaned_df["Mid-Career Pay"].min())  # get min value
print(cleaned_df["Early Career Pay"].apply(
    clean_currency).idxmax())  # get id of max value
print(cleaned_df["% High Meaning"].apply(
    clean_percentage).idxmin())  # get id of min value


print(cleaned_df["Mid-Career Pay"].apply(clean_currency).sort_values())
print(cleaned_df["Early Career Pay"].apply(
    clean_currency).sort_values(ascending=False))
Spread = (
    cleaned_df["Mid-Career Pay"].apply(clean_currency) -
    cleaned_df["Early Career Pay"].apply(clean_currency)).apply(add_currency)
cleaned_df.insert(
    5,
    "Spread",
    Spread)
print(cleaned_df)


print(cleaned_df.groupby('Major').count())
print(cleaned_df.groupby('Major').mean())
