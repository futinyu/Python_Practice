# -*- coding: utf-8 -*-
#Author :The Y Devil

#实现两个节点的加法输入2->4->3  5->6->4 得出7->0->8
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         re=ListNode(0)#init one List Node
#         r=re
#         carry=0
#         while l1 or l2:#无论谁在循环都需要继续执行
#             x=l1.val if l1 else 0#获取他们的值
#             y=l2.val if l2 else 0
#             s=carry+x+y#carry是一个用来表示进位的值
#             carry=s//10
#             r.next=ListNode(s%10)
#             r=r.next
#             if l1!=None:l1=l1.next
#             if l2!=None:l2=l2.next
#         if carry>0:#若最后相加往前进一
#             r.next=ListNode(1)
#         return re.next
#
# a=Solution()
# b=ListNode(2)
# b.next=ListNode(4)
# b.next.next=ListNode(3)
# c=ListNode(5)
# c.next=ListNode(6)
# c.next.next=ListNode(4)
# res=a.addTwoNumbers(b,c)
# while res:
#     print(res.val,end=' ')
#     res=res.next

'''
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
#暴力法 ， 还可以使用字典模拟hash
# class Solution:
#     def twoSum(self,nums, target):
#         for i in range(len(nums)):
#             val=target-nums[i]
#             if val in nums and nums.count(val)==1 and val!=nums[i]:#不存在重复的val
#                     j=nums.index(val)
#                     return [i,j]


''':给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度
   :采用窗口滑动的想法来使用 列表来模拟该窗口
'''
# def shot(s):
#     widget=[]
#     max_num=0#记录最大长度
#     for i in s:
#         if i in widget:#窗口中存在该字母，记录本次长度，并从左边取出一个数，直到取到了该
#             num=len(widget)
#             while i in widget:#
#                 res=widget.pop(0)
#                 if res==i:
#                     break
#             max_num=num if num>max_num else max_num
#         else:
#             widget.append(i)
#     max_num=len(widget) if len(widget)>max_num else max_num
#     return max_num


'''给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 
两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素'''
# def twoSum(nums, target):
#     '''
#     :这样的时间大概为1400ms
#     for i in range(len(nums)):
#         val=target-nums[i]
#         if val in nums[i+1:]:
#             j=nums.index(val,i+1)
#             return [i,j]
#     '''
#     lens = len(nums)
#     j = -1
#     for i in range(1, lens):
#         temp = nums[:i]#切片花的时间大大缩短
#         if (target - nums[i]) in temp:
#             j = temp.index(target - nums[i])
#             break
#     if j >= 0:
#         return [i,j]


#求一个集合他的幂集,递归的方法
# def PowerSet(items):
#     if len(items)==0:#返回条件
#         return [[]]
#     all_set=[]
#     first=items[0]#待组合
#     sub_dic=items[1:]
#     #print(first,sub_dic)#
#     for power in PowerSet(sub_dic):#类似于切片
#         all_set.append(power)#把基类列表添加
#         new_set=power[:]+[first]
#         all_set.append(new_set)
#     return all_set
# print(PowerSet([1,2,3]))


'''使用树的方法 左取右边舍   回溯法：先把问题化成树或者图，在来遍历'''
# class Node(object):
#     def __init__(self,data):
#         self.data=data#存在的是一个列表
#         self.lchild=None
#         self.rchild=None
# def PowerSet(alist,node):
#     if alist==[]:
#         return
#     b=alist.pop(0)
#     left_a=alist.copy()#此步骤开辟多个内存块，未想到解决办法
#     right_a=alist.copy()
#     node.rchild=Node(node.data)
#     if node.data==None:
#         node.lchild=Node([b])
#     else:
#         node.lchild = Node([b]+node.data)
#     PowerSet(left_a,node.lchild)
#     PowerSet(right_a,node.rchild)
# def preorder(node):
#     if node.lchild is None:
#         if node.data==None:
#             return [[]]
#         else:
#             return [node.data]
#     return preorder(node.lchild)+preorder(node.rchild)
# node=Node(None)
# PowerSet([1,2,3,4],node)#创建一个这样的二叉树
# a=preorder(node)#遍历
# b=sorted(a)
# print(b,len(b))