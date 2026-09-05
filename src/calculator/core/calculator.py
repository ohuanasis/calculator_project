"""Framework-independent calculator operations."""


class Calculator:
    """Perform basic arithmetic on two numbers."""

    def add(self, first_number: float, second_number: float) -> float:
        """Return the sum of two numbers."""
        return first_number + second_number

    def subtract(self, first_number: float, second_number: float) -> float:
        """Subtract the second number from the first."""
        return first_number - second_number

    def multiply(self, first_number: float, second_number: float) -> float:
        """Return the product of two numbers."""
        return first_number * second_number

    def divide(self, first_number: float, second_number: float) -> float:
        """Divide the first number by the second.

        Raises:
            ValueError: If the second number is zero.
        """
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")

        return first_number / second_number
