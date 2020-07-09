# https://stackoverflow.com/questions/47894387/how-to-correlate-an-ordinal-categorical-column-in-pandas
import sys
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("out.csv")

colss = [
    "Hair Style Name",
    "Normal Price (N$)",
    "Barber",
    "Physical Height (m)",
    "Body Mass (kg)",
    "Weather",
    "Environment Noise Level",
    "Head Shape",
    "Customer Reaction",
    "Discount Percent",
    "Age Group",
    "Pre Hair Length",
    "Client Skin Tone",
    "Styling Time (minutes)",
]

if len(sys.argv) > 2:
    colss = sys.argv[1:]
    print(colss)


df = data[colss]
for c in colss:
    if c == "Barber":
        df[c] = pd.Categorical(df[c])
        df = df.assign(Barber_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Hair Style Name":
        df[c] = pd.Categorical(df[c])
        df = df.assign(HairStyle=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Weather":
        df[c] = pd.Categorical(df[c])
        df = df.assign(Weather_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Environment Noise Level":
        df[c] = pd.Categorical(df[c])
        df = df.assign(EnvironmentNoiseLevel_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Head Shape":
        df[c] = pd.Categorical(df[c])
        df = df.assign(HeadShape_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Customer Reaction":
        df[c] = pd.Categorical(df[c])
        df = df.assign(CustomerReaction_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Age Group":
        df[c] = pd.Categorical(df[c])
        df = df.assign(AgeGroup_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Pre Hair Length":
        df[c] = pd.Categorical(df[c])
        df = df.assign(BeforeHairLength_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)
    elif c == "Client Skin Tone":
        df[c] = pd.Categorical(df[c])
        df = df.assign(ClientSkinTone_=df[c].astype("category").cat.codes)
        df.drop(c, axis=1, inplace=True)


plt.imshow(df.corr(), cmap="coolwarm", interpolation="nearest")
plt.colorbar()
plt.xticks(range(len(df.columns)), df.columns, rotation=90)
plt.yticks(range(len(df.columns)), df.columns)
plt.title("Heatmap of Identified Patterns")
labels = df.corr().values
for y in range(labels.shape[0]):
    for x in range(labels.shape[1]):
        plt.text(
            x, y, "{:.2f}".format(labels[y, x]), ha="center", va="center", color="white"
        )
plt.margins(0)
plt.show()
