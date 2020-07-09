CREATE TABLE Barber(
	id INTEGER primary key,
	barber_name VARCHAR(120)
);

CREATE TABLE Hairstyle(
	id INTEGER primary key,
	hairstyle_name VARCHAR(120),
	price REAL
);

CREATE TABLE Client(
	id INTEGER primary key,
	age_group VARCHAR(120)
	hair_length_before_haircut VARCHAR(120)
	height REAL,
	body_mass REAL,
	skin_tone VARCHAR(50),
	head_shape VARCHAR(50),
	reaction VARCHAR(50)
);

CREATE TABLE Environment(
	id INTEGER primary key,
	weather_condition VARCHAR(120),
	noise_level VARCHAR(120)
);

CREATE TABLE Haircut_Session(
	id INTEGER primary key,
	barber_id INTEGER,
	hairstyle_id INTEGER,
	customer_id INTEGER,
	environment_id INTEGER,
	styling_time REAL,
	date_ DATE,
	discount_percent REAL
);

CREATE TABLE Client_Haircut_Session(
	id INTEGER primary key,
	client_id INTEGER,
	haircut_session_id INTEGER,
	CONSTRAINT client_haircut_pk PRIMARY KEY (client_id, haircut_session_id),
	CONSTRAINT FK_client_id 
      FOREIGN KEY (client_id) REFERENCES Client (id),
    CONSTRAINT FK_haricut_id 
      FOREIGN KEY (haircut_session_id) REFERENCES Haircut_Session (id),
);
