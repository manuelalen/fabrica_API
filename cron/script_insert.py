import requests
import mysql.connector

data = requests.get("http://api:5000/produccion").json()

def insert_data(host):
    conn = mysql.connector.connect(
        host=host, user="root", password="root", database="produccion"
    )
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produccion")
    for item in data:
        cursor.execute("INSERT INTO produccion (fabrica, produccion) VALUES (%s, %s)", (item["fabrica"], item["produccion"]))
    conn.commit()
    conn.close()

insert_data("mysql_prod")
insert_data("mysql_dev")
