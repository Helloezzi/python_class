class Calculator:
    def __init__(self):
        self.result = 0

    def sum(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def multiply(self, num1, num2):
        res = num1 * num2
        return res