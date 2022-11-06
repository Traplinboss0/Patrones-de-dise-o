class UndecoratedObject:
    @staticmethod
    def get():
        return "UndecoratedObject"

class DecoratedObject:
    def __init__(self, undecorated):
        self.undecorated = undecorated

    def get(self):
        return self.undecorated.get().replace("Undecorated", "Decorated")


UNDECORATED = UndecoratedObject()
print(UNDECORATED.get())

DECORATED = DecoratedObject(UNDECORATED)
print(DECORATED.get())