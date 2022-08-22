from lib import db_sqlite as db
from lib import batch, provider, stock, sale, currency
import setup


def test_data():
    # batch.Batch(None(id), providerId, stockId, datetime, price, priceCurrencyId, amount, note)
    b1 = batch.Batch(None, 1, 1, "2022-05-04", 939562, 1, 2600, None)
    b2 = batch.Batch(None, 1, 1, "2022-05-31", 200000, 1, 537.45, None)
    b3 = batch.Batch(None, 1, 1, "2022-06-02", 4700000, 1, 12569.2, None)
    b4 = batch.Batch(None, 1, 1, "2022-07-18", 150000, 1, 375.98, None)
    b5 = batch.Batch(None, 1, 1, "2022-07-21", 296514, 1, 760, None)

    b6 = batch.Batch(None, 1, 1, "2022-08-01 17:16:56", 5000000, 1, 12704.54, None)
    b7 = batch.Batch(None, 1, 1, "2022-08-02 09:00:21", 5000000, 1, 12653.42, None)
    b8 = batch.Batch(None, 1, 1, "2022-08-02 10:55:50", 4000000, 1, 10198.62, None)

    # batchObject.sell(datetime, price, amount, note)
    b1.sell("2022-07-28", 397, 1, None)
    b1.sell("2022-07-28", 0, 1.58, "Költség és jutalék")
    b1.sell("2022-07-28", 1034994, 2597.42, None)
    b2.sell("2022-07-28", 214158, 537.45, None)
    b3.sell("2022-07-28", 5008449, 12569.20, None)
    b4.sell("2022-07-28", 141827, 355.93, None)
    b4.sell("2022-07-28", 0, 16.82, "Költség és jutalék")
    b5.sell("2022-07-28", 302837, 760, None)

    b4.sell("2022-08-22 10:40:00", 1298, 3.23, None)
    b6.sell("2022-08-22 10:40:00", 5106844, 12704.54, None)
    b7.sell("2022-08-22 10:40:00", 5086295, 12653.42, None)
    b8.sell("2022-08-22 10:40:00", 4083939, 10159.81, None)
    b8.sell("2022-08-22 10:40:00", 0, 35.52, "Költség és jutalék")

    # b1.print()
    # b2.print()
    # b3.print()
    # b4.print()
    # b5.print()


def main():
    # setup.create_tables()
    # setup.create_base()
    # test_data()

    # elements = provider.getAll()
    # for element in elements:
    #     provider.Provider(element).print()

    # elements = currency.getAll()
    # for element in elements:
    #     currency.Currency(element).print()

    # elements = stock.getAll()
    # for element in elements:
    #     stock.Stock(element).print()

    # elements = batch.getAll()
    # for element in elements:
    #     batch.Batch(element).print()

    # batch.printStock(1)
    
    elements = batch.getByStockWithBalance(1)
    for element in elements:
        batch.Batch(element).print()

    # print(db.batch_select_id_all())
    # print(db.batch_select_all())


if __name__ == '__main__':
    main()