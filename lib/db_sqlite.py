import sqlite3
from sqlite3 import Error
from datetime import datetime


def create_connection(db_file:str="database.db") -> sqlite3.Connection:
    conn = None
    base_path = "./data/"
    path = base_path + db_file

    try:
        conn = sqlite3.connect(path)
    except Error as e:
        print(e)

    return conn


def create_table(create_table_sql:str):
    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(create_table_sql)
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()


def create_tables():
    sql_create_table_providers = """ CREATE TABLE IF NOT EXISTS providers (
                                        id integer PRIMARY KEY,
                                        code text NOT NULL UNIQUE,
                                        name text NOT NULL
                                    ); """

    sql_create_table_currency = """ CREATE TABLE IF NOT EXISTS currencies (
                                        id integer PRIMARY KEY,
                                        code text NOT NULL UNIQUE,
                                        name text NOT NULL,
                                        symbol text NOT NULL
                                    ); """

    sql_create_table_stock = """ CREATE TABLE IF NOT EXISTS stocks (
                                        id integer PRIMARY KEY,
                                        code text NOT NULL UNIQUE,
                                        name text NOT NULL
                                    ); """

    sql_create_table_batch = """ CREATE TABLE IF NOT EXISTS batches (
                                        id integer PRIMARY KEY,
                                        providerId integer NOT NULL,
                                        stockId integer NOT NULL,
                                        datetime text NOT NULL,
                                        price real NOT NULL,
                                        priceCurrencyId integer NOT NULL,
                                        amount real NOT NULL,
                                        note text
                                    ); """

    sql_create_table_sales = """ CREATE TABLE IF NOT EXISTS sales (
                                        id integer PRIMARY KEY,
                                        datetime text NOT NULL,
                                        batchId integer NOT NULL,
                                        price real NOT NULL,
                                        amount real NOT NULL,
                                        note text
                                    ); """

    create_table(sql_create_table_providers)
    create_table(sql_create_table_currency)
    create_table(sql_create_table_stock)
    create_table(sql_create_table_batch)
    create_table(sql_create_table_sales)


def data_insert(table:str, **values) -> int:
    columnNames = ', '.join(values.keys())
    columnValues = ', '.join(['?'] * len(values))
    sql = f"INSERT INTO {table} ({columnNames}) VALUES ({columnValues})"
    ret = None

    conn = create_connection()
    if bool(conn):
        try:
            cur = conn.cursor()
            cur.execute(sql, tuple(values.values()))
            conn.commit()
            ret = cur.lastrowid
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

    return ret


def data_select(table:str, fields:tuple=("*",), whereClause:str=None) -> list:
    ret = None

    selectFields = ','.join(fields)
    sql = f"SELECT {selectFields} FROM {table}"

    if bool(whereClause):
        sql += f" WHERE {whereClause}"

    conn = create_connection()
    if bool(conn):
        try:
            cur = conn.cursor()
            cur.execute(sql)
            ret = cur.fetchall()
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

    return ret


def provider_insert(code:str, name:str) -> int:
    ret = data_insert("providers", code=code, name=name)
    return ret


def provider_validate(code:str, name:str) -> list:
    error_messages = {}
    code_errors = []
    name_errors = []

    if bool(code) is False:
        code_errors.append("Value is empty")
    element = provider_select_by_code(code)
    if bool(element):
        code_errors.append("Value already exists, it must be unique")
    if bool(name) is False:
        name_errors.append("Value is empty")

    if bool(code_errors):
        error_messages.update({"code": code_errors})
    if bool(name_errors):
        error_messages.update({"name": name_errors})

    return error_messages


def provider_select_all() -> list:
    ret = data_select("providers")
    return ret


def provider_select_by_id(id:int) -> list:
    whereClause = f"id={id}"
    ret = data_select("providers", whereClause=whereClause)
    return ret


def provider_select_by_code(code:str) -> list:
    whereClause = f"code='{code}'"
    ret = data_select("providers", whereClause=whereClause)
    return ret


def currency_insert(code:str, name:str, symbol:str) -> int:
    ret = data_insert("currencies", code=code, name=name, symbol=symbol)
    return ret


def currency_validate(code:str, name:str, symbol:str) -> list:
    error_messages = {}
    code_errors = []
    name_errors = []
    symbol_errors = []

    if bool(code) is False:
        code_errors.append("Value is empty")
    element = currency_select_by_code(code)
    if bool(element):
        code_errors.append("Value already exists, it must be unique")
    if bool(name) is False:
        name_errors.append("Value is empty")
    if bool(symbol) is False:
        symbol_errors.append("Value is empty")

    if bool(code_errors):
        error_messages.update({"code": code_errors})
    if bool(name_errors):
        error_messages.update({"name": name_errors})
    if bool(symbol_errors):
        error_messages.update({"symbol": symbol_errors})

    return error_messages


def currency_select_all() -> list:
    ret = data_select("currencies")
    return ret


def currency_select_by_id(id:int) -> list:
    whereClause = f"id={id}"
    ret = data_select("currencies", whereClause=whereClause)
    return ret


def currency_select_by_code(code:str) -> list:
    whereClause = f"code='{code}'"
    ret = data_select("currencies", whereClause=whereClause)
    return ret


def stock_insert(code:str, name:str) -> int:
    ret = data_insert("stocks", code=code, name=name)
    return ret


def stock_validate(code:str, name:str) -> list:
    error_messages = {}
    code_errors = []
    name_errors = []

    if bool(code) is False:
        code_errors.append("Value is empty")
    element = stock_select_by_code(code)
    if bool(element):
        code_errors.append("Value already exists, it must be unique")
    if bool(name) is False:
        name_errors.append("Value is empty")

    if bool(code_errors):
        error_messages.update({"code": code_errors})
    if bool(name_errors):
        error_messages.update({"name": name_errors})

    return error_messages


def stock_select_all() -> list:
    ret = data_select("stocks")
    return ret


def stock_select_by_id(id:int) -> list:
    whereClause = f"id={id}"
    ret = data_select("stocks", whereClause=whereClause)
    return ret


def stock_select_by_code(code:str) -> list:
    whereClause = f"code='{code}'"
    ret = data_select("stocks", whereClause=whereClause)
    return ret


def batch_insert(providerId:int, stockId:int, datetime:str, price:float, priceCurrencyId:int, amount:float, note:str) -> int:
    ret = data_insert("batches", providerId=providerId, stockId=stockId, datetime=datetime, price=price, priceCurrencyId=priceCurrencyId, amount=amount, note=note)
    return ret


def batch_validate(providerId:int, stockId:int, dateAndTime:str, price:float, priceCurrencyId:int, amount:float, note:str) -> list:
    error_messages = {}
    provider_errors = []
    stock_errors = []
    datetime_errors = []
    price_errors = []
    priceCurrency_errors = []
    amount_errors = []

    provider = provider_select_by_id(providerId)
    if len(provider) == 0:
        provider_errors.append("Value is not exists")

    stock = stock_select_by_id(stockId)
    if len(stock) == 0:
        stock_errors.append("Value is not exists")

    if bool(dateAndTime) is False:
        datetime_errors.append("Value is empty")
    try:
        dateAndTime = datetime.fromisoformat(dateAndTime).strftime("%Y-%m-%d %H:%M:%S")
    except:
        datetime_errors.append(f'Date and time error (format: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")})')

    price = float(str(price).replace(',', '.'))
    if bool(price) is False:
        price_errors.append("Value is empty")
    if str(price).replace('.','',1).isdigit() is False:
        price_errors.append("Value is not a number")

    currency = currency_select_by_id(priceCurrencyId)
    if len(currency) == 0:
        priceCurrency_errors.append("Value is not exists")

    amount = float(str(amount).replace(',', '.'))
    if bool(amount) is False:
        amount_errors.append("Value is empty")
    if str(amount).replace('.','',1).isdigit() is False:
        amount_errors.append("Value is not a number")

    if bool(provider_errors):
        error_messages.update({"provider": provider_errors})
    if bool(stock_errors):
        error_messages.update({"stock": stock_errors})
    if bool(datetime_errors):
        error_messages.update({"datetime": datetime_errors})
    if bool(price_errors):
        error_messages.update({"price": price_errors})
    if bool(priceCurrency_errors):
        error_messages.update({"priceCurrency": priceCurrency_errors})
    if bool(amount_errors):
        error_messages.update({"amount": amount_errors})

    return error_messages


def batch_select_all() -> list:
    ret = data_select("batches")
    return ret


def batch_select_id_all() -> list:
    ret = data_select("batches", fields=("id",))
    return ret


def batch_select_by_id(id:int) -> list:
    whereClause = f"id={id}"
    ret = data_select("batches", whereClause=whereClause)
    return ret


def batch_select_by_stockId(stockId:int) -> list:
    whereClause = f"stockId={stockId}"
    ret = data_select("batches", whereClause=whereClause)
    return ret


def sale_insert(datetime:str, batchId:int, price:float, amount:float, note:str) -> int:
    ret = data_insert("sales", datetime=datetime, batchId=batchId, price=price, amount=amount, note=note)
    return ret


def sale_select_all() -> list:
    ret = data_select("sales")
    return ret


def sale_select_id_by_batchId(batchId:int) -> list:
    whereClause = f"batchId={batchId}"
    ret = data_select("sales", fields=("id",), whereClause=whereClause)
    return ret


def sale_select_by_id(id:int) -> list:
    whereClause = f"id={id}"
    ret = data_select("sales", whereClause=whereClause)
    return ret