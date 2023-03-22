import logging
import sqlite3

logging.basicConfig(filename='scrapers/scraper.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')

db_path = 'database/odds.db'


def find_prev_entry(entry):
    return entry


def insert_entries(entries):
    """
    Insert a list of entries (as tuples) into a SQLite database using executemany.

    Args:
        entries (list): A list of tuples, where each tuple represents a row to be inserted
                        into the database.
        db_path (str): The file path of the SQLite database.

    Returns:
        None
    """
    with sqlite3.connect(db_path) as conn:
        c = conn.cursor()
        c.executemany('''INSERT INTO my_table (col1, col2, col3)
                          VALUES (?, ?, ?)''', entries)
        conn.commit()
