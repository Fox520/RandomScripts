import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out.csv")
weather_counts = dict(df["Weather"].value_counts())
fig, ax = plt.subplots()
keys = list(weather_counts.keys())
values = list(weather_counts.values())

ax.bar(keys, values, label="count of occurance during client visit")

for a, b in zip(keys, values):
    plt.text(a, b, str(b))
ax.set_title("Weather conditions")
ax.set_ylim(150)
ax.legend()
plt.show()
