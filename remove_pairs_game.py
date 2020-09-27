def remove_pairs_game(arr):
    stack = [arr[0]]
    length = len(arr)
    total = 0

    for i in range(1, length):
        if len(stack) == 0 or arr[i] != stack[-1]:
            stack.append(arr[i])
        elif arr[i] == stack[-1]:
            stack.pop()
            total += 1

    print(total)

    return 'Alice' if total % 2 == 1 else 'Bob'


print(remove_pairs_game([1, 2, 2, 1, 3, 2, 2, 1, 4, 4, 1]))
