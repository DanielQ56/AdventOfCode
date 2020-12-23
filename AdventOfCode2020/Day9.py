
def GetInvalidNumber(nums, size):

    start = 0
    end = size

    while end < len(nums):
        bracket = nums[start:end]
        bracket.sort()

        if not CheckForSum(bracket, nums[end]):
            return nums[end]
        
        start += 1
        end += 1

    return -1

def CheckForSum(bracket, target):
    start = 0
    end = len(bracket) - 1
    while start < end:
        s = bracket[start] + bracket[end]

        if s < target:
            start += 1
        elif s > target:
            end -= 1
        else:
            return True
        
    return False

def FindWeakness(nums, size):
    target = GetInvalidNumber(nums, size)

    start = 0
    series = []

    while start < len(nums):
        index = start
        while sum(series) < target and index < len(nums):
            series.append(nums[index])
            index += 1

            if sum(series) == target:
                series.sort()
                return series[0] + series[len(series)-1]
        series.clear()
        start += 1
    return -1

if __name__ == "__main__":
    inputFile = open("Day9Input.txt")

    nums = inputFile.readlines()

    nums = [int(num) for num in nums]

    print(FindWeakness(nums, 25))

    inputFile.close()