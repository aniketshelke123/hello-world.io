import sqlite3

con = sqlite3.connect('aniket.db')
query = "insert into stud_info values('aniket', 15)"
con.execute(query)
con.commit()
con.close()
print("Done...")