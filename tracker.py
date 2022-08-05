import argparse
from datetime import datetime
from lib import provider, stock, currency


def buy(args):
    providerId = args.provider
    providerObj = None
    stockId = args.stock
    stockObj = None
    dt = args.datetime
    price = args.price
    priceCurrencyId = args.currency
    currencyObj = None
    amount = args.amount
    note = args.note

    providerObj = provider.Provider(providerId)
    while providerObj.getId() is None:
        print(f"Provider id is not exists: {providerId}")
        providerId = input("Type provider id: ")
        providerObj = provider.Provider(providerId)
    print(f"Provider: {providerObj.getAsString()}")

    stockObj = stock.Stock(stockId)
    while stockObj.getId() is None:
        print(f"Stock id is not exists: {stockId}")
        stockId = input("Type stock id: ")
        stockObj = stock.Stock(stockId)
    print(f"Stock: {stockObj.getAsString()}")

    dtt = None
    try:
        dtt = datetime.fromisoformat(dt)
    except:
        dtt = None
    else:
        dt = dtt
    while dtt is None:
        dt = input("Type date and time of transaction: ")
        try:
            dtt = datetime.fromisoformat(dt)
        except:
            dtt = None
        else:
            dt = dtt
    print(f"Date and time of transaction: {dt}")

    while price is None or price.replace('.','',1).isdigit() is False:
        print(f"Price error: {price}")
        price = input("Type the price of transaction: ")
    print(f"Price of transaction: {price}")

    currencyObj = currency.Currency(priceCurrencyId)
    while currencyObj.getId() is None:
        print(f"Currency id is not exists: {priceCurrencyId}")
        priceCurrencyId = input("Type currency id: ")
        currencyObj = currency.Currency(priceCurrencyId)
    print(f"Currency: {currencyObj.getAsString()}")

    while amount is None or amount.replace('.','',1).isdigit() is False:
        print(f"Amount error: {amount}")
        amount = input("Type amount of transaction: ")
    print(f"Amount of transaction: {amount}")


def main():
    parser = argparse.ArgumentParser(description='TradeTracker command line interface')
    subparser = parser.add_subparsers(dest='subcommand', title='subcommands')

    buy_parser = subparser.add_parser('buy', description='Buy a batch', help='Buy a batch')
    sell_parser = subparser.add_parser('sell', description='Sell a batch', help='Sell a batch')
    list_parser = subparser.add_parser('list', description='Batch list', help='Batch list')

    buy_parser.add_argument('-p', '--provider', help='Provider id of the transaction')
    buy_parser.add_argument('-s', '--stock', help='Stock id')
    buy_parser.add_argument('-d', '--datetime', help='Date and time of the transaction')
    buy_parser.add_argument('-r', '--price', help='Price of the transaction')
    buy_parser.add_argument('-c', '--currency', help='Currency id of the price')
    buy_parser.add_argument('-a', '--amount', help='Amount of the transaction')
    buy_parser.add_argument('-n', '--note', help='Note of the transaction')

    sell_parser.add_argument('-b', '--batch', help='Batch id of the transaction')
    sell_parser.add_argument('-d', '--datetime', help='Date and time of the transaction')
    sell_parser.add_argument('-r', '--price', help='Price of the transaction')
    sell_parser.add_argument('-a', '--amount', help='Amount of the transaction')
    sell_parser.add_argument('-n', '--note', help='Note of the transaction')

    args = parser.parse_args()

    if args.subcommand == "buy":
        print("Buy a new batch")
        buy(args)
    elif args.subcommand == "sell":
        print("Sell from existing batch")
    elif args.subcommand == "list":
        print("List existing batches")
    elif args.subcommand is None:
        print("No subcommand")
    else:
        print("Subcommand error")
        exit(0)


if __name__ == '__main__':
    main()