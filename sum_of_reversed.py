def sum_of_reversed(arr):
    total = 0

    for num in arr:
        curr = num
        seen = False
        number_of_zeros = 0
        num = 0

    while curr:
        c = curr % 10
        if c > 0:
            seen = True
        if not seen and c == 0:
            number_of_zeros += 1
        elif c >= 0 and seen:
            num = num * 10 + c
        curr = curr // 10

        num = num * 10**number_of_zeros
        total += num

    return total


print(sum_of_reversed([5000, 123, 40500, 1]))
