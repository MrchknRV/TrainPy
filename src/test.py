def single_number(nums: list) -> int:
    xor_res = 0
    for el in nums:
        xor_res ^= el
    return xor_res


numbers = [4, 3, 2, 3, 2]
print(single_number(numbers))
