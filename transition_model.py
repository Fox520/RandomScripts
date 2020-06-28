import csv
import matplotlib.pyplot as plt

# name: {style: count}
barber_style = {
    "Tom": {
        "Panga": 0,
        "Bald": 0,
        "Baby cut": 0,
        "Trim": 0,
        "Fade": 0,
        "Mohawk": 0,
        "Afro": 0,
    },
    "Ben": {
        "Panga": 0,
        "Bald": 0,
        "Baby cut": 0,
        "Trim": 0,
        "Fade": 0,
        "Mohawk": 0,
        "Afro": 0,
    },
    "Leo": {
        "Panga": 0,
        "Bald": 0,
        "Baby cut": 0,
        "Trim": 0,
        "Fade": 0,
        "Mohawk": 0,
        "Afro": 0,
    },
}

with open("out.csv", "r") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    data = list(csv_reader)
    for barber in barber_style.keys():
        for row in data:
            if row[2] == barber:
                style = row[0]
                barber_style[barber][style] = barber_style[barber][style] + 1

# total_y = []
panga = []
bald = []
baby_cut = []
trim = []
fade = []
hawk = []
afro = []

names = list(barber_style.keys())

for name in names:
    # total_y.append(sum(barber_style[name].values()))
    panga.append(barber_style[name]["Panga"])
    bald.append(barber_style[name]["Bald"])
    baby_cut.append(barber_style[name]["Baby cut"])
    trim.append(barber_style[name]["Trim"])
    fade.append(barber_style[name]["Fade"])
    hawk.append(barber_style[name]["Mohawk"])
    afro.append(barber_style[name]["Afro"])

fig, ax = plt.subplots()

# Overall
ax.plot(names, panga, label="Panga")
ax.plot(names, bald, label="Bald")
ax.plot(names, baby_cut, label="Baby cut")
ax.plot(names, trim, label="Trim")
ax.plot(names, fade, label="Fade")
ax.plot(names, hawk, label="Mohawk")
ax.plot(names, afro, label="Afro")

ax.set_ylim([40, 80])
ax.set_title("Hairstyle done vs Barber Transition Model")
ax.legend()
# plt.tight_layout()
plt.grid()

plt.show()
