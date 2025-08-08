"""Prompt user for two numbers, add them, and print the result."""


def main() -> None:
    """Read two numbers from the user, add them, and print the sum."""
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    result = first + second
    print(result)


if __name__ == "__main__":
    main()
