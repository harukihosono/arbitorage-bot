import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import bybit_
import binance_
import order_


# symbol名を入力
SYMBOL = "BTCUSDT"
# 注文サイズを入力
QTY = 0.001
# エントリーしきい値を入力
ENTRY_SIKIITI = 0.01
# イグジットしきい値を入力
CLOSE_SIKIITI = 0.01
symbol = SYMBOL
qty = QTY
entry_sikiiti = ENTRY_SIKIITI
close_sikiiti = CLOSE_SIKIITI

num = []
x = []
bybit_price_y = []
binance_price_y = []

def animate(i):

    bybit_price = bybit_.price(symbol)
    binance_price =binance_.price(symbol)

    # X軸
    x.append(len(num))
    num.append(1)
    # Y軸
    bybit_price_y.append(float(bybit_price))
    binance_price_y.append(float(binance_price))

    # 最大・最小を計算して、割合を計算する
    price       = [bybit_price_y[-1],binance_price_y[-1]]
    price_min   = min(bybit_price_y[-1],binance_price_y[-1])
    price_max  = max(bybit_price_y[-1],binance_price_y[-1])
    kakakusa  = round(price_max / price_min - 1,5) * 100

    # BUY
    if price_min == price[0]:
        buy_name = "bybit"
        buy_num=0
    elif price_min == price[1]:
        buy_name = "binance"
        buy_num=1

    # SELL
    if price_max == price[0]:
        sell_name = "bybit"
        sell_num=0
    elif price_max == price[1]:
        sell_name = "binance"
        sell_num=1

    if entry_sikiiti <= kakakusa:
        message = str(datetime.datetime.now().strftime('%H:%M:%S')) +"\n"+symbol +"\n"+ f'{kakakusa:.3f}' + "%" +"\n"+ "BUY:" + buy_name  + str(price[buy_num]) +"\n"+ "SELL:" + sell_name + str(price[sell_num])+"\n"
        print(message)
        order_.entry_order(symbol,qty,buy_name,sell_name)

    if kakakusa <= close_sikiiti:
        order_.close_order(symbol)

    plt.cla()
    main_text = "Price_Gap: " + f'{kakakusa:.3f}' +"%"
    plt.title(main_text,color="green")
    plt.xlabel("Time")
    plt.ylabel(symbol)
    plt.plot(x,bybit_price_y ,label="bybit")
    plt.plot(x,binance_price_y ,label="binance")
    plt.legend(loc="upper left")
    plt.tight_layout()

    if len(x) >= 100:
        num.clear()
        x.clear()
        bybit_price_y.clear()
        binance_price_y.clear()

ani = FuncAnimation(plt.gcf(),animate,interval=1000)

plt.tight_layout()
plt.show()