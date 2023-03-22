import pyodbc as pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-8KEOEI7\\SQLEXPRESS'
DB_NAME = 'Betting2022'

#connection_string = f"""
#    DRIVER={{{DRIVER_NAME}}};
#    SERVER={SERVER_NAME};
#    DATABASE={DATABASE_NAME};
#    Trust_Connection=yes;
#"""
#connection_string = f'DRIVER={DRIVER_NAME};Server=' + SERVER_NAME + ';Database=' + DATABASE_NAME

conn = pyodbc.connect('Driver=' + DRIVER_NAME + ';'
                      'Server=' + SERVER_NAME + ';'
                      'Database=' + DB_NAME + ';'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# insert - create
#cursor.execute("INSERT INTO [team] VALUES ('Hold 2');")
#conn.commit()

# select - read
cursor.execute('SELECT [country], [name] FROM [race]')
for i in cursor:
    print(i)



# delete
#cursor.execute("DELETE FROM [team] WHERE [title] = 'Hold 2'")
#print(cursor.rowcount, 'deleted items')
#conn.commit()






