#!/usr/bin/env python


def twoSum(nums, target):
    l = len(nums)
    for n, i in enumerate(nums):
        for z in range(n+1, l):
            if i + nums[z] == target:
                return [n, z]


def main():
    z = [2, 7, 11, 15]
    y = 9
    print(twoSum(z, y))
    ab = [3, 2, 3]
    cd = 6
    print(twoSum(ab, cd))


if __name__ == '__main__':
    main()
