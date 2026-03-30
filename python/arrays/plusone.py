def plusOne(digits: [int]):
    if digits[-1] < 9:
        digits[-1] = digits[-1] + 1
        return digits
    # if last digit is == 9
    add = True
    for i in range(len(digits) - 1, -1, -1):
        if add and digits[i] == 9:
            digits[i] = 0
        elif add:
            digits[i] += 1
            add = False

        if not add:
            break

    if add:
        digits.append(1)
        digits[-1], digits[0] = digits[0], digits[-1]
    return digits


digit = [9]
print(plusOne(digit))
