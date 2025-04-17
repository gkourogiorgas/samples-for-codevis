from functools import reduce
from math import pow


class Operation:
    """Base class for all mathematical operations"""

    def __init__(self, name):
        self.name = name

    def execute(self, numbers):
        """Execute the operation on the list of numbers"""
        raise NotImplementedError("Subclasses must implement execute method")

    def __str__(self):
        return self.name


class Addition(Operation):
    """Addition operation"""

    def __init__(self):
        super().__init__("Addition")

    def execute(self, numbers):
        return sum(numbers)


class Multiplication(Operation):
    """Multiplication operation"""

    def __init__(self):
        super().__init__("Multiplication")

    def execute(self, numbers):
        return reduce(lambda x, y: x * y, numbers)


class Power(Operation):
    """Power operation (applies the power sequentially)"""

    def __init__(self):
        super().__init__("Power")

    def execute(self, numbers):
        if not numbers:
            return 0
        result = numbers[0]
        for num in numbers[1:]:
            result = pow(result, num)
        return result


class Average(Operation):
    """Average operation"""

    def __init__(self):
        super().__init__("Average")

    def execute(self, numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)


class Maximum(Operation):
    """Maximum operation"""

    def __init__(self):
        super().__init__("Maximum")

    def execute(self, numbers):
        if not numbers:
            return 0
        return max(numbers)


class Minimum(Operation):
    """Minimum operation"""

    def __init__(self):
        super().__init__("Minimum")

    def execute(self, numbers):
        if not numbers:
            return 0
        return min(numbers)
