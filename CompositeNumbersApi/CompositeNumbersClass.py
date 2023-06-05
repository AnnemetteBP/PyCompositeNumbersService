from ICompositeNumbers import *

class CompositeNumbers(ICompositeNumbers):

    def check_number(self, number: int) -> bool:
        self.number = number
        if number <= 1 or number <= 3:
            return False
        elif number % 2 is 0 or number % 3 is 0:
            return True
        elif ():
            self.i = 5
            while self.i * self.i <= self.number:
                self.i += 6
                if self.number % self.i is 0 or self.number % (self.i + 2) is 0:
                    return True
        else:
            return False

    def check_numbers_list(self, num1: int, num2: int) -> list:
        self.num1 = num1
        self.num2 = num2
        self.composite_numbers_list = []
        self.count = 0

        for n in range(self.num1, self.num2):
            n += 1
            if self.check_number(n):
                self.count += 1
                self.composite_numbers_list.append(n)
        return self.composite_numbers_list