class Calc:
    @staticmethod
    def sum(*args) -> float:
        total = 0
        for i, arg in enumerate(args):
            if i == 0:
                print(f"{arg}", end='')
            else:
                print(f" + {arg}", end='')
            total += arg
        print(f" = {total}")
        return total
    
Calc.sum(1, 2, 3, 4, 5) # 1 + 2 + 3 + 4 + 5 = 15
Calc.sum(3, 6, 9, 12) # 3 + 6 + 9 + 12 = 30