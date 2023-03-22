import logging
import sqlite3
from tabulate import tabulate

db_name = 'odds.db'

logging.basicConfig(filename='scraper.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y/%m/%d %H:%M:%S')


def create_table_odds():
    conn = sqlite3.connect(db_name)
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
    conn.close()


def insert(entry):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""INSERT INTO odds VALUES (?, ?, ?, ?, ?, ?)""", entry)
    conn.commit()
    conn.close()


def select_entry(entry):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM odds WHERE race = ? AND rider = ? ORDER BY datetime DESC LIMIT 1", (entry[2], entry[3]))
    prev = c.fetchone()
    if prev is None:
        insert(entry)  # if matching entry is not found, entry was not added to as a betoffer until now
        logging.info("Inserted new entry for the first time: " + str(entry))
    else:
        return prev
    conn.close()


def select_entries(entry):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM odds WHERE race = ? AND rider = ? ORDER BY datetime DESC LIMIT 2", (entry[2], entry[3]))
    entries = c.fetchall()
    if len(entries) > 1:
        for e in entries:
            print(e)
            logging.info("Entry: " + str(e))
        return entries
    conn.close()


# evt prøv at tabulate den her metode, eller indsæt den i spreadsheet?
def select_all():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT id, race, datetime, size, rider
                 FROM odds
                 ORDER BY datetime""")
    results = c.fetchall()

    for result in results:
        print(result)

    conn.close()


def table_of(race_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT id, datetime, size, rider, race 
                 FROM odds WHERE race = ?
                 ORDER BY race, rider, datetime""", (race_name,))
    rows = c.fetchall()

    columns = [description[0] for description in c.description]

    print(tabulate(rows, headers=columns))

    conn.close()


# def print_rider(rider_name):
#    c.execute("""SELECT rider, datetime, size
#                 FROM odds WHERE rider = ?
#                 AND race = 'Stage 7 (Tirreno-Adriatico 2023)'
#                 ORDER BY datetime""", rider_name)
#    results = c.fetchall()
#    for result in results:
#        print(result)
#
#
# def get_riders_names():
#    c.execute("""SELECT DISTINCT rider
#                 FROM odds WHERE race = 'Stage 7 (Tirreno-Adriatico 2023)'""")
#    results = c.fetchall()
#    return results
#
#
# riders = get_riders_names()
#
# print(riders)
# for rider in riders:
#    print_rider(rider)