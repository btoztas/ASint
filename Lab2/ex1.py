
class rpnCalculator:

    memory = []

    def pushValue(self, num):
        self.memory.insert(0, num)

    def popValue(self):
        return self.memory.pop(0)

    def add(self):
        sum = self.memory.pop(0) + self.memory.pop(0)
        self.memory.insert(0, sum)


calc = rpnCalculator()

calc.pushValue(10)
print(calc.popValue())

calc.pushValue(5)
calc.pushValue(10)
calc.add()
print(calc.popValue())

