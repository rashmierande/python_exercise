import pandas,sqlite3

data = pandas.read_csv("ten-more-countries.txt")
#print(type(data))

conn = sqlite3.connect("database.db")
cur = conn.cursor()

for index,row in data.iterrows():
    print(row["Country"],row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"],row["Area"]))
conn.commit()
conn.close()
