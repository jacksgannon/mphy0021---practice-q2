class SimpleMaths():
    '''
    A simple class to allow calculations to be performed on an integer.
    '''
    def __init__(self, number):
        if type(number) != int:
            raise TypeError("Error: Integer not passed into SimpleMaths constructor")
        self.number = number

    def square(self):
        x = self.number
        if self.number < 0: 
            x*(-1)
        return x ** 2

    def _factorial(self, value):
        if value == 0:
            return 1
        else:
            return value * self._factorial(value - 1)

    def factorial(self):
        if self.number < 0:
            raise TypeError("Error: No defined factorial for negative integer")
        return self._factorial(self.number)

    def power(self, power=3):
        if type(power) != int or type(power) != float:
            raise TypeError("Error: Incompatible data type passed in")
        return self.number ** power

    def odd_or_even(self):
        '''
        Note that this code assumes that 0 is even.
        '''
        if (self.number % 2) == 0:
            return 'Even'
        elif (self.number % 2) == 1:
            return 'Odd'

    def square_root(self):
        
        return self.number ** (0.5)
