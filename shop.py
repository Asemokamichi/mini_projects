class GoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def toString(self):
        return "Name:" + self.name + "\nPrice:" + self.price


class BuyHistory:
    import datetime

    def __init__(self, goodName, goodPrice, buyTime=datetime.datetime.now()):
        self.goodName = goodName
        self.goodPrice = goodPrice
        self.buyTime = buyTime

    def get_GoodName(self):
        return self.goodName

    def get_GoodPrice(self):
        return self.goodPrice

    def get_BuyTime(self):
        return self.buyTime

    def toString(self):
        return "GoodName:" + self.goodName + "\nPGoodPrice:" + \
               self.goodPrice + "\nBuyTime:" + self.buyTime
    

