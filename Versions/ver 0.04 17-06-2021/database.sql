.header on
.mode column

CREATE TABLE Tickers (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, symbol TEXT, cost INTEGER);

CREATE TABLE Historical (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, symbol TEXT, cost INTEGER);

INSERT INTO Tickers (slug, symbol, cost) VALUES ("Bitcoin", "BTC", 420);
INSERT INTO Tickers (slug, symbol, cost) VALUES ("Ethereum", "ETH", 4);
INSERT INTO Tickers (slug, symbol, cost) VALUES ("Ripple", "XRP", 69);

SELECT * FROM Tickers;
SELECT " ";
SELECT * FROM Tickers ORDER BY -cost;
SELECT " ";
SELECT slug AS "Name", MAX(cost) AS "Highest cost" FROM Tickers;