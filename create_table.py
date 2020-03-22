import sqlite3


connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table_users_query = "CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY_KEY, username text, password text)"
cursor.execute(create_table_users_query)


create_table_items_query = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY_KEY, name text, price real)"
cursor.execute(create_table_items_query)


connection.commit()
connection.close()