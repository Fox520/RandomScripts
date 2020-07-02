import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out.csv")
hsn_counts = dict(df["Pre Hair Length"].value_counts())
fig, ax = plt.subplots()
keys = list(hsn_counts.keys())
values = list(hsn_counts.values())

ax.scatter(keys, values, label="count")

for a, b in zip(keys, values):
    plt.text(a, b, str(b))
ax.set_title("Client Hair Length Before Styling")
ax.legend()
plt.show()
