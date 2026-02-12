########################################################
# coin_acceptor_cli.py
# Developer: Christofer Rostedt
# Date:
########################################################
class CoinAcceptor:
    __amount: int
    __value: float

    def __init__(self):
        '''
        initialize values
        '''
        self.__amount = 0
        self.__value = 0.0

    def insertCoin(self, Pvalue) -> None:
        self.__value += Pvalue
        self.__amount = round(self.__value) # This need to round up
        return None
    
    def getAmount(self) -> int:
        return self.__amount
    
    def returnCoins(self, Pvalue) -> tuple[int, float]:
        valList = [self.__amount, self.__value]
    
        if Pvalue == 0:
            print("Returning coins...")
            print(f"{self.__amount} coins with {self.__value}€ value retured.")
            
            self.__amount = 0
            self.__value = 0.0
            valList = [self.__amount, self.__value]
            return valList
        else:
            return valList
