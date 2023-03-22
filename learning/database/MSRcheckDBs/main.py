import pandas as pd
import db


unibet = 'C:\\Users\\pvikp\\Dropbox\\2-semester\\Programmering\\Odds\\SQLite\\odds.db'
oddset = 'C:\\Users\\pvikp\\Dropbox\\2-semester\\Programmering\\Odds\\oddsetMSRlive\\odds.db'

u = 'Milano - Sanremo 2023'
o = 'Milano-Sanremo: Vinder'

#db.table_of(unibet, u)

#db.table_of(oddset, o)

#db.select_all_as_table(unibet, u)

#df = db.fetch_data(unibet)
#df = db.fetch_all_data(unibet)

df = db.fetch_top_ten(unibet)
print(df)

db.create_excel_file(df, 'msr-top10.xlsx')