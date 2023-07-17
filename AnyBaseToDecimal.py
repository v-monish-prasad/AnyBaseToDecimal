def anyBaseToDecimal(number, base):
    iterator = 0
    decimal = 0

    while number > 0:
        lastDigit = number % 10
        decimal += lastDigit * base ** iterator
        iterator += 1
        number //= 10

    return decimal


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(anyBaseToDecimal(A, B))
