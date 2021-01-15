import pandas as pd
import numpy as np


def call_file(year):
    path = '/Users/nathanoliver/Desktop/Python/US_Energy/csv/data_201' + \
        str(year) + '.csv'
    data = pd.read_csv(path)
    return pd.DataFrame(data)


def concat(df1, df2):
    return pd.concat((df1, df2), axis='index')


df1 = call_file(1)
df2 = call_file(2)

print(len(df1))
print(len(df2))

df = pd.concat((df1, df2), axis='index')

for i in range(3, 10):
    df2 = call_file(i)
    df = concat(df, df2)
    print(i)

df.to_csv(
    '/Users/nathanoliver/Desktop/Python/US_Energy/csv/data_final.csv', index=False)
