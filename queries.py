def save_data_in_db(city, date, temp, hum):
    import sqlite3
    con = sqlite3.connect("weather_data.db")
    cur = con.cursor()
    # data = (data['dt'], data['main']['temp'], data['main']['humidity'])
    cr_command = f"CREATE TABLE IF NOT EXISTS {city} (date,temperature,humidity)"
    cur.execute(cr_command)
    ins_command = "INSERT INTO {} VALUES {};".format(city, (date, temp, hum))
    cur.execute(ins_command)
    con.commit()
    con.close()
    print("Saved data in database")


def check_db(city):
    import sqlite3
    con = sqlite3.connect("weather_data.db")
    cur = con.cursor()
    command = f"SELECT * FROM {city}"
    cur.execute(command)
    for i in cur.fetchall():
        print(i)
