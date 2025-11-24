def factorial(n: int) -> int:
    """
    Calculate n! with basic validation.

    Args:
        n: Integer whose factorial is required.

    Returns:
        Factorial of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if n in (0, 1):
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial(5))