import sqlite3
from sqlite3 import Error
from datetime import datetime


def create_connection(db_file="database.db"):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(create_table_sql):
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
                                        name text
                                    ); """

    sql_create_table_currency = """ CREATE TABLE IF NOT EXISTS currencies (
                                        id integer PRIMARY KEY,
                                        code text NOT NULL UNIQUE,
                                        name text,
                                        symbol text
                                    ); """

    sql_create_table_stock = """ CREATE TABLE IF NOT EXISTS stocks (
                                        id integer PRIMARY KEY,
                                        code text NOT NULL UNIQUE,
                                        name text
                                    ); """

    sql_create_table_batch = """ CREATE TABLE IF NOT EXISTS batches (
                                        id integer PRIMARY KEY,
                                        providerId integer,
                                        stockId integer,
                                        datetime text,
                                        price real,
                                        priceCurrencyId integer,
                                        amount real,
                                        note text
                                    ); """

    sql_create_table_sales = """ CREATE TABLE IF NOT EXISTS sales (
                                        id integer PRIMARY KEY,
                                        datetime text,
                                        batchId integer,
                                        price real,
                                        amount real,
                                        note text
                                    ); """

    create_table(sql_create_table_providers)
    create_table(sql_create_table_currency)
    create_table(sql_create_table_stock)
    create_table(sql_create_table_batch)
    create_table(sql_create_table_sales)


def data_insert(table, values):
    sql = "INSERT INTO {}({}) VALUES({})".format(table, ','.join(tuple(values.keys())), ','.join(['?'] * len(values)))
    ret = None

    conn = create_connection()
    if conn is not None:
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


def data_select(table, values=None, fields=["*"]):
    sql = None
    ret = None

    if values is None:
        sql = "SELECT {} FROM {}".format(','.join(fields), table)
    else:
        where = []
        for key, val in values.items():
            where.append(str(key) + "='" + str(val) + "'")
        sql = "SELECT {} FROM {} WHERE {}".format(','.join(fields), table, ' AND '.join(where))

    conn = create_connection()
    if conn is not None:
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


def provider_insert(code, name):
    ret = data_insert("providers", {"code": code, "name": name})
    return ret


def provider_select_all():
    ret = data_select("providers")
    return ret


def provider_select_by_id(id):
    ret = data_select("providers", {"id": id})
    return ret


def currency_insert(code, name, symbol):
    ret = data_insert("currencies", {"code": code, "name": name, "symbol": symbol})
    return ret


def currency_select_all():
    ret = data_select("currencies")
    return ret


def currency_select_by_id(id):
    ret = data_select("currencies", {"id": id})
    return ret


def stock_insert(code, name):
    ret = data_insert("stocks", {"code": code, "name": name})
    return ret


def stock_select_all():
    ret = data_select("stocks")
    return ret


def stock_select_by_id(id):
    ret = data_select("stocks", {"id": id})
    return ret


def batch_insert(providerId, stockId, datetime, price, priceCurrencyId, amount, note):
    ret = data_insert("batches", {"providerId": providerId, "stockId": stockId, "datetime": datetime, "price": price, "priceCurrencyId": priceCurrencyId, "amount": amount, "note": note})
    return ret


def batch_select_all():
    ret = data_select("batches")
    return ret


def batch_select_id_all():
    ret = data_select("batches", fields=["id"])
    return ret


def batch_select_by_id(id):
    ret = data_select("batches", {"id": id})
    return ret


def sale_insert(datetime, batchId, price, amount, note):
    ret = data_insert("sales", {"datetime": datetime, "batchId": batchId, "price": price, "amount": amount, "note": note})
    return ret


def sale_select_all():
    ret = data_select("sales")
    return ret


def sale_select_id_by_batchId(batchId):
    ret = data_select("sales", {"batchId": batchId}, ["id"])
    return ret


def sale_select_by_id(id):
    ret = data_select("sales", {"id": id})
    return ret