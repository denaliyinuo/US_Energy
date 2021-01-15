import pandas as pd
import matplotlib.pyplot as plt


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

# import files


file_name = 'ieee_30'

path = '/Users/nathanoliver/Desktop/Python/US_Energy/csv/data_final.csv'

df = read_file(path)

print(df.columns)


res_wasted = []
res_used = []
res_total = []

# wasted energy

df1 = df.copy()

df2 = df1[df1['category'] == 'rejected energy']
df3 = df1[df1['category'] == 'energy services']

for i in range(len(df2)):
    res_wasted.append(df2())


print(df2)
print(df3)

plt.plot(df2['residential'])
plt.plot(df3['residential'])
plt.show()
