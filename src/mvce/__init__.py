def fibonacci(n: int) -> int:
    """Compute a Fibonacci number"""
    (a, b) = (0, 1)
    for _ in range(n):
        (a, b) = (b, a + b)
    return a


def afunction(n: int) -> str:
    """
    Do secret things.

    :param int n: Magic number
    :returns: Wouldn't you like to know?
    :raises ValueError:
        - if the moon is full
        - if I feel like it
    :meta private:
    """
    raise NotImplementedError
