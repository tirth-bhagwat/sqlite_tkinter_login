import sqlite3
import re


def create_tables_002():
    conn_002 = sqlite3.connect("database.db")

    # conn_002.execute("DROP TABLE IF EXISTS users")

    conn_002.execute(
        """CREATE TABLE IF NOT EXISTS users
       (
        id INTEGER PRIMARY KEY     AUTOINCREMENT,
        name           TEXT    NOT NULL,
        username          TEXT    NOT NULL UNIQUE,
        password       TEXT    NOT NULL,
        address       TEXT,
        email       TEXT
       );
       """
    )

    conn_002.close()


def insert_user_002(name, username_002, password_002, address_002, email_002):
    conn_002 = sqlite3.connect("database.db")
    conn_002.execute(
        f"""INSERT INTO users (name, username, password, address, email) VALUES ('{name}', '{username_002}', '{password_002}', '{address_002}', '{email_002}')"""
    )
    conn_002.commit()
    conn_002.close()


def get_user_002(username):
    conn_002 = sqlite3.connect("database.db")
    cursor = conn_002.cursor()
    cursor.execute(f"""SELECT * FROM users WHERE username = '{username}' """)
    result = cursor.fetchone()
    conn_002.close()

    return result
