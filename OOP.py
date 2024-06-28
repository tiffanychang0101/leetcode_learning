class bank():
    def __init__(self, uname) -> None:
        #變數前加__，變為私有屬性，之後在外面程式就無法修改
        self.__name = uname #設定存款人姓名
        self.__balance = 0 #開戶預設金額
        self.__title = 'chiikawa_bank' #設定銀行名稱(屬性)
        self.__rate = 30 #美金換台幣匯率
        self.__service_charge = 0.01 #換匯手續費

    def savemoney(self, money): #方法
        self.__balance += money

    def withdrawmoney(self, money):
        self.__balance -= money

    def nowmoney(self):
        print(self.__title, "存款人: ", self.__name, "餘額: ", self.__balance)

    def usd_to_twd(self, usd): #較容易忘記
        self.result = self.__calculate_rate(usd) 
        return(self.result)

    def __calculate_rate(self, usd): #私有方法也是前面加__ (銀行換匯可能會根據顧客有不同匯率與手續費)
        return int(usd * self.__rate * (1 + self.__service_charge))

tiffany = bank('hachi')
tiffany.savemoney(150)
tiffany.__balance = 10 #這行是錯的，是要呈現私有屬性無法藉由外部程式直接修改(不安全)
tiffany.withdrawmoney(13)
tiffany.withdrawmoney(23)
tiffany.nowmoney()
usd = 100
print(usd, '可兌換', tiffany.usd_to_twd(usd), '台幣')