# -*- coding: utf-8 -*-
"""
# @Time    : 2021/3/2 8:41
# @Author  : ChristineHu
"""

"""
题目描述
    航天飞行器是一项复杂而又精密的仪器，飞行器的损耗主要集中在发射和降落的过程，科学家根据实验数据估计，
    如果在发射过程中，产生了 x 程度的损耗，那么在降落的过程中就会产生 x2 程度的损耗，
    如果飞船的总损耗超过了它的耐久度，飞行器就会爆炸坠毁。问一艘耐久度为 h 的飞行器，
    假设在飞行过程中不产生损耗，那么为了保证其可以安全的到达目的地，只考虑整数解，至多发射过程中可以承受多少程度的损耗？
输入描述:
    每个输入包含一个测试用例。每个测试用例包含一行一个整数 h （1 <= h <= 10^18）。
输出描述:
    输出一行一个整数表示结果。
示例1
输入
 10
输出
 2
"""

"""
1、对于h开方向下取整，如果可以满足x+x**2小于等于h则返回x，否则向下取一个数字，就可以满足
2、（x-1）**2=x**2-2X+1<x**2 + x
"""
from math import floor, sqrt


def spacecraft(h):
	x = floor(sqrt(h))
	if x + x ** 2 <= h:
		return x
	else:
		return x - 1


if __name__ == '__main__':
	h = int(input())
	print(spacecraft(h))
