from binance.um_futures import UMFutures

key = ""
secret = ""

um_futures_client = UMFutures(key=key, secret=secret)

def price(symbol):
    res = um_futures_client.ticker_price(symbol)
    return res["price"]

def entry(symbol:str,side:str,qty:str):
    qty = float(qty)
    if(side=="Buy"):
        side = "BUY"
    else:
        side = "SELL"
    res = um_futures_client.new_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty,
            timeInForce="GTC",
        )
    print(res)

def close(symbol:str,side:str,qty:str):
    qty = float(qty)
    if(side=="Buy"):
        side = "BUY"
    else:
        side = "SELL"
    res = um_futures_client.new_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=qty,
            timeInForce="GTC",
            reduceOnly="true"
        )
    print(res)