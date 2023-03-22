import sqlite3
import pandas as pd
from tabulate import tabulate


def select_all(db_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT id, race, datetime, km_to_go, size, rider
                 FROM odds
                 ORDER BY datetime""")
    results = c.fetchall()

    for result in results:
        print(result)

    conn.close()


def table_of(db_name, race_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT id, datetime, km_to_go, size, rider, race 
                 FROM odds WHERE race = ?
                 ORDER BY race, rider, datetime""", (race_name,))
    rows = c.fetchall()

    columns = [description[0] for description in c.description]

    print(tabulate(rows, headers=columns))

    conn.close()


def select_all_as_table(db_name, race_name):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("""SELECT id, race, datetime, km_to_go, size, rider
                 FROM odds
                 WHERE race = ?
                 ORDER BY datetime""", (race_name,))
    rows = c.fetchall()

    columns = [description[0] for description in c.description]

    print(tabulate(rows, headers=columns))

    conn.close()


def fetch_data(db_name):
    conn = sqlite3.connect(db_name)
    query = """SELECT datetime, size, rider
                 FROM odds
                 WHERE race = 'Milano - Sanremo 2023' and size < 52
                 ORDER BY datetime"""
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def fetch_all_data(db_name):
    conn = sqlite3.connect(db_name)
    query = """SELECT *
               FROM odds
               ORDER BY datetime"""
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def fetch_top_ten(db_name):
    conn = sqlite3.connect(db_name)
    top_ten = ('van der Poel, Mathieu', 'Ganna, Filippo', 'Van Aert, Wout', 'Pogacar, Tadej', 'Kragh Andersen, Soren',
               'Pedersen, Mads', 'Powless, Neilson', 'Mohoric, Matej', 'Turgis, Anthony', 'Stuyven, Jasper')

    order_by_case = "CASE rider "
    for index, rider in enumerate(top_ten):
        order_by_case += f"WHEN '{rider}' THEN {index} "
    order_by_case += "END"

    query = f"""SELECT datetime, km_to_go, size, rider
                FROM odds
                WHERE rider IN {top_ten} AND race = 'Milano - Sanremo 2023'
                ORDER BY {order_by_case}, datetime"""

    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def create_excel_file(df, file_name):
    # Create Excel file
    writer = pd.ExcelWriter(file_name, engine="openpyxl")
    df.to_excel(writer, index=False, sheet_name="Sheet1")
    writer.save()
