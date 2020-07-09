import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out.csv")
weather_counts = dict(df["Weather"].value_counts())
fig, ax = plt.subplots()
keys = list(weather_counts.keys())
values = list(weather_counts.values())

ax.plot(keys, values, label="No. of haircuts")

for a, b in zip(keys, values):
    plt.text(a, b, str(b))
ax.set_title("Number of haircuts vs Weather condition")
ax.set_ylim(200)
ax.legend()
plt.show()
