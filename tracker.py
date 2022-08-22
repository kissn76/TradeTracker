import os
import argparse
from datetime import datetime
from lib import provider, stock, currency, batch
from lib import db_sqlite as db


def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def menu_loop():
    menu_code = "menu_main"
    while(True):
        if menu_code == "menu_main":
            menu_code = menu_main()
        elif menu_code == "menu_provider":
            menu_code = menu_provider()
        elif menu_code == "menu_provider_list":
            menu_code = menu_provider(True)
        elif menu_code == "menu_provider_new":
            menu_code = menu_provider_new()
        elif menu_code == "menu_stock":
            menu_code = menu_stock()
        elif menu_code == "menu_stock_list":
            menu_code = menu_stock(True)
        elif menu_code == "menu_stock_new":
            menu_code = menu_stock_new()
        elif menu_code == "menu_currency":
            menu_code = menu_currency()
        elif menu_code == "menu_currency_list":
            menu_code = menu_currency(True)
        elif menu_code == "menu_currency_new":
            menu_code = menu_currency_new()
        elif menu_code == "menu_batch":
            menu_code = menu_batch()
        elif menu_code == "menu_batch_list":
            menu_code = menu_batch(True)
        elif menu_code == "menu_batch_buy":
            menu_code = menu_batch_buy()
        elif menu_code == "menu_batch_sell":
            menu_code = menu_batch()
        elif menu_code == "program_exit":
            exit()


def print_menu_option(head, menu_options, footer=None):
    cls()
    if head is not None:
        print(head)
    for key in menu_options.keys():
        print (key, '--', menu_options[key])
    if footer is not None:
        print(footer)
    option = None
    while option is None:
        try:
            option = int(input("Enter your choice: "))
        except:
            print("Wrong input. Please enter a number from list above.")
            option = None
            continue

        if option in menu_options.keys():
            return option
        else:
            print("Invalid option. Please enter a number from list above.")
            option = None
            continue


def menu_main():
    head = "Main menu"
    menu_options = {
        1: "Provider",
        2: "Stock",
        3: "Currency",
        4: "Batch",
        0: "Exit program"
    }
    option = print_menu_option(head, menu_options)
    if option == 0:
        return "program_exit"
    elif option == 1:
        return "menu_provider"
    elif option == 2:
        return "menu_stock"
    elif option == 3:
        return "menu_currency"
    elif option == 4:
        return "menu_batch"


def menu_provider(list_providers=False):
    head = "Provider menu"
    menu_options = {
        1: "List",
        2: "New",
        0: "Back to main menu"
    }
    footer = None
    if list_providers is True:
        text = ""
        elements = provider.getAll()
        for element in elements:
            text += provider.Provider(element).getAsString() + "\n"
        if text != "":
            footer = text[:-1]
    option = print_menu_option(head, menu_options, footer=footer)
    if option == 0:
        return "menu_main"
    elif option == 1:
        return "menu_provider_list"
    elif option == 2:
        return "menu_provider_new"


def menu_provider_new():
    id = None
    code = None
    name = None

    code = input("Type provider code: ")
    name = input("Type provider name: ")
    obj = provider.Provider(id, code, name)
    if bool(obj.error):
        print(f"Error: {obj.error}")
    else:
        print(f"New provider: {obj.getAsString()}")
    input("Press Enter to continue...")
    return "menu_provider"


def menu_stock(list_stocks=False):
    head = "Stock menu"
    menu_options = {
        1: "List",
        2: "New",
        0: "Back to main menu"
    }
    footer = None
    if list_stocks is True:
        text = ""
        elements = stock.getAll()
        for element in elements:
            text += stock.Stock(element).getAsString() + "\n"
        if text != "":
            footer = text[:-1]
    option = print_menu_option(head, menu_options, footer=footer)
    if option == 0:
        return "menu_main"
    elif option == 1:
        return "menu_stock_list"
    elif option == 2:
        return "menu_stock_new"


def menu_stock_new():
    id = None
    code = None
    name = None

    code = input("Type stock code: ")
    name = input("Type stock name: ")
    obj = stock.Stock(id, code, name)
    if bool(obj.error):
        print(f"Error: {obj.error}")
    else:
        print(f"New stock: {obj.getAsString()}")
    input("Press Enter to continue...")
    return "menu_stock"


def menu_currency(list_currencies=False):
    head = "Currency menu"
    menu_options = {
        1: "List",
        2: "New",
        0: "Back to main menu"
    }
    footer = None
    if list_currencies is True:
        text = ""
        elements = currency.getAll()
        for element in elements:
            text += currency.Currency(element).getAsString() + "\n"
        if text != "":
            footer = text[:-1]
    option = print_menu_option(head, menu_options, footer=footer)
    if option == 0:
        return "menu_main"
    elif option == 1:
        return "menu_currency_list"
    elif option == 2:
        return "menu_currency_new"


def menu_currency_new():
    id = None
    code = None
    name = None
    symbol = None

    code = input("Type currency code: ")
    name = input("Type currency name: ")
    symbol = input("Type currency symbol: ")
    obj = currency.Currency(id, code, name, symbol)
    if bool(obj.error):
        print(f"Error: {obj.error}")
    else:
        print(f"New currency: {obj.getAsString()}")
    input("Press Enter to continue...")
    return "menu_currency"


def menu_batch(list_batches=False):
    head = "Batch menu"
    menu_options = {
        1: "List",
        2: "Buy",
        3: "Sell",
        0: "Back to main menu"
    }
    footer = None
    if list_batches is True:
        text = ""
        elements = batch.getAll()
        for element in elements:
            text += batch.Batch(element).getAsString() + "\n"
        if text != "":
            footer = text[:-1]
    option = print_menu_option(head, menu_options, footer=footer)
    if option == 0:
        return "menu_main"
    elif option == 1:
        return "menu_batch_list"
    elif option == 2:
        return "menu_batch_buy"
    elif option == 3:
        return "menu_batch_sell"


def menu_batch_buy():
    id = None
    providerId = None
    stockId = None
    dateTime = None
    price = None
    priceCurrencyId = None
    amount = None
    note = None

    provider.printAll()
    providerId = input("Type provider ID: ")
    stock.printAll()
    stockId = input("Type stock ID: ")
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dateTime = input(f"Type date & time ({dt}): ")
    if bool(dateTime) is False:
        dateTime = dt
    print(dateTime)
    price = input("Type price: ")
    currency.printAll()
    priceCurrencyId = input("Type price currency ID: ")
    amount = input("Type amount: ")
    note = input("Type note: ")
    obj = batch.Batch(id, providerId, stockId, dateTime, price, priceCurrencyId, amount, note)
    if bool(obj.error):
        print(f"Error: {obj.error}")
    else:
        print(f"New batch:\n{obj.getAsString()}")
    input("Press Enter to continue...")
    return "menu_batch"


def main():
    parser = argparse.ArgumentParser(description='TradeTracker command line interface')
    subparser = parser.add_subparsers(dest='subcommand', title='subcommands')

    provider_parser = subparser.add_parser('provider', description='Provider control', help='Provider control')
    currency_parser = subparser.add_parser('currency', description='Currency control', help='Currency control')
    stock_parser = subparser.add_parser('stock', description='Stock control', help='Stock control')
    buy_parser = subparser.add_parser('buy', description='Buy new batch', help='Buy new batch')
    sell_parser = subparser.add_parser('sell', description='Sell from batch', help='Sell from batch')
    list_parser = subparser.add_parser('list', description='List batches', help='List batches')

    provider_subparser = provider_parser.add_subparsers(dest="subcommand2nd")
    provider_add = provider_subparser.add_parser('add', help='Add new provider')
    provider_list = provider_subparser.add_parser('list', help='List providers')
    # provider_delete = provider_subparser.add_parser('delete', help='Delete a provider')
    # provider_modify = provider_subparser.add_parser('modify', help='Modify a provider')

    provider_add.add_argument('code', help='Provider code')
    provider_add.add_argument('name', help='Provider name')

    # provider_delete_group = provider_delete.add_mutually_exclusive_group(required=True)
    # provider_delete_group.add_argument("-bi", "--byid", help="Delete by id")
    # provider_delete_group.add_argument("-bc", "--bycode", help="Delete by code")

    # provider_modify_group = provider_modify.add_mutually_exclusive_group(required=True)
    # provider_modify_group.add_argument("-bi", "--byid", help="Modify by id")
    # provider_modify_group.add_argument("-bc", "--bycode", help="Modify by code")
    # provider_modify.add_argument("-c", "--code", nargs=1, metavar=('new_code'), help="New code")
    # provider_modify.add_argument("-n", "--name", nargs=1, metavar=('new_name'), help="New name")

    currency_subparser = currency_parser.add_subparsers(dest="subcommand2nd")
    currency_add = currency_subparser.add_parser('add', help='Add new currency')
    currency_list = currency_subparser.add_parser('list', help='List currencies')
    # currency_delete = currency_subparser.add_parser('delete', help='Delete a currency')
    # currency_modify = currency_subparser.add_parser('modify', help='Modify a currency')

    currency_add.add_argument('code', help='Currency code')
    currency_add.add_argument('name', help='Currency name')
    currency_add.add_argument('symbol', help='Currency symbol')

    stock_subparser = stock_parser.add_subparsers(dest="subcommand2nd")
    stock_add = stock_subparser.add_parser('add', help='Add new stock')
    stock_list = stock_subparser.add_parser('list', help='List stock')
    # stock_delete = stock_subparser.add_parser('delete', help='Delete a stock')
    # stock_modify = stock_subparser.add_parser('modify', help='Modify a stock')

    stock_add.add_argument('code', help='Stock code')
    stock_add.add_argument('name', help='Stock name')

    buy_parser.add_argument('provider', help='Provider id of the transaction')
    buy_parser.add_argument('stock', help='Stock id')
    buy_parser.add_argument('datetime', help='Date and time of the transaction')
    buy_parser.add_argument('price', help='Price of the transaction')
    buy_parser.add_argument('currency', help='Currency id of the price')
    buy_parser.add_argument('amount', help='Amount of the transaction')
    buy_parser.add_argument('-n', '--note', help='Note of the transaction')

    # sell_parser.add_argument('-b', '--batch', help='Batch id of the transaction')
    # sell_parser.add_argument('-d', '--datetime', help='Date and time of the transaction')
    # sell_parser.add_argument('-r', '--price', help='Price of the transaction')
    # sell_parser.add_argument('-a', '--amount', help='Amount of the transaction')
    # sell_parser.add_argument('-n', '--note', help='Note of the transaction')

    args = parser.parse_args()

    # print(args)
    # exit()

    if args.subcommand == "provider":
        provider_start(args)
    elif args.subcommand == "currency":
        currency_start(args)
    elif args.subcommand == "stock":
        stock_start(args)
    elif args.subcommand == "buy":
        buy(args)
    elif args.subcommand == "sell":
        print("Sell from existing batch")
    elif args.subcommand == "list":
        list_batches(args)
    elif args.subcommand is None:
        menu_loop()
    else:
        print("Subcommand error")
        exit(0)


def provider_start(args):
    if args.subcommand2nd == "list":
        provider.printAll()
    elif args.subcommand2nd == "add":
        id = None
        code = args.code
        name = args.name
        obj = provider.Provider(id, code, name)
        if bool(obj.error):
            print(f"Error: {obj.error}")
        else:
            print(f"New provider: {obj.getAsString()}")
    else:
        print("Subcommand error")
        exit(0)


def currency_start(args):
    if args.subcommand2nd == "list":
        currency.printAll()
    elif args.subcommand2nd == "add":
        id = None
        code = args.code
        name = args.name
        symbol = args.symbol
        obj = currency.Currency(id, code, name, symbol)
        if bool(obj.error):
            print(f"Error: {obj.error}")
        else:
            print(f"New currency: {obj.getAsString()}")
    else:
        print("Subcommand error")
        exit(0)


def stock_start(args):
    if args.subcommand2nd == "list":
        stock.printAll()
    elif args.subcommand2nd == "add":
        id = None
        code = args.code
        name = args.name
        obj = stock.Stock(id, code, name)
        if bool(obj.error):
            print(f"Error: {obj.error}")
        else:
            print(f"New stock: {obj.getAsString()}")
    else:
        print("Subcommand error")
        exit(0)


def buy(args):
    id = None
    providerId = args.provider
    stockId = args.stock
    dt = args.datetime
    price = args.price
    priceCurrencyId = args.currency
    amount = args.amount
    note = args.note
    obj = batch.Batch(None, providerId, stockId, dt, price, priceCurrencyId, amount, note)
    if bool(obj.error):
        print(f"Error: {obj.error}")
    else:
        print("New batch")
        obj.print()


def list_batches(args):
    elements = batch.getAll()
    for element in elements:
        batch.Batch(element).print()


if __name__ == '__main__':
    main()