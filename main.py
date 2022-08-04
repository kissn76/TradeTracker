import db_sqlite as db
import batch


def main():
    # db.create_tables()
    # db.provider_insert(["OTP", "OTP Bank NyRT"])
    # db.stock_insert(["HUF", "Hungarian forint"])
    # db.stock_insert(["USD", "United States dollar"])
    # db.stock_insert(["EUR", "Euro"])
    # db.batch_insert([1, 2, "2022-08-02 12:01:01", 1100000, 2825.95, None])
    # db.batch_insert([1, 3, "2022-08-02 12:01:01", 1100000, 2747.04, None])
    # db.sale_insert(["2022-08-03 07:12:34", 1, 79090, 200, None])
    # db.sale_insert(["2022-08-04 07:13:54", 1, 79997, 200, None])

    # all_provider = db.provider_select_all()
    # if all_provider is not None:
    #     print(all_provider)

    # all_stocks = db.stock_select_all()
    # if all_stocks is not None:
    #     print(all_stocks)

    # all_batches = db.batch_select_all()
    # if all_batches is not None:
    #     print(all_batches)

    # all_sales = db.sale_select_all()
    # if all_sales is not None:
    #     print(all_sales)

    batch_1 = batch.Batch()
    batch_1.load_by_id(1)
    batch_1.print()


if __name__ == '__main__':
    main()