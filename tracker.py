import argparse
from datetime import datetime
from lib import provider, stock, currency
from lib import db_sqlite as db


def buy(args):
    providerId = None
    providerObj = None
    stockId = None
    stockObj = None
    dt = None
    price = None
    priceCurrencyId = None
    currencyObj = None
    amount = None
    note = None

    try:
        providerId = args.provider
    except AttributeError:
        providerId = None

    try:
        stockId = args.stock
    except AttributeError:
        stockId = None

    try:
        dt = args.datetime
    except AttributeError:
        dt = None
    
    try:
        price = args.price
    except AttributeError:
        price = None
    
    try:
        priceCurrencyId = args.currency
    except AttributeError:
        priceCurrencyId = None
    
    try:
        amount = args.amount
    except AttributeError:
        amount = None
    
    try:
        note = args.note
    except AttributeError:
        note = None
    
    providerObj = provider.Provider(providerId)
    while providerObj.getId() is None:
        print(f"Provider id is not exists: {providerId}")
        all_provider = db.provider_select_all()
        if all_provider is not None:
            print(all_provider)
        providerId = input("Type provider id: ")
        providerObj = provider.Provider(providerId)
    print(f"Provider: {providerObj.getAsString()}")

    stockObj = stock.Stock(stockId)
    while stockObj.getId() is None:
        print(f"Stock id is not exists: {stockId}")
        all_stocks = db.stock_select_all()
        if all_stocks is not None:
            print(all_stocks)
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
        dt = input(f'Type date and time of transaction (format: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}):')
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
        all_currencies = db.currency_select_all()
        if all_currencies is not None:
            print(all_currencies)
        priceCurrencyId = input("Type currency id: ")
        currencyObj = currency.Currency(priceCurrencyId)
    print(f"Currency: {currencyObj.getAsString()}")

    while amount is None or amount.replace('.','',1).isdigit() is False:
        print(f"Amount error: {amount}")
        amount = input("Type amount of transaction: ")
    print(f"Amount of transaction: {amount}")

    if note is None:
        note = ""

    print(f"Provider: {providerObj.getName()}")
    print(f"Stock: {stockObj.getName()}")
    batch_unit_price = float(price) / float(amount)
    print(f"{'Date':<19}|{'Price':>16}|{'Amount':>16}|{'Unit price':>16}|{'Note':^35}")
    print(f"{'':-^100}")
    print(f"{dt}|{(price + ' ' + currencyObj.getSymbol()):>16}|{amount:>16}|{batch_unit_price:16,.2f}|{note}")

    menu_options = {
            1: 'Provider',
            2: 'Stock',
            3: 'Date',
            4: 'Price',
            5: 'Currency',
            6: 'Amount',
            7: 'Note'
        }
    
    while(True):
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            providerIdNew = None
            providerObjNew = provider.Provider(providerIdNew)
            while providerObjNew.getId() is None:
                all_provider = db.provider_select_all()
                if all_provider is not None:
                    print(all_provider)
                providerIdNew = input("Type provider id: ")
                providerObjNew = provider.Provider(providerIdNew)
                if providerIdNew == "":
                    providerIdNew = providerId
                    providerObjNew = providerObj
            providerId = providerIdNew
            providerObj = providerObjNew
        elif option == 2:
            print('Handle option \'Option 2\'')
        elif option == 3:
            print('Handle option \'Option 3\'')
        elif option == 4:
            print('Thanks message before exiting')
            exit(0)
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
        
        if note is None:
            note = ""

        print(f"Provider: {providerObj.getName()}")
        print(f"Stock: {stockObj.getName()}")
        batch_unit_price = float(price) / float(amount)
        print(f"{'Date':<19}|{'Price':>16}|{'Amount':>16}|{'Unit price':>16}|{'Note':^35}")
        print(f"{'':-^100}")
        print(f"{dt}|{(price + ' ' + currencyObj.getSymbol()):>16}|{amount:>16}|{batch_unit_price:16,.2f}|{note}")



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
        menu_options = {
            1: 'Buy',
            2: 'Sell',
            3: 'List',
            4: 'Exit'
        }
        while(True):
            for key in menu_options.keys():
                print (key, '--', menu_options[key] )
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            #Check what choice was entered and act accordingly
            if option == 1:
                print('Buy a new batch')
                buy(None)
            elif option == 2:
                print('Handle option \'Option 2\'')
            elif option == 3:
                print('Handle option \'Option 3\'')
            elif option == 4:
                print('Thanks message before exiting')
                exit(0)
            else:
                print('Invalid option. Please enter a number between 1 and 4.')
    else:
        print("Subcommand error")
        exit(0)


if __name__ == '__main__':
    main()