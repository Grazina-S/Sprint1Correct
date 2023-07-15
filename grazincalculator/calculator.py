from decimal import Decimal  # Needed to avoid problems with floating point


class Calculator:
    """Has add/subtract, multiply/divide, root and reset functions"""

    def __init__(self):
        self.memory = None

    def add(self, *numbers: float) -> float:
        numbers = [Decimal(str(num)) for num in numbers]
        if self.memory is None:
            self.memory = numbers[0]
            numbers = numbers[1:]
        self.memory = Decimal(self.memory)
        self.memory += sum(numbers)
        return float(self.memory)

    def subtract(self, *numbers: float) -> float:
        numbers = [Decimal(str(num)) for num in numbers]
        if self.memory is None:
            if len(numbers) > 1:
                self.memory = numbers[0]
                numbers = numbers[1:]
                # If memory is empty 1st num becomes minuend
            else:
                self.memory = Decimal(0.0)
                # If memory is empty and one num is entered
                # minuend becomes 0.0
        self.memory = Decimal(self.memory)
        self.memory -= sum(numbers)
        return float(self.memory)

    def multiply(self, *numbers: float) -> float:
        numbers = [Decimal(str(num)) for num in numbers]
        if self.memory is None:
            if len(numbers) > 1:
                self.memory = numbers[0]
                numbers = numbers[1:]
            else:
                self.memory = Decimal(0.0)
        self.memory = Decimal(self.memory)
        for num in numbers:
            self.memory *= num
        return float(self.memory)

    def divide(self, *numbers: float) -> float:
        numbers = [Decimal(str(num)) for num in numbers]
        if self.memory is None:
            if len(numbers) > 1:
                self.memory = numbers[0]
                numbers = numbers[1:]
            else:
                self.memory = Decimal(0.0)
                # If memory is empty and one number is entered
                # dividend becomes 0
        self.memory = Decimal(self.memory)
        for num in numbers:
            self.memory /= num
        return float(self.memory)

    def root(self, *numbers: float) -> float:
        numbers = [Decimal(str(num)) for num in numbers]
        if self.memory is None:
            if len(numbers) != 2:
                raise ValueError("Enter number and root degree")
            else:
                self.memory = numbers[0] ** (1 / numbers[1])
                # If memory is empty and 2 arguments are entered
                # 1st becomes number and 2nd becomes root degree
        elif len(numbers) != 1:
            raise ValueError("Enter root degree or reset")
        else:
            self.memory = Decimal(self.memory) ** (1 / numbers[0])
        return float(self.memory)

    def reset(self):
        """Clean the memory"""
        self.memory = None
