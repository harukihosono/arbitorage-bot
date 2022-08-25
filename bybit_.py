from pybit import usdt_perpetual
session_unauth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com"
)

session_auth = usdt_perpetual.HTTP(
endpoint='https://api.bybit.com',
api_key="",
api_secret="")

def price(symbol):
    res = session_unauth.latest_information_for_symbol(
        symbol=symbol,
    )

    price = res["result"][0]["last_price"]
    return price

def entry(symbol:str,side:str,qty:str):
    qty = float(qty)
    print(session_auth.place_active_order(
        symbol=symbol,
        side=side,
        order_type="Market",
        qty=qty,
        time_in_force="GoodTillCancel",
        reduce_only=False,
        close_on_trigger=False
    ))

def close(symbol:str,side:str,qty:str):
    qty = float(qty)
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

