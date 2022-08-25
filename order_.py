import bybit_
import binance_

import db

bybit_db = db.Database("Bybit")

def is_no_position(symbol):
    position = bybit_db.position_info(symbol)
    if position == None:
        return True
    qty=float(position["qty"])
    if qty==0:
        return True

    return False

def entry_order(symbol,qty,buy_exchange,sell_exchange):
    if buy_exchange == "bybit" and sell_exchange == "binance":
        if is_no_position(symbol):
            print("bybitで買い、binanceで売る")
            bybit_.entry(symbol,"Buy",qty)
            binance_.entry(symbol,"Sell",qty)
            bybit_db.update_position_info(symbol,"Buy",qty)
    if buy_exchange == "binance" and sell_exchange == "bybit":
        if is_no_position(symbol):
            print("binanceで買い、bybitで売る")
            bybit_.entry(symbol,"Sell",qty)
            binance_.entry(symbol,"Buy",qty)
            bybit_db.update_position_info(symbol,"Sell",qty)

def close_order(symbol):
    if is_no_position(symbol):
        return

    position = bybit_db.position_info(symbol)
    qty=position["qty"]
    if position["side"] == "Buy":
        bybit_.close(symbol,"Sell",qty)
        binance_.close(symbol,"Buy",qty)
        bybit_db.update_position_info(symbol,"Sell","0")
    elif position["side"] == "Sell":
        bybit_.close(symbol,"Sell",qty)
        binance_.close(symbol,"Buy",qty)
        bybit_db.update_position_info(symbol,"Buy","0")

