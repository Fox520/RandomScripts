import sqlite3
import csv, random, os

conn = sqlite3.connect("barbershop.db")
c = conn.cursor()

# The barbers
try:
    c.execute("INSERT INTO Barber VALUES(1,'Tom')")
    c.execute("INSERT INTO Barber VALUES(2,'Ben')")
    c.execute("INSERT INTO Barber VALUES(3,'Leo')")
except Exception as e:
    print(e)


# The barbers
try:
    c.execute("INSERT INTO Hairstyle VALUES(1,'Panga', 80)")
    c.execute("INSERT INTO Hairstyle VALUES(2,'Bald', 50)")
    c.execute("INSERT INTO Hairstyle VALUES(3,'Baby cut',30)")
    c.execute("INSERT INTO Hairstyle VALUES(4,'Trim',20)")
    c.execute("INSERT INTO Hairstyle VALUES(5,'Fade',80)")
    c.execute("INSERT INTO Hairstyle VALUES(6,'Mohawk',80)")
    c.execute("INSERT INTO Hairstyle VALUES(7,'Afro',70)")
except Exception as e:
    print(e)


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
weather_list = ["Hot", "Cold", "Moderate"]
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

counter = 0
for date in dates:
    random.seed(os.urandom(random.randint(5, 50)))
    for i in range(1, 15):  # range(random.randint(10, 20)):
        counter += 1
        # print(counter)
        random.seed(os.urandom(random.randint(5, 50)))
        style_key = random.choice(list(styles.keys()))
        price = styles[style_key][0]
        random.seed(os.urandom(random.randint(5, 50)))
        pre_length = random.choice(styles[style_key][2])
        random.seed(os.urandom(random.randint(5, 50)))
        barber = random.choice(barbers)
        random.seed(os.urandom(random.randint(5, 50)))
        age_key = random.choice(list(age_groups.keys()))
        # if counter < 150:
        #     barber = "Tom"
        if counter < 500:
            style_key = "Panga"
            pre_length = "Long"
            age_key = "20-29"
        elif counter < 650:
            style_key = "Bald"
            pre_length = "Short"
            # barber = "Ben"
        elif counter < 850:
            style_key = "Trim"
            pre_length = "Short"
            age_key = "30-39"
        styling_time = plus_minus(styles[style_key][1], 10)
        if style_key == "Panga":
            sk = "1"
        elif style_key == "Bald":
            sk = "2"
        elif style_key == "Baby cut":
            sk = "3"
        elif style_key == "Trim":
            sk = "4"
        elif style_key == "Fade":
            sk = "5"
        elif style_key == "Mohawk":
            sk = "6"
        elif style_key == "Afro":
            sk = "7"

        if barber == "Tom":
            bk = "1"
        elif barber == "Ben":
            bk = "2"
        elif barber == "Leo":
            bk = "3"

        if counter < 300:
            weather = "Cold"
        elif counter < 650:
            weather = "Hot"
        else:
            weather = "Moderate"
        # weather = random.choice(weather_list)
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
        print(data)
        sql = "INSERT INTO Client VALUES(NULL,?,?,?,?,?,?,?)"
        c.execute(sql, (age_key, pre_length, height, mass, tone, shape, reaction))
        client_id = c.lastrowid

        sql1 = "INSERT INTO Environment VALUES(NULL,?,?)"
        c.execute(sql1, (weather, noise))
        env_id = c.lastrowid

        sql2 = "INSERT INTO Haircut_Session VALUES(NULL,?,?,?,?,?,?,?)"
        c.execute(
            sql2, (bk, sk, client_id, env_id, styling_time, date, discount_percent)
        )
        conn.commit()
        count += 1
        ay += i
print(count)
print(ay / count)


conn.close()
