import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("out.csv")
hsn_counts = dict(df["Client Skin Tone"].value_counts())
fig, ax = plt.subplots()
keys = list(hsn_counts.keys())
values = list(hsn_counts.values())

ax.bar(keys, values, label="count")

for a, b in zip(keys, values):
    plt.text(a, b, str(b))
ax.set_title("Client Skin Tone")
ax.legend()
plt.show()
