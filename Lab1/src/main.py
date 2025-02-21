def add(first: int, second: int) -> int:
    return first + second


def max(digits: any) -> any:
    if not digits:
        return None

    result = digits[0]

    for digit in digits:
        if digit == None:
            return None

        if result < digit:
            result = digit

    return result


def is_perfect(n):
    if n < 2:
        return False

    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i

    return total == n


if __name__ == "__main__":
    list = [1,2,3]
    print(max(list))