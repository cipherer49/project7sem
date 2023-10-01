import sqlite3


def create_db():
    con = sqlite3.connect(database=r'login.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS login_table (uid INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(20) UNIQUE, password VARCHAR(20))")
    cur.execute("CREATE TABLE IF NOT EXISTS start_login_table (uid INTEGER PRIMARY KEY AUTOINCREMENT, sh_pwd VARCHAR(20))")
    con.commit()
def add_users(users_list):
    con = sqlite3.connect(database=r'login.db')
    cur = con.cursor()

    # SQL query to insert a new user into the 'login_table'
    query = "INSERT INTO login_table (username, password) VALUES (?, ?)"

    try:
        for user in users_list:
            # Execute the query with the 'username' and 'password' values from the tuple
            cur.execute(query, user)
        con.commit()
        print("Users added successfully!")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different username.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        con.close()

def add_sh_pwd_data(sh_pwd_list):
    con = sqlite3.connect(database=r'login.db')
    cur = con.cursor()

    # SQL query to insert a new data into the 'secure_login_table'
    query = "INSERT INTO start_login_table (sh_pwd) VALUES (?)"

    try:
        for sh_pwd in sh_pwd_list:
            # Execute the query with the 'sh_pwd' value
            cur.execute(query, (sh_pwd,))
        con.commit()
        print("Share password added successfully!")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        con.close()


# Example usage:
if __name__ == "__main__":
    users_to_add = [
        ("aryan", "aryan123"),
        ("arsalaan", "password"),
        ("kaif", "password"),
        ("asif","password")
        # Add more users as needed in the same format (username, password)
    ]
    share_pwd_to_add = [
        "group18rait",
        "admin",
        "password"


    ]
    create_db()  # Ensure the table is created before adding users
    add_users(users_to_add)
    add_sh_pwd_data(share_pwd_to_add)

