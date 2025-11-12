import re
from sqlite3 import Cursor
import psycopg2
from connection import get_connection

def create_register_table():
    conexion=get_connection()
    if conexion is None:
        print("Failed to connect to database")
        return False
    cursor=conexion.cursor()
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS resgistros (
        id SERIAL PRIMARY KEY,
        name varchar(100),
        email varchar(100),
        password varchar(100))
        """)

        conexion.commit()
        print("table created successfully") 
        return True
    except psycopg2.Error as e:
         print(f"error created: {e}")
         return False
    finally:
        cursor.close()
        conexion.close()

#solo se ejecuta una vez y luego se 
#if __name__ == "__main__":
#   create_register_table() 


def register_user(name, email, password):
   
    conexion = get_connection()
    if conexion is None:
        print("Error: No se pudo conectar a la base de datos")
        return False
    
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO resgistros (name, email, password) VALUES (%s, %s, %s) returning id",
            (name, email, password)
        )
        conexion.commit()
        print(f"Usuario {name} registrado exitosamente")
        return True
    except psycopg2.Error as e:
        print(f"Error al registrar usuario: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()


def search_users_id(user_id):
    conexion=get_connection()
    if conexion is None:
        print("Error: No se pudo conectar a la base de datos")
        return None
    
    cursor=conexion.cursor()
    try:
        cursor.execute("""
        SELECT id, name, email, password 
        FROM resgistros
        WHERE id = %s""", (user_id,))

        user = cursor.fetchone()
        return user
    except psycopg2.Error as e:
        print(f"error al buscar usuario: {e}")
        return None
    finally:
        cursor.close()
        conexion.close()


def get_all_registers():
    conexion = get_connection()
    if conexion is None:
        print("Error: No se pudo conectar a la base de datos")
        return []
    
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id, name, email, password FROM resgistros")
        registros = cursor.fetchall()
        return registros
    except psycopg2.Error as e:
        print(f"Error al consultar registros: {e}")
        return []
    finally:
        cursor.close()
        conexion.close()

####
def delete_name(user_id):
    conexion = get_connection()
    if conexion is None:
        print("error: no connected to the database")
        return False

    cursor=conexion.cursor()
    try:
        cursor.execute("DELETE FROM resgistros WHERE id = %s", (user_id,))
        conexion.commit()
        return True
    except psycopg2.Error as e:
        print(f"error eliminar usuario: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()


def update_user(user_id, name, email, password):
    conexion = get_connection()
    if conexion is None:
        print("Error: No se pudo conectar a la base de datos")
        return False
    
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "UPDATE resgistros SET name = %s, email = %s, password = %s WHERE id = %s",
            (name, email, password, user_id)
        )
        conexion.commit()
        print(f"Usuario con ID {user_id} actualizado exitosamente")
        return True
    except psycopg2.Error as e:
        print(f"Error al actualizar usuario: {e}")
        conexion.rollback()
        return False
    finally:
        cursor.close()
        conexion.close()






