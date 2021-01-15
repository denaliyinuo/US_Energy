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

for year in range(2011, 2016):
    print(year)
    df1 = df1[df1['year'] != year]

df1 = df1.drop(columns='electricity generation')
print(df1)

# # plt.plot(df2['residential'])
# plt.show()


# fig = plt.figure(figsize = (15, 10))


# t1 = x['Solar Energy Generation (terawatt-hours)']
# t2 = x['Solar Energy Generation (terawatt-hours)'] + x['Wind Energy Generation (terawatt-hours)']
# t3 = x['Solar Energy Generation (terawatt-hours)'] + x['Wind Energy Generation (terawatt-hours)'] +x['Hydropower Energy Generation (terawatt-hours)']
# t4 = x['Solar Energy Generation (terawatt-hours)'] + x['Wind Energy Generation (terawatt-hours)'] +x['Hydropower Energy Generation (terawatt-hours)']+ x['Nuclear Energy Generation (terawatt-hours)']

width = .1

sector = ['residential', 'commercial', 'industrial']

energy = ['natural gas', 'petroleum', 'coal', 'biomass']

color = ['#87ceeb', '#964B00', 'black', 'green']

df2 = df1[df1['category'] == energy[0]]
df3 = df1[df1['category'] == energy[1]]
df4 = df1[df1['category'] == energy[2]]
df5 = df1[df1['category'] == energy[3]]

factor = 2

shift = [-.1 * factor, 0, .1 * factor]

print(shift)


def reset_index(df):
    df = df.reset_index(drop=True)

    return df


df2 = reset_index(df2)
df3 = reset_index(df3)
df4 = reset_index(df4)
df5 = reset_index(df5)

print(df2[sector[0]])

print(df3[sector[0]])


for i in range(3):
    print(i)
    plt.bar(df2['year'] + shift[i], df2[sector[i]],
            color=color[0], width=width, label=energy[0])
    plt.bar(df3['year'] + shift[i], df3[sector[i]],
            color=color[1], width=width, label=energy[1], bottom=df2[sector[i]])
    plt.bar(df4['year'] + shift[i], df4[sector[i]],
            color=color[2],   width=width, label=energy[2], bottom=df2[sector[i]] + df3[sector[i]])
    plt.bar(df5['year'] + shift[i], df5[sector[i]],
            color=color[3],   width=width, label=energy[3], bottom=df2[sector[i]] + df3[sector[i]] + df4[sector[i]])
# plt.bar(x['Entity'],x['Hydropower Energy Generation (terawatt-hours)'],left=t6,color='#30b4c9')
# plt.bar(x['Entity'],x['Nuclear Energy Generation (terawatt-hours)'],left=t7,color='#f25c5c')
# plt.bar(x['Entity'],x['Other renewables Energy Generation (terawatt-hours)'],left=t8,color='#ad85d2')
plt.legend((energy), prop={'size': 12})


# plt.title('Top 10 Renewable Energy Producing Countries\nEnergy Source Breakdown',fontsize=20)
# plt.xlabel('Electricity Generation (TWh)', size=15)
# plt.xticks(size=13)
# plt.yticks(size=13)
plt.show()
