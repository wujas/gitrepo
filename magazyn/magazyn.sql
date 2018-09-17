DROP TABLE IF EXISTS tbCustomers;
CREATE TABLE tbCustomers (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customers_name TEXT,
	adress TEXT
);

DROP TABLE IF EXISTS tbSubscriptions;
CREATE TABLE tbSubscriptions (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description TEXT,
	price_per_month DECIMAL,
	subscription_length TEXT
);

DROP TABLE IF EXISTS tbOrders;
CREATE TABLE tbOrders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER NOT NULL REFERENCES tbCustomers(id),
	subscription_id INTEGER NOT NULL REFERENCES tbSubscriptions(id), 
	purchase_date DATE
);
