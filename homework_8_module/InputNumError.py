class InputNumError(ValueError):
    def __init__(self, txt):
        self.txt = txt
