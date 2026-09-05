"""Command-line interface for the calculator."""

import argparse
from collections.abc import Sequence

from calculator import Calculator


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Perform basic operations on two numbers."
    )
    parser.add_argument("first_number", type=float, help="The first number.")
    parser.add_argument("second_number", type=float, help="The second number.")
    return parser


def main(arguments: Sequence[str] | None = None) -> int:
    """Parse arguments, perform the calculations, and print the results."""
    parsed_arguments = create_parser().parse_args(arguments)
    first_number = parsed_arguments.first_number
    second_number = parsed_arguments.second_number
    calculator = Calculator()

    print(f"Addition:       {calculator.add(first_number, second_number)}")
    print(f"Subtraction:    {calculator.subtract(first_number, second_number)}")
    print(f"Multiplication: {calculator.multiply(first_number, second_number)}")

    try:
        division_result = calculator.divide(first_number, second_number)
        print(f"Division:       {division_result}")
    except ValueError as error:
        print(f"Division:       {error}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())