class Calculator:

    @staticmethod
    def add(*args):
        starting_value = 0
        for number in args:
            starting_value += number
        return starting_value

    @staticmethod
    def multiply(*args):
        starting_value = 1
        for number in args:
            starting_value *= number
        return starting_value

    @staticmethod
    def divide(*args):
        starting_value = args[0]
        for number in args[1:]:
            if number != 0:
                starting_value /= number
        return starting_value

    @staticmethod
    def subtract(*args):
        starting_value = args[0]
        for number in args[1:]:
            starting_value -= number
        return starting_value

print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
