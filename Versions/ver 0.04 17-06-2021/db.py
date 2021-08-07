import sqlite3
conn = sqlite3.connect('test.db')

conn.execute('DROP TABLE Tickers;')


conn.execute('''CREATE TABLE 'Tickers' (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT, 'slug' TEXT, 'symbol' TEXT, 'cost' INTEGER);''')


def new_table (title, slug, symbol, cost):
    conn.execute(f'''CREATE TABLE '{title}' (
    'id' INTEGER PRIMARY KEY, 'slug' TEXT, 'symbol' TEXT, 'cost' INTEGER);''')
    conn.execute(f"INSERT INTO {title} (slug, symbol, cost) VALUES ('{slug}', '{symbol}', {cost})");
    conn.execute(f"INSERT INTO {title} (slug, symbol, cost) VALUES ('{slug}', '{symbol}', {cost})");
    conn.execute(f"INSERT INTO {title} (slug, symbol, cost) VALUES ('{slug}', '{symbol}', {cost})");
    # conn.execute(f"INSERT INTO {title} (slug, symbol, cost) VALUES ('Ethereum', 'ETH', 4)");
    # conn.execute(f"INSERT INTO {title} (slug, symbol, cost) VALUES ('Ripple', 'XRP', 69)");
    return title

conn.execute("INSERT INTO Tickers (slug, symbol, cost) VALUES ('Bitcoin', 'BTC', 420)");
conn.execute("INSERT INTO Tickers (slug, symbol, cost) VALUES ('Ethereum', 'ETH', 4)");
conn.execute("INSERT INTO Tickers (slug, symbol, cost) VALUES ('Ripple', 'XRP', 69)");


tickers = conn.execute("SELECT * FROM Tickers")
print("Basic info about all the current programmed crypto-currencies")
print("")
for row in tickers:
    # print ("Id = ", row[0])
    print ("Slug = ", row[1])
    print ("Symbol = ", row[2])
    print ("Cost = ", row[3], "\n")

table = new_table('name', input("Slug: "), input("Symbol: "), int(input("Cost: ")))
table = new_table(symbol, input("Slug: "), input("Symbol: "), int(input("Cost: ")))
def table ():
    tickers = conn.execute(f"SELECT * FROM {table}")
    print("Basic info about all the cies")
    print("")
    for row in tickers:
        # print ("Id = ", row[0])
        print ("Slug = ", row[1])
        print ("Symbol = ", row[2])
        print ("Cost = ", row[3], "\n")
# people = conn.execute("SELECT * FROM people")
# print("Information on people")
# for row in people:
#     print ("Id = ", row[0])
#     print ("Full name = ", row[1])
#     print ("Email = ", row[2])
#     print ("Phone number = ", row[3], "\n")
conn.close()