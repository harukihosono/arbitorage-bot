from binance.um_futures import UMFutures

key = ""
secret = ""
testnet = "https://testnet.binancefuture.com/"
um_futures_client = UMFutures(key=key, secret=secret,base_url=testnet)

def price(symbol):
    try:
        res = um_futures_client.ticker_price(symbol)
        return res["price"]
    except Exception as e:
        print(e)
        return 0

def entry(symbol:str,side:str,qty:str):
    qty = float(qty)
    if(side=="Buy"):
        side = "BUY"
    else:
        side = "SELL"
    try:
        res = um_futures_client.new_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty
            )
        print(res)
    except Exception as e:
        print(e)
        return 0

def close(symbol:str,side:str,qty:str):
    qty = float(qty)
    if(side=="Buy"):
        side = "BUY"
    else:
        side = "SELL"
    try:
        res = um_futures_client.new_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty,
                reduceOnly="true"
            )
        print(res)
    except Exception as e:
        print(e)
        return 0