import re
import db
from fuzzywuzzy import fuzz
from tabulate import tabulate

import fun

u = 'C:\\Users\\pvikp\\Dropbox\\2-semester\\Programmering\\Odds\\SQLite\\odds.db'
o = 'C:\\Users\\pvikp\\Dropbox\\2-semester\\Programmering\\Odds\\oddsetMSRlive\\odds.db'

unibet_names = [fun.normalize_name_u(name) for name in db.select_all_names(u)]
oddset_names = [fun.normalize_name_o(name) for name in db.select_all_names(o)]

# normalized_names = [fun.normalize_name_o(name) for name in names]
# similarity_scores = [fuzz.ratio(name, normalized_name) for name, normalized_name in zip(names, normalized_names)]
# table_data = list(zip(names, similarity_scores, normalized_names))
# table_data.sort(key=lambda x: x[1], reverse=True)
# headers = ["Name", "Fuzz", "Normalized Name"]
# print(tabulate(table_data, headers=headers))

fun.compare_name_lists(unibet_names, oddset_names)
