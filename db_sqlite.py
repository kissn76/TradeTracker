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
    create_table(sql_create_table_stock)
    create_table(sql_create_table_batch)
    create_table(sql_create_table_sales)


def provider_insert(values):
    sql = "INSERT INTO providers(code, name) VALUES(?, ?)"
    ret = None

    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            ret = cur.lastrowid
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

    return ret


def provider_select_all():
    sql = "SELECT * FROM providers"
    ret = None

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


def provider_select_by_id(id):
    sql = "SELECT * FROM providers WHERE id='" + str(id) + "'"
    ret = None

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


def stock_insert(values):
    sql = "INSERT INTO stocks(code, name) VALUES(?, ?)"
    ret = None

    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            ret = cur.lastrowid
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

    return ret


def stock_select_all():
    sql = "SELECT * FROM stocks"
    ret = None

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


def stock_select_by_id(id):
    sql = "SELECT * FROM stocks WHERE id='" + str(id) + "'"
    ret = None

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


def batch_insert(values):
    sql = "INSERT INTO batches(providerId, stockId, datetime, price, amount, note) VALUES(?, ?, ?, ?, ?, ?)"
    ret = None

    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            ret = cur.lastrowid
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

    return ret


def batch_select_all():
    sql = "SELECT * FROM batches"
    ret = None

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


def batch_select_by_id(id):
    sql = "SELECT * FROM batches WHERE id='" + str(id) + "'"
    ret = None

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


def sale_insert(values):
    sql = "INSERT INTO sales(datetime, batchId, price, amount, note) VALUES(?, ?, ?, ?, ?)"
    ret = None

    conn = create_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(sql, values)
            conn.commit()
            ret = cur.lastrowid
        except Error as e:
            print(e)
    else:
        print("Error! Cannot create the database connection.")
    conn.close()

    return ret


def sale_select_all():
    sql = "SELECT * FROM sales"
    ret = None

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


def sale_select_by_batchId(batchId):
    sql = "SELECT * FROM sales WHERE batchId='" + str(batchId) + "'"
    ret = None

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


def sale_select_by_id(id):
    sql = "SELECT * FROM sales WHERE id='" + str(id) + "'"
    ret = None

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