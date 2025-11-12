import psycopg2
from config import df_config

def get_connection():
    if not df_config["password"]:

        raise ValueError("password is required")
    
    try:
        connection=psycopg2.connect(
            host=df_config["host"],
            port=df_config["port"],
            user=df_config["user"],
            password=df_config["password"],
            database=df_config["database"]
        )
        return connection
    except psycopg2.Error as e:
        print(f"error connecting to the database: {e}")
        return None

    