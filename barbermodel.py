import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out.csv")
barber_counts = dict(df["Barber"].value_counts())
fig, ax = plt.subplots()
keys = list(barber_counts.keys())
values = list(barber_counts.values())

ax.bar(keys, values, label="client count")

for a, b in zip(keys, values):
    plt.text(a, b, str(b))
ax.set_title("Total Clients per Barber")
# ax.set_ylim(400)
ax.legend()
plt.show()
