import sqlite3

#VALID SETS
ACCOUNTS = {'Chase', 'Compass'}
CATEGORIES = {'Fast Food', 'Groceries', 'Mortgage', 'Income', 'Pay', 'Home', 'Clothes', 'Electric', 'Gas', 'Home Gas', 'Alcohol', 'Internet', 'Entertainment'}

#SQL QUERIES
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, date TEXT, vendor TEXT, amount INTEGER, account TEXT, category TEXT);"

INSERT_TRANSACTION = "INSERT INTO transactions (date, vendor, amount, account, category) VALUES (?, ?, ?, ?, ?);"

GET_ALL_TRANSACTIONS = "SELECT * FROM transactions;"

GET_TRANSACTIONS_BY_VENDOR = "SELECT * FROM transactions WHERE vendor = ?;"

GET_TOTAL_BY_ACCOUNT = "SELECT account, SUM(amount) FROM transactions WHERE account = ? GROUP BY account;"
GET_TOTALS_BY_ACCOUNT = "SELECT account, SUM(amount) FROM transactions GROUP BY account;"
GET_TOTAL_BY_CATEGORY = "SELECT category, SUM(amount) FROM transactions WHERE category = ? GROUP BY category;"
GET_TOTALS_BY_CATEGORY = "SELECT category, SUM(amount) FROM transactions GROUP BY category;"

def connect():
    return sqlite3.connect('data.db')


def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE)


def add_transaction(connection, date, vendor, amount, account, category):
    with connection:
        connection.execute(INSERT_TRANSACTION, (date, vendor, amount, account, category))


def get_all_transactions(connection):
    with connection:
        return connection.execute(GET_ALL_TRANSACTIONS).fetchall()


def get_transactions_by_vendor(connection, vendor):
    with connection:
        return connection.execute(GET_TRANSACTIONS_BY_VENDOR, (vendor,)).fetchall()


def get_total_by_account(connection, account):
    with connection:
        return connection.execute(GET_TOTAL_BY_ACCOUNT, (account,)).fetchall()


def get_totals_by_account(connection):
    with connection:
        return connection.execute(GET_TOTALS_BY_ACCOUNT).fetchall()


def get_total_by_category(connection, category):
    with connection:
        return connection.execute(GET_TOTAL_BY_CATEGORY, (category,)).fetchall()


def get_totals_by_category(connection):
    with connection:
        return connection.execute(GET_TOTALS_BY_CATEGORY).fetchall()


def is_account_valid(account):
    return (account in ACCOUNTS)


def is_category_valid(category):
    return (category in CATEGORIES)




