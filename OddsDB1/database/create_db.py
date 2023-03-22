import logging
import sqlite3

logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')

db_path = 'database/odds.db'


def drop_if_exists(conn, table_name):
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS', table_name)


def create_table_org(conn):
    c = conn.cursor()


def create_table_team(conn):
    c = conn.cursor()


def create_table_race(conn):
    c = conn.cursor()


def create_table_comp_market(conn):
    c = conn.cursor()


def create_table_bookmaker(conn):
    c = conn.cursor()


def create_table_odds(conn):
    c = conn.cursor()
    c.execute("""DROP TABLE odds""")
    c.execute("""CREATE TABLE odds (
                      id INTEGER PRIMARY KEY,
                      bookmaker TEXT,
                      race TEXT,
                      rider TEXT,
                      size REAL,
                      datetime DATETIME)""")
    conn.commit()


tables = {
    "org": """CREATE TABLE IF NOT EXISTS org (
                  id INTEGER PRIMARY KEY)""",
    "team": """CREATE TABLE IF NOT EXISTS team (
                  id INTEGER PRIMARY KEY,
                  org_id INTEGER,
                  name TEXT,
                  country TEXT,                  
                  category TEXT,
                  year INTEGER,
                  FOREIGN KEY(org_id) REFERENCES org(id))""",
    "race": """CREATE TABLE IF NOT EXISTS race (
                  id INTEGER PRIMARY KEY,
                  name TEXT,
                  country TEXT)""",
    "event": """CREATE TABLE IF NOT EXISTS event (
                  id INTEGER PRIMARY KEY,
                  race_id INTEGER,
                  name TEXT,
                  classification TEXT,
                  date DATE,
                  FOREIGN KEY(race_id) REFERENCES race(id))""",
    "bookmaker": """CREATE TABLE IF NOT EXISTS bookmaker (
                  id INTEGER PRIMARY KEY,
                  name TEXT)""",
    "rider": """CREATE TABLE IF NOT EXISTS rider (
                  id INTEGER PRIMARY KEY,
                  firstname TEXT,
                  lastname TEXT,
                  country TEXT,
                  date_of_birth DATE)""",
    "odds": """CREATE TABLE IF NOT EXISTS odds (
                  id INTEGER PRIMARY KEY,
                  bookmaker_id INTEGER,
                  event_id INTEGER,
                  rider_id INTEGER,
                  size REAL,
                  timestamp DATETIME,
                  FOREIGN KEY(bookmaker_id) REFERENCES bookmaker(id),
                  FOREIGN KEY(event_id) REFERENCES event(id),
                  FOREIGN KEY(rider_id) REFERENCES rider(id))"""
}


def create_table(conn, table_name, sql_string):
    c = conn.cursor()
    c.execute(sql_string)
    logging.info(f"Created table: {table_name}")


def init_db():
    conn = sqlite3.connect(db_path)

    for table in tables:
        create_table(conn, table, tables[table])

    get_table_metadata()


def get_table_metadata():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    for table in tables:
        c.execute(f"PRAGMA table_info({table})")

        rows = c.fetchall()

        print(table)
        for row in rows:
            print(row)
