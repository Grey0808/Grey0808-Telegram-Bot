import app.player as player

import app.variables as var
conn, cur = var.conn, var.cur


cur.execute(f"""CREATE TABLE IF NOT EXISTS users(
   id INT PRIMARY KEY,
   money INT,
   gamemode INT,
   admin TINYINT(1));
""")
conn.commit()


def insert(*args):
    cur.execute("INSERT INTO users VALUES(%s, %s, %s, %s);", args)
    conn.commit()


def update(_id, _arg, _val):
    cur.execute(f"UPDATE users SET {_arg} = {_val} WHERE id = {_id};")
    conn.commit()


def readbase():
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    users = {i[0]: player.Player(*i) for i in users}
    return users
