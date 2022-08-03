import db_sqlite as db


def account_movements_print(accountId):
    account = bankaccount.BankAccount()
    account.load_by_id(accountId)
    account_provider = account.getProvider()
    account_currency = account.getCurrency()

    print(f"{'Account name':16}: {account.getName()}")
    print(f"{'Provider name':16}: {account_provider.getName()}")
    print(f"{'Account currency':16}: {account_currency.getName()} ({account_currency.getCode()}, {account_currency.getSimbol()})\n")
    print(f"{'Date':<19}|{'Type':<12}|{'Amount':>16}|{'Balance':>16}|{'Connected movement':>35}|")
    print( "===================|============|================|================|===================================|")

    account_movements = movements_by_accountId(accountId)
    balance = 0
    for movement in account_movements:
        balance += movement.getAmount()

        movement_transaction = db.transaction_select_by_id(movement.getId())
        movement_transaction_typeId = movement_transaction[0][1]
        movement_transaction_note = movement_transaction[0][2]

        movement_transaction_type = db.transaction_type_select_by_id(movement_transaction_typeId)
        movement_transaction_type_code = movement_transaction_type[0][1]
        movement_transaction_type_name = movement_transaction_type[0][2]
        movement_transaction_type_note = movement_transaction_type[0][3]

        movement_connected_movements = movements_by_transactionId(movement.getId())
        connected_movements_str = ""
        for m in movement_connected_movements:
            m_account = bankaccount.BankAccount()
            m_account.load_by_id(m.getId())
            m_account_currency = m_account.getCurrency()

            if m.getId() != movement.getId():
                connected_movements_str += f"{m_account.getName()} {m.getAmount():16,.2f}{m_account_currency.getSimbol()}".replace(",", " ")

        print(f"{movement.getDatetime():19}|{movement_transaction_type_name:12}|{movement.getAmount():16,.2f}|{balance:16,.2f}|".replace(",", " "), f"{connected_movements_str:>34}|")

    print( "=================================================|================|====================================")
    print(f"                                                 |{balance:16,.2f}|".replace(",", " "))


def main():
    # db.create_tables()
    # db.provider_insert(["OTP", "OTP Bank NyRT"])
    # db.stock_insert(["HUF", "Hungarian forint"])
    # db.stock_insert(["USD", "United States dollar"])
    # db.stock_insert(["EUR", "Euro"])
    # db.batch_insert([1, 2, "2022-08-02 12:01:01", 1100000, 2825.95, None])
    # db.batch_insert([1, 3, "2022-08-02 12:01:01", 1100000, 2747.04, None])
    # db.sale_insert(["2022-08-03 07:12:34", 1, 79090, 200, None])

    all_provider = db.provider_select_all()
    if all_provider is not None:
        print(all_provider)

    all_stocks = db.stock_select_all()
    if all_stocks is not None:
        print(all_stocks)

    all_batches = db.batch_select_all()
    if all_batches is not None:
        print(all_batches)

    all_sales = db.sale_select_all()
    if all_sales is not None:
        print(all_sales)

    # account_movements_print(1)
    # account_movements_print(2)
    # account_movements_print(3)


if __name__ == '__main__':
    main()