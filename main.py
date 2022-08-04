import db_sqlite as db
import batch, provider, currency, stock


def create_base():
    db.create_tables()
    provider.Provider(None, "OTP", "OTP Bank NyRT")
    currency.Currency(None, "HUF", "Hungarian forint", "Ft")
    currency.Currency(None, "USD", "United States dollar", "$")
    currency.Currency(None, "EUR", "Euro", "€")
    stock.Stock(None, "USD", "United States dollar")
    stock.Stock(None, "EUR", "Euro")

    all_provider = db.provider_select_all()
    if all_provider is not None:
        print(all_provider)

    all_currencies = db.currency_select_all()
    if all_currencies is not None:
        print(all_currencies)

    all_stocks = db.stock_select_all()
    if all_stocks is not None:
        print(all_stocks)


def create_batches():
    # batch.Batch(None, providerId, stockId, datetime, price, priceCurrencyId, amount, note)
    b1 = batch.Batch(None, 1, 1, "2022-05-04", 939562, 1, 2600, None)
    b2 = batch.Batch(None, 1, 1, "2022-05-31", 200000, 1, 537.45, None)
    b3 = batch.Batch(None, 1, 1, "2022-06-02", 4700000, 1, 12569.2, None)
    b4 = batch.Batch(None, 1, 1, "2022-07-18", 150000, 1, 375.98, None)
    b5 = batch.Batch(None, 1, 1, "2022-07-21", 296514, 1, 760, None)

    # batchObject.sell(datetime, price, amount, note)
    b1.sell("2022-07-28", 397, 1, None)
    b1.sell("2022-07-28", 0, 1.58, "Költség és jutalék")
    b1.sell("2022-07-28", 1034994, 2597.42, None)
    b2.sell("2022-07-28", 214158, 537.45, None)
    b3.sell("2022-07-28", 5008449, 12569.20, None)
    b4.sell("2022-07-28", 141827, 355.93, None)
    b4.sell("2022-07-28", 0, 16.82, "Költség és jutalék")
    b5.sell("2022-07-28", 302837, 760, None)

    b1.print()
    b2.print()
    b3.print()
    b4.print()
    b5.print()


def main():
    # create_base()

    # create_batches()

    b = batch.getBaches()
    for ba in b:
        ba.print()

    # b1 = batch.Batch(1)
    # b1.print()


if __name__ == '__main__':
    main()