class Counter:
    # Private
    __count: int = 0
    
    # All below are public
    def increase(self) -> None:
        self.__count += 1
        return None
    def read(self) -> int:
        return self.__count
    def reset(self) -> None:
        return self.__count
    
counter1 = Counter() # Initialize Counter object
print("count:", counter1.read()) # count: 0
counter1.increase()
print("count:", counter1.read()) # count: 1
counter1.__count = 4 # Illegal operation
print("count:", counter1.read()) # count: 1

# Note! Python private isn't fully encapsulated
counter1._Counter__count = 9 # modifying the private property
print(counter1.read()) # count: 9