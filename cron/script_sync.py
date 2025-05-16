import mysql.connector

def copiar_datos(src_host, dst_host):
    src = mysql.connector.connect(host=src_host, user="root", password="root", database="produccion")
    dst = mysql.connector.connect(host=dst_host, user="root", password="root", database="produccion")
    src_cursor = src.cursor()
    dst_cursor = dst.cursor()

    src_cursor.execute("SELECT fabrica, produccion FROM produccion")
    datos = src_cursor.fetchall()

    dst_cursor.execute("DELETE FROM produccion")
    for fila in datos:
        dst_cursor.execute("INSERT INTO produccion (fabrica, produccion) VALUES (%s, %s)", fila)
    
    dst.commit()
    src.close()
    dst.close()

copiar_datos("mysql_prod", "mysql_sit")
