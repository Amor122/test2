# #coding=utf-8
# # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))
#
# #coding=utf-8
# # 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)


# 1
# 规则，找数组中满足A=B+2c的规则
# import sys
#
# n = int(sys.stdin.readline().strip())
# dtl = list(map(int, sys.stdin.readline().strip().split()))
# dtl.sort()
# A = B = C = 0
# label = False
# while dtl:
#     if label:
#         break
#     A = dtl.pop()
#     leng = len(dtl)
#     for i in range(leng):
#         if label:
#             break
#         for j in range(leng):
#             if i == j:
#                 continue
#             count = dtl[i] + 2 * dtl[j]
#             if count == A:
#                 B = dtl[i]
#                 C = dtl[j]
#                 label = True
#                 break
# if label:
#     print(A, B, C)
# else:
#     print(0)


# 2 多组整数数组需要合并为一个新的数组
# 从每个数组按照顺序取出固定长度的内容合并到新数组，
# 如果长度小于固定长度就全部拿下，
# 60%
# import sys
# # 每次取得的长度
# leng = int(sys.stdin.readline().strip())
# # 数组数目
# n = int(sys.stdin.readline().strip())
# # 截取2*l-1个数组,循环跑，跑到列表为空
# st = ''
# stl = []
# for i in range(n):
#     xx=sys.stdin.readline().strip()
#     stl.append(xx)
# while stl:
#     num = len(stl)
#     for i in range(num):
#         if stl[i]==',':
#             stl[i]=''
#         if stl[i]=='':
#             continue
#         if stl[i].startswith(','):
#             stl[i]=stl[i][1:]
#         if len(stl[i])<2*leng-1:
#             st+=stl[i]+','
#             stl[i]=''
#         else:
#             st+=stl[i][:2*leng-1]+','
#             stl[i]=stl[i][2*leng-1:]
#     while '' in stl:
#         stl.remove('')
# print(st[:-1])

# 95%
# import sys
# # 每次取得的长度
# leng = int(sys.stdin.readline().strip())
# # 数组数目
# n = int(sys.stdin.readline().strip())
# # 截取2*l-1个数组,循环跑，跑到列表为空
# st = ''
# stl = []
# for i in range(n):
#     xx = list(sys.stdin.readline().strip().split(','))
#     if xx:
#         stl.append(xx)
# # 源头确保没有空列表
# num = len(stl)
# # 将用完的列表标记
# ss = [1]*num
# data_list=[]
# while sum(ss):
#     for i in range(num):
#         if not ss[i]:
#             continue
#         if len(stl[i])<=leng:
#             data_list=data_list+stl[i]
#             ss[i]=0
#         else:
#             data_list+=stl[i][:leng]
#             stl[i]=stl[i][leng:]
# st= ''
# if data_list:
#     for i in data_list:
#         st+=str(i)+','
#     print(st[:-1])
# else: print(st)


# 3 25%
# import sys
#
# # 待系统执行的任务列表，数组的每一个元素代表一个任务，
# # 元素的值代表任务的类型
# tkl = list(map(int, sys.stdin.readline().strip().split(',')))
# # 任务冷却时间
# N = int(sys.stdin.readline().strip())
# # 每个任务耗时是一个时间单位，顺序随意
# # 同一个类型任务之间必须有冷却时间
#
# # 任务列表的长度
# L = len(tkl)
# # 最短时间
# M = 0
# # 本次启动的位置，标记列表，当前累计时间,冷却列表
# def qidong(i, label, S, cold):
#     # 使用过的直接抛弃
#     if label[i]:
#         return
#     global L, M, N
#     # 准备运行这个任务，查看他的受冷却时间
#     cot = cold[tkl[i]]
#     S = S + 1 + cot
#     label[i] = 1
#     # 已经比初始化过的最小值大了的直接修剪掉
#     if M != 0 and S >= M:
#         return
#     # 启动他，并 标记这个已经启动过了
#     # 所有的非0项减去冷却过的时间再减去1
#     # 计算下一个任务启动前的冷却表
#     for key in cold:
#         if cold[key] >= (cot + 1):
#             cold[key] -= (cot + 1)
#         else:
#             cold[key] = 0
#     # 下一轮这个任务的冷却时间就是N了
#     cold[tkl[i]] = N
#     if sum(label) == L:
#         # 全部走过了
#         if M == 0:
#             M = S
#         if S < M:
#             M = S
#     else:
#         # 还要继续往下走
#         for j in range(L):
#             if label[j]:
#                 continue
#             xx = label[:]
#             yy=cold.copy()
#             qidong(j, xx, S, yy)
#
# cold = {}
# for xx in tkl:
#         cold.update({xx: 0})
# for i in range(L):
#     # 标记列表,使用过的标记
#     label = [0] * L
#     # 冷却队列 ,字典，存储每个任务类型的值的冷却时间
#     xx=cold.copy()
#     # 随便启动第一个任务,拟启动的位置，标记列表，启动累计时间,冷却队列
#     qidong(i, label, 0, xx)
#
# print(M)
from typing import List


def qidong(i, label, S, cold):
    # 使用过的直接抛弃
    if label[i]:
        return
    global L, M, N
    # 准备运行这个任务，查看他的受冷却时间
    cot = cold[tkl[i]]
    S = S + 1 + cot
    label[i] = 1
    # 已经比初始化过的最小值大了的直接修剪掉
    if M != 0 and S >= M:
        return
    # 启动他，并 标记这个已经启动过了
    # 所有的非0项减去冷却过的时间再减去1
    # 计算下一个任务启动前的冷却表
    for key in cold:
        if cold[key] >= (cot + 1):
            cold[key] -= (cot + 1)
        else:
            cold[key] = 0
    # 下一轮这个任务的冷却时间就是N了
    cold[tkl[i]] = N
    if sum(label) == L:
        # 全部走过了
        if M == 0:
            M = S
        if S < M:
            M = S
    else:
        # 还要继续往下走
        for j in range(L):
            if label[j]:
                continue
            xx = label[:]
            yy=cold.copy()
            qidong(j, xx, S, yy)
import sys

tkl = eval(input())
N = int(input().strip())
L = len(tkl)
M = 0
cold = {}
for xx in tkl:
    cold.update({xx: 0})
for i in range(L):
    # 标记列表,使用过的标记
    label = [0] * L
    # 冷却队列 ,字典，存储每个任务类型的值的冷却时间
    xx=cold.copy()
    # 随便启动第一个任务,拟启动的位置，标记列表，启动累计时间,冷却队列
    qidong(i, label, 0, xx)

print(M)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        L = len(tasks)
        M = 0
        cold = {}
        for xx in tkl:
            cold.update({xx: 0})
        for i in range(L):
            # 标记列表,使用过的标记
            label = [0] * L
            # 冷却队列 ,字典，存储每个任务类型的值的冷却时间
            xx=cold.copy()
            # 随便启动第一个任务,拟启动的位置，标记列表，启动累计时间,冷却队列
            qidong(i, label, 0, xx)
        return
    def qidong(i, label, S, cold):
        # 使用过的直接抛弃
        if label[i]:
            return
        global L, M, N
        # 准备运行这个任务，查看他的受冷却时间
        cot = cold[tkl[i]]
        S = S + 1 + cot
        label[i] = 1
        # 已经比初始化过的最小值大了的直接修剪掉
        if M != 0 and S >= M:
            return
        # 启动他，并 标记这个已经启动过了
        # 所有的非0项减去冷却过的时间再减去1
        # 计算下一个任务启动前的冷却表
        for key in cold:
            if cold[key] >= (cot + 1):
                cold[key] -= (cot + 1)
            else:
                cold[key] = 0
        # 下一轮这个任务的冷却时间就是N了
        cold[tkl[i]] = N
        if sum(label) == L:
            # 全部走过了
            if M == 0:
                M = S
            if S < M:
                M = S
        else:
            # 还要继续往下走
            for j in range(L):
                if label[j]:
                    continue
                xx = label[:]
                yy=cold.copy()
                qidong(j, xx, S, yy)


