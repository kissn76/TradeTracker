import db_sqlite as db
import batch


def main():
    db.create_tables()

    db.provider_insert("OTP", "OTP Bank NyRT")

    db.currency_insert("HUF", "Hungarian forint", "Ft")
    db.currency_insert("USD", "United States dollar", "$")
    db.currency_insert("EUR", "Euro", "€")

    db.stock_insert("USD", "United States dollar")
    db.stock_insert("EUR", "Euro")

    # db.batch_insert(providerId, stockId, datetime, price, priceCurrencyId, amount, note)
    db.batch_insert(1, 1, "2022-05-04", 939562, 1, 2600, None)
    db.batch_insert(1, 1, "2022-05-31", 200000, 1, 537.45, None)
    db.batch_insert(1, 1, "2022-06-02", 4700000, 1, 12569.2, None)
    db.batch_insert(1, 1, "2022-07-18", 150000, 1, 375.98, None)
    db.batch_insert(1, 1, "2022-07-21", 296514, 1, 760, None)

    # db.sale_insert(datetime, batchId, price, amount, note)
    db.sale_insert("2022-07-28", 1, 397, 1, None)
    db.sale_insert("2022-07-28", 1, 0, 1.58, "Költség és jutalék")
    db.sale_insert("2022-07-28", 1, 1034994, 2597.42, None)

    db.sale_insert("2022-07-28", 2, 214158, 537.45, None)

    db.sale_insert("2022-07-28", 3, 5008449, 12569.20, None)

    db.sale_insert("2022-07-28", 4, 141827, 355.93, None)
    db.sale_insert("2022-07-28", 4, 0, 16.82, "Költség és jutalék")

    db.sale_insert("2022-07-28", 5, 302837, 760, None)

    # db.sale_insert("2022-07-28", 2, 207455, 520.63, None)
    # db.sale_insert("2022-07-28", 1, 1034994, 2597.42, None)

    # all_provider = db.provider_select_all()
    # if all_provider is not None:
    #     print(all_provider)

    # all_currencies = db.currency_select_all()
    # if all_currencies is not None:
    #     print(all_currencies)

    # all_stocks = db.stock_select_all()
    # if all_stocks is not None:
    #     print(all_stocks)

    # all_batches = db.batch_select_all()
    # if all_batches is not None:
    #     print(all_batches)

    # all_sales = db.sale_select_all()
    # if all_sales is not None:
    #     print(all_sales)

    b = batch.getBaches()

    for ba in b:
        ba.print()

    # db.data_select("probaTable", {"id": 23, "nem": "no"})


if __name__ == '__main__':
    main()