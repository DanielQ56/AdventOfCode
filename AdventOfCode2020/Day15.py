def NumSpoken(nums):
    num = {}

    for i in range(len(nums)):
        num[int(nums[i])] = i + 1
    print(num)
    cr = len(nums) + 1
    ln = 0
    while cr < 30000000:
        if ln in num:
            num[ln], ln = cr, cr - num[ln]
        else:
            num[ln] = cr
            ln = 0
        cr += 1

    return ln


if __name__ == "__main__":
    inputFile = open("Day15Input.txt")

    nums = inputFile.read().split(",")

    print(NumSpoken(nums))

    inputFile.close()