import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out.csv")
gb = df.groupby("Hair Style Name").mean()
fig, ax = plt.subplots()
keys = dict(gb["Styling Time (minutes)"]).keys()
values = dict(gb["Styling Time (minutes)"]).values()

ax.scatter(keys, values, label="minutes")

for a, b in zip(keys, values):
    plt.text(a, b, str(int(b)))
ax.set_title("Average styling time per hairstyle")
ax.legend()
plt.show()
