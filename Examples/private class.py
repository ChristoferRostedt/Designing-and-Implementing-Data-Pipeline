class Test:
    def __init__(self):
        self.__x = 10 # Python changes this to format _Test__x
        self._x = 20 # Just a naming convention

t = Test()
# print(t.__x) # does not work
print(t._Test__x)