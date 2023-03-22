import sqlite3


def select_all_names(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT DISTINCT rider
                 FROM odds
                 ORDER BY datetime""")
    results = c.fetchall()
    conn.close()

    return [str(t[0]) for t in results]