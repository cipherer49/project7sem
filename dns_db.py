import sqlite3

def createDatabase():
    try:
        conn = sqlite3.connect('dns_database.db')
        conn.close()
        print("SQLite database 'dns_database.db' created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating SQLite database: {e}")

if __name__ == "__main__":
    createDatabase()