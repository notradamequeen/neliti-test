def construct_match_math_operations(numbers, expected):
    # initialize the result variable
    result = f'{expected} = '
    res = 0
    # loop trough the index of array input
    for i in range(0, len(numbers)):
        # attach the first number to the result
        if i == 0:
            res += numbers[i]
            result += f'{numbers[i]}'
        else:
            # check if the index is not the last index
            if i < len(numbers) - 1:
                # check the match operation for current number
                if numbers[i] >= 0 and res + numbers[i] + numbers[i+1] <= expected:
                    res += numbers[i]
                    result += f' + {numbers[i]}'
                else:
                    res -= numbers[i]
                    result += f' - {numbers[i]}'
            else:
                # check the match operation for the last number
                if res + numbers[i] == expected:
                    res += numbers[i]
                    result += f' + {numbers[i]}'
                elif res - numbers[i] == expected:
                    res -= numbers[i]
                    result += f' - {numbers[i]}'
                else:
                    return None
    return result

print(construct_match_math_operations([1, 2, 3, 4, 5], 9))
print(construct_match_math_operations([2, 5, 60, -5, 3], 69))
