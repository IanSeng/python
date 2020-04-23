class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"Not airline code in '{number}'")
        self._number = number

    def number(self):
        return "SN060"

    def number2(self):
        return self._number