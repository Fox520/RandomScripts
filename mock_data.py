import csv
import os
import random

a = [
    "Hair Style Name",
    "Normal Price (N$)",
    "Barber",
    "Weather",
    "Environment Noise Level",
    "Head Shape",
    "Customer Reaction",
    "Discount Percent",
    "Age Group",
    "Pre Hair Length",
    "Physical Height (m)",
    "Body Mass (kg)",  # in age group +/- 5
    "Date (DDMMYYYY)",
    "Client Skin Tone",
    "Styling Time (minutes)",  # in style +/- 10
]

styles = {
    # price, styling time
    "Panga": [80, 50, ["Long", "Medium"]],
    "Bald": [50, 30, ["Short", "Medium", "Long"]],
    "Baby cut": [60, 40, ["Short", "Medium", "Long"]],
    "Trim": [20, 25, ["Long", "Medium", "Short"]],
    "Fade": [80, 44, ["Medium", "Short"]],
    "Mohawk": [80, 52, ["Long", "Medium"]],
    "Afro": [70, 43, ["Long"]],
}
barbers = ["Tom", "Ben", "Leo"]
weather_list = ["Sunny", "Hot", "Cold", "Humid", "Windy", "Stormy", "Dry"]
env_noise = ["Loud", "Moderate", "Low"]
head_shape = ["Triangular", "Round", "Heart", "Oval", "Pear", "Square"]
customer_reaction = ["Happy", "Worried", "Hurried", "Serious", "Relaxed", "Tired"]
discount_percent = [0, 10, 15, 20]
age_groups = {
    "30-39": 67,
    "50-59": 78,
    "20-29": 55,
    "40-49": 73,
    "5-19": 34,
    "60-69": 80,
}
heights = [1.5, 1.6, 1.86, 1.72, 1.57, 1.65, 1.66, 1.7, 1.55, 1.83, 1.88, 1.9]
skin_tone = ["Dark", "Light"]
dates = [
    "1/04/2020",
    "2/04/2020",
    "3/04/2020",
    "4/04/2020",
    "5/04/2020",
    "6/04/2020",
    "7/04/2020",
    "8/04/2020",
    "9/04/2020",
    "10/04/2020",
    "11/04/2020",
    "12/04/2020",
    "13/04/2020",
    "14/04/2020",
    "15/04/2020",
    "16/04/2020",
    "17/04/2020",
    "18/04/2020",
    "19/04/2020",
    "20/04/2020",
    "21/04/2020",
    "22/04/2020",
    "23/04/2020",
    "24/04/2020",
    "25/04/2020",
    "26/04/2020",
    "27/04/2020",
    "28/04/2020",
    "29/04/2020",
    "30/04/2020",
    "1/05/2020",
    "2/05/2020",
    "3/05/2020",
    "4/05/2020",
    "5/05/2020",
    "6/05/2020",
    "7/05/2020",
    "8/05/2020",
    "9/05/2020",
    "10/05/2020",
    "11/05/2020",
    "12/05/2020",
    "13/05/2020",
    "14/05/2020",
    "15/05/2020",
    "16/05/2020",
    "17/05/2020",
    "18/05/2020",
    "19/05/2020",
    "20/05/2020",
    "21/05/2020",
    "22/05/2020",
    "23/05/2020",
    "24/05/2020",
    "25/05/2020",
    "26/05/2020",
    "27/05/2020",
    "28/05/2020",
    "29/05/2020",
    "30/05/2020",
    "31/05/2020",
    "1/06/2020",
    "2/06/2020",
    "3/06/2020",
    "4/06/2020",
    "5/06/2020",
    "6/06/2020",
    "7/06/2020",
    "8/06/2020",
    "9/06/2020",
    "10/06/2020",
    "11/06/2020",
    "12/06/2020",
    "13/06/2020",
    "14/06/2020",
    "15/06/2020",
    "16/06/2020",
    "17/06/2020",
    "18/06/2020",
    "19/06/2020",
    "20/06/2020",
    "21/06/2020",
    "22/06/2020",
    "23/06/2020",
    "24/06/2020",
    "25/06/2020",
    "26/06/2020",
    "27/06/2020",
    "28/06/2020",
    "29/06/2020",
    "30/06/2020",
]


def plus_minus(num, amount):
    random.seed(os.urandom(random.randint(5, 50)))
    return num + random.randint(-amount, amount)


# for i in range(1, 31):
#     print(f"\'{i}/06/2020\',")
count = 0
ay = 0
with open("out.csv", "w", newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(a)
    for date in dates:
        random.seed(os.urandom(random.randint(5, 50)))
        for i in range(random.randint(10, 20)):
            random.seed(os.urandom(random.randint(5, 50)))
            style_key = random.choice(list(styles.keys()))
            styling_time = plus_minus(styles[style_key][1], 10)
            price = styles[style_key][0]
            random.seed(os.urandom(random.randint(5, 50)))
            pre_length = random.choice(styles[style_key][2])
            random.seed(os.urandom(random.randint(5, 50)))
            barber = random.choice(barbers)
            random.seed(os.urandom(random.randint(5, 50)))
            weather = random.choice(weather_list)
            random.seed(os.urandom(random.randint(5, 50)))
            noise = random.choice(env_noise)
            random.seed(os.urandom(random.randint(5, 50)))
            shape = random.choice(head_shape)
            random.seed(os.urandom(random.randint(5, 50)))
            reaction = random.choice(customer_reaction)
            random.seed(os.urandom(random.randint(5, 50)))
            disc = random.choice(discount_percent)
            random.seed(os.urandom(random.randint(5, 50)))
            tone = random.choice(skin_tone)
            random.seed(os.urandom(random.randint(5, 50)))
            age_key = random.choice(list(age_groups.keys()))
            random.seed(os.urandom(random.randint(5, 50)))
            mass = plus_minus(age_groups[age_key], 5)
            random.seed(os.urandom(random.randint(5, 50)))
            height = random.uniform(1.5, 1.9)
            data = [
                style_key,
                price,
                barber,
                weather,
                noise,
                shape,
                reaction,
                disc,
                age_key,
                pre_length,
                height,
                mass,
                date,
                tone,
                styling_time,
            ]
            csv_writer.writerow(data)
            count += 1
            ay += i
print(count)
print(ay / count)

