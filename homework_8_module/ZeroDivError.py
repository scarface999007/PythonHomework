class ZeroDivError(ZeroDivisionError):
    def __init__(self, txt):
        self.txt = txt

