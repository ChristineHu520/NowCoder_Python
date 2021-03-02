# -*- coding: utf-8 -*-
"""
# @Time    : 2021/3/1 9:04
# @Author  : ChristineHu
"""

"""
n 只奶牛坐在一排，每个奶牛拥有 ai 个苹果，现在你要在它们之间转移苹果，使得最后所有奶牛拥有的苹果数都相同，
每一次，你只能从一只奶牛身上拿走恰好两个苹果到另一个奶牛上，问最少需要移动多少次可以平分苹果，如果方案不存在输出 -1。
输入描述:
	每个输入包含一个测试用例。每个测试用例的第一行包含一个整数 n（1 <= n <= 100），接下来的一行包含 n 个整数 ai（1 <= ai <= 100）。
输出描述:
	输出一行表示最少需要移动多少次可以平分苹果，如果方案不存在则输出 -1。
示例1
输入
	4
	7 15 9 5
输出
	3
"""

"""
1：苹果总数不能整除奶牛总数
2：苹果数，不能通过2的移动来达到平均数
3：移动次数 = 大于均值或者小于均值的和/2（除以2是因为一次移动两个苹果）
"""

# 优化代码
# def solve(nums):
# 	_sum = sum(nums)
# 	if _sum % len(nums):
# 		return -1
# 	avg = _sum // len(nums)
# 	res = 0
# 	for n in nums:
# 		if abs(n - avg) % 2:
# 			return -1
# 		res += abs(n - avg)
# 	return res // 4

# 代码无措，程序超时
def solve(nums):
	avge = sum(nums) / int(N)
	if sum(nums) % int(N) != 0:
		print(-1)
	else:
		count = int(0)
		while True:
			nums.sort()
			if nums[0] == nums[-1]:
				break
			else:
				nums[0] += 2
				nums[-1] -= 2
				count += 1
		return count


if __name__ == '__main__':
	N = int(input())
	nums = list(map(int, input().split()))
	print(solve(nums))
