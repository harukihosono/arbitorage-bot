from pybit import usdt_perpetual

key = ""
secret = ""
testnet = "https://api-testnet.bybit.com"
mainnet = "https://api.bybit.com"

session_unauth = usdt_perpetual.HTTP(
    endpoint=testnet
)

session_auth = usdt_perpetual.HTTP(
endpoint=testnet,
api_key=key,
api_secret=secret)

def price(symbol):
    try:
        res = session_unauth.latest_information_for_symbol(
            symbol=symbol,
        )
    except Exception as e:
        print(e)
        return 0

    price = res["result"][0]["last_price"]
    return price

def entry(symbol:str,side:str,qty:str):
    qty = float(qty)
    try:
        print(session_auth.place_active_order(
            symbol=symbol,
            side=side,
            order_type="Market",
            qty=qty,
            time_in_force="GoodTillCancel",
            reduce_only=False,
            close_on_trigger=False
        ))
    except Exception as e:
        print(e)
        return 0

def close(symbol:str,side:str,qty:str):
    qty = float(qty)
    try:
        res = session_auth.place_active_order(
            symbol=symbol,
            side=side,
            order_type="Market",
            qty=qty,
            time_in_force="GoodTillCancel",
            reduce_only=True,
            close_on_trigger=False
        )
        print(res)
    except Exception as e:
        print(e)
        return 0