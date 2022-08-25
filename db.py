import dataset

class Database():
    def __init__(self,name):
        db = dataset.connect("sqlite:///data.sqlite")
        self.table  = db[name + "_" +"positions"]
    # ポジション情報書き込み
    def update_position_info(self,symbol,side,qty):
        position = self.table.find_one(symbol=symbol)
        if position==None:
            self.table.insert({"symbol":symbol,"side": side,"qty":qty})
        else:
            self.table.update({"symbol":symbol,"side": side,"qty":qty}, ["symbol"])
    # データベースからポジション情報読み取り
    def position_info(self,symbol):
        position = self.table.find_one(symbol=symbol)
        return position
    # テーブル削除
    def delete_table(self):
        self.table.drop()

