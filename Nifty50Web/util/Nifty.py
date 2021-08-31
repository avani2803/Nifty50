class Nifty50:
    symbol: str
    series: str
    open_price: float
    high_price: float
    low_price: float
    ltp: float
    previous_price: float
    net_price: float
    traded_quantity: float
    turnover_in_lakhs: float
    last_corp_announcement_date: str
    last_corp_announcement: str

    def __init__(self, symbol: str, series: str, open_price: float, high_price: float, low_price: float, ltp: float, previous_price: float, net_price: float, traded_quantity: float, turnover_in_lakhs: float, last_corp_announcement_date: str, last_corp_announcement: str) -> None:
        self.symbol = symbol
        self.series = series
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.ltp = ltp
        self.previous_price = previous_price
        self.net_price = net_price
        self.traded_quantity = traded_quantity
        self.turnover_in_lakhs = turnover_in_lakhs
        self.last_corp_announcement_date = last_corp_announcement_date
        self.last_corp_announcement = last_corp_announcement
