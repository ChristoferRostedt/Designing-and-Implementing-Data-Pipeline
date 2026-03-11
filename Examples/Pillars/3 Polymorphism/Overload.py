class Calculator:
    @staticmethod
    def sum(a: float, b: float, c: float | None = None) -> float:
        print(f"{a} + {b}", end='')
        total = a + b
        if c != None:
            print(f" + {c}", end='')
            total += c
        print(f" = {total}")
        return total
    
Calculator.sum(1, 2) # 1 + 2 = 3
Calculator.sum(1, 2, 3) # 1 + 2 + 3 = 6