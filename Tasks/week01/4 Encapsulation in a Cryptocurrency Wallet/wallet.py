from datetime import datetime

class CryptoWallet:
    _next_id = 1
    
    def __init__(self):
        self.__balance: float = 0.0
        self.__walletId: int = CryptoWallet._next_id
        CryptoWallet._next_id += 1
        self.__history: list[tuple[datetime, str, float]] = []
        
    # Public read‑only interface
    @property
    def walletId(self) -> int:
        """Return the wallet identifier (read‑only)."""
        return self.__walletId

    def get_balance(self) -> float:
        """Return the current balance."""
        return self.__balance
    
    def get_history(self) -> list[tuple[datetime, str, float]]:
        """Return a copy of the transaction history."""
        return list(self.__history)

    # Core operations
    def deposit(self, amount: float) -> None:
        '''Add *amount* to to balance.'''
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        self.__balance += amount
        self.__record("DEPOSIT", amount)

    def withdraw(self, amount: float) -> None:
        '''Subtract *amount* from balance.'''
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__record("WITHDRAW", amount)

    # Transaction log
    def __record(self, txn_type: str, amount: float) -> None:
        self.__history.append((datetime.now(), txn_type, amount))