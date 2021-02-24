# -*- coding: utf-8 -*-
"""
# @Time    : 2021/2/22 8:48
# @Author  : ChristineHu
"""
"""
题目描述
	小易经常沉迷于网络游戏.有一次,他在玩一个打怪升级的游戏,他的角色的初始能力值为 a.在接下来的一段时间内,他将会依次遇见n个怪物,每个怪物的防御力为b1,b2,b3...bn. 如果遇到的怪物防御力bi小于等于小易的当前能力值c,那么他就能轻松打败怪物,并 且使得自己的能力值增加bi;如果bi大于c,那他也能打败怪物,但他的能力值只能增加bi 与c的最大公约数.那么问题来了,在一系列的锻炼后,小易的最终能力值为多少?
输入描述:
	对于每组数据,第一行是两个整数n(1≤n<100000)表示怪物的数量和a表示小易的初始能力值.
	第二行n个整数,b1,b2...bn(1≤bi≤n)表示每个怪物的防御力
输出描述:
	对于每组数据,输出一行.每行仅包含一个整数,表示小易的最终能力值
示例1
输入
	3 50
	50 105 200
	5 20
	30 20 15 40 100
输出
	110
	205
"""


def hcf(num1, num2):
	smaller = num1 if num1 <= num2 else num2
	hcf_num = 1
	for i in range(1, smaller + 1):
		if (num1 % i == 0) and (num2 % i == 0):
			hcf_num = i
	return hcf_num


def dfs(n, a, N, b):
	if n == int(N)-1:
		return a
	else:
		if a < int(b[n]):
			a += hcf(a, int(b[n]))
		else:
			a += int(b[n])
		dfs(n + 1, a, N,b)


if __name__ == '__main__':
	N = input("怪物的数量N：")
	a = input("小易的初始能力值：")
	b = list(input().strip().split())
	print(dfs(0, int(a), int(N), b))
