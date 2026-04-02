def divide(self, dividend: int, divisor: int) -> int:
    if dividend == divisor:
        return 1

    sign = True  # +ve
    if dividend >= 0 and divisor < 0:
        sign = False
    elif dividend < 0 and divisor > 0:
        sign = False

    n = abs(dividend)
    d = abs(divisor)
