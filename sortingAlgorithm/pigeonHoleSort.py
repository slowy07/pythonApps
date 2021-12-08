def pigeonHoleSort(nums):
    minNumbers = min(nums)
    maxNumbers = max(nums)

    size = maxNumbers - minNumbers + 1
    holes = [0] * size

    for x in nums:
        holes[x - minNumbers] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            nums[i] = count + minNumbers
            i += 1


nums = [12, 26, 77, 22, 88, 1]
print(pigeonHoleSort(nums))
print(nums)
