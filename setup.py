from lib import db_sqlite as db
from lib import provider, stock, currency


def create_tables():
    db.create_tables()


def create_base():
    provider.Provider(None, "OTP", "OTP Bank NyRT")
    currency.Currency(None, "HUF", "Hungarian forint", "Ft")
    currency.Currency(None, "USD", "United States dollar", "$")
    currency.Currency(None, "EUR", "Euro", "€")
    stock.Stock(None, "USD", "United States dollar")
    stock.Stock(None, "EUR", "Euro")


def main():
    create_tables()
    create_base()


if __name__ == '__main__':
    main()