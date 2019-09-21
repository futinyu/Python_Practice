# -*- coding: utf-8 -*-
#Author :The Y Devil
'''
算法:分治法（将一个复杂的问题划分为两个或多个相同相似的子问题，直到可以求解，原问题的解即子问题解的合集） ex：快排，归并
动态规划（通过把原问题分解为相对简单的子问题的方式求解复杂问题的方法，适用于有重叠子问题和最优子结构性质的问题）ex：背包问题，斐波那契
贪心法：（一种在每一步选择中都采取在当前状态下最好或最优（即最有利）的选择，从而希望导致结果是最好或最优的算法）
ex：哈夫曼编码，最小生成树
'''
'''
  :param  名称   最佳时间复杂度  最坏时间复杂度  数据稳定性
  :param  冒泡排序   n**2      n**2             稳定
  :param  选择排序   n**2      n**2             数组不稳定，链表稳定
  :param  插入排序   n**2      n**2             稳定
  :param  快速排序   nlogn     n**2             不稳定
  :param  堆排序     nlogn     nlogn            不稳定
  :param  归并排序   mlogn     nlog             稳定
  :param  计数排序   n+m       n+m              稳定
 '''
#快排
#递归思想，分而治之  复杂度很高
# def quicksort(List):
#     if len(List)<2:
#         return List
#     else:
#         zeroValue=List[0]
#         lowperList=[i for i in List[1:] if i<zeroValue ]
#         upperList=[i for i in List[1:] if i>zeroValue ]
#         newList=quicksort(lowperList)+[zeroValue]+quicksort(upperList)
#         return newList#不返回则报错
# a=[2,3,1,6,1,9,8,0,10]
# c=quicksort(a)
# print(c)

#另一种复杂度为n的快排方式
# def qucik_soft(L,left,right):
#     if left<right:
#         val_base=q_soft(L,left,right)
#         qucik_soft(L,left,val_base-1)
#         qucik_soft(L,val_base+1,right)
#     return L
# def q_soft(L,left,right):
#     key=L[left]#看做基础值
#     while left<right:
#         #对比右边:
#         print(L,key)
#         while left<right and L[right]>=key:
#             right-=1
#         L[left]=L[right]#首次交换值
#         print('right',L)
#         while left<right and L[left]<=key:
#             left+=1
#         L[right]=L[left]#遇到比他大的值，则覆盖在之前尾部指针
#         print('left', L)
#     L[left]=key
#     return left
# print(qucik_soft([2,4,8,3,1,0],0,5))


#选择排序法：find the smallest number  and  return，Complexity：O(n^2)
# def findSmall(arr):#find small number and return  Complexity:O(n)
#     smallest=arr[0]#存储最小值，默认取第一个
#     # smallindex=0#get the small number index
#     for i in range(1,len(arr)):
#         if(smallest>arr[i]):
#             smallest=arr[i]
#     return smallest
# def selectSort(arr):#read  the len for arr,and get the findSmall
#     new_Arr=[]
#     for i in range(len(arr)):
#         small=findSmall(arr)
#         arr.remove(small)
#         new_Arr.append(small)
#     return new_Arr
# print(selectSort([1,3,5,3,2,9,8]))

#另外一种选择
# def chose_sort(arr):
#     for i in range(len(arr)-1):
#         m=i
#         for j in range(i+1,len(arr)):
#             print(j)
#             if arr[m]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[m]
#     return arr


#-----------冒泡法--------------
# def budd_sort(arr):
#     for i in range(1,len(arr)):
#         for j in range(0,len(arr)-i):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
#     return arr
# print(budd_sort([3,1,2,6,7,8,10,1]))

#---------------------归并法----------------
'''
 先对列表进行作业拆分，在合并
'''
# def merge_sort(arr):
#     if len(arr)<2:#列表剩余1时，返回
#         return arr
#     mid=len(arr)//2
#     left=merge_sort(arr[:mid])#进行递归调用
#     right=merge_sort(arr[mid:])
#     return merge(left,right)
# def merge(left,right):#合并
#     i,j=0,0#记录下标
#     left_len=len(left)
#     right_len=len(right)
#     new_merge=[]#合成新的列表
#     while i<left_len and j<right_len:
#         if left[i]<=right[j]:
#             new_merge.append(left[i])
#             i+=1#有一个列表比较完就退出
#         else:
#             new_merge.append(right[j])
#             j+=1
#     #减少代码使用，不做判断
#     new_merge.extend(left[i:])
#     new_merge.extend(right[j:])
#     print(left,right,new_merge)#跟踪查看
#     return new_merge
# a=[9,2,1,4,6,7,4,0]
# print(merge_sort(a))

n=108
#a=sum([i for i in range(1,109)])
b=sum([j for j in range(1,109) if j%4==0 and j%6!=0])
d=sum([h for h in range(1,109) if h%6==0])
print(b+d)