# -*- coding: utf-8 -*-
#Author :The Y Devil
# d= {'a':24,'g':52,'i':12,'k':33}
# sorted(d.items(), key=lambda x: x[1])
# print(d.items())
# print(sorted(d.items(),key=lambda x:x[1]))
# print("aStr"[::-1])

#处理成字典
# s='k:1 |k1:2|k2:3|k3:4'
# dic={k:int(v) for i in s.split('|') for k,v in (i.split(":"), ) }#分解成两个数，需要用元祖来装
# print(dic)

#创建装饰器
# def sing(csl):
#     instent={}
#     def warp(*args,**kwargs):
#         if  csl not in instent:
#             instent[csl]=csl(*args,**kwargs)
#
#         return instent[csl]
#     return warp
# @sing
# class Func(object):
#     pass
# foo1=Func()
# foo2=Func()
# print(foo1,foo2)
# print(foo1 is foo2)

# class Sing(object): 单模式
#     _instance = None
#     def __init__(self):
#         pass
#     def __new__(cls, *args, **kwargs):#在__init__之前调用，生成唯一实例
#         if Sing._instance is None:
#             Sing._instance=object.__new__(cls,*args,**kwargs)
#             print(1)
#         return Sing._instance
#
# P=Sing('fty')#生成了唯一实例
# X=Sing()

#反转一个整数
# def revese(x):
#     if -10<x<10:
#         return x
#     str_x=str(x)
#     if str_x[0]!='-':
#         new_x=str_x[::-1]
#     else:
#         new_x='-'+str_x[1:][::-1]
#     return new_x
# print(revese(-231))

#设计遍历目录与子目录，抓取.pyc文件
# import os
# def get_file(dir,suffix):
#     res=[]
#     for read,dirs,files in os.walk(dir):#获取当前文件，当前文件下的目录，当前文件下的文件
#         for file in files:
#             head,body=os.path.splitext(file)#分隔标题和后缀
#             if body==suffix:
#                 res.append(os.path.join(head,body))#
#     return res
# dir='D:\pycharm\code\project'
# print(get_file(dir,'.py'))


#返回不存的字母
# def deal(string):
#     s=set("abcdefghijklmnopqrstuvwxyz")
#     s1=set(string.lower())
#     print("".join(sorted(s-s1)))#sorted生成的是列表
# deal('PYthon')

#求合到10248
# from functools import reduce
# a=sum([1,2,3,10248])
# print(a)
# num1 = reduce(lambda x,y :x+y,[1,2,3,10248])#reduce累积(function, iterable[, initializer])
# print(num1)

#统计词频，输出最高的十位
# import re
# words={}
# with open('file','r') as f:
#     for line in f:
#         line=re.sub('\W',' ',line)
#         lineone=line.split()
#         for word in line:
#             if words.get(word):
#                 words[word]+=1
#             else:
#                 words[word]=1
# data=sorted(words.items(),key=lambda x:x[1],reverse=True )[0:10]
# print(data)

#返回的数和索引都为偶数的情况
# def num_list(num):
#     return [i for i in num if i%2==0 and num.index(i)%2==0 ]
# num = [0,1,2,3,4,5,6,7,8,9,10]
# result = num_list(num)
# print(result)


#计算当前天数为多少天
# import datetime
# da=datetime.date(2016,10,31)
# dayCount=da-datetime.date(2015,12,31)
# print(dayCount)

#奇数升序，偶数降序，奇数在前
# def get(l):
#     if isinstance(l,str):
#         l=[int(i) for i in l]
#     l.sort(reverse=True)
#     for i in range(len(l)):
#         if l[i]%2>0:
#             l.insert(0,l.pop(i))
#     print([str(e) for e in l])
#
# s=[1,2,3,9,6,7,8]
# get(s)

#
# def count_str(str_data):
#     """定义一个字符出现次数的函数"""
#     dict_str = {}
#     for i in str_data:
#         dict_str[i] = dict_str.get(i, 0) + 1#存在取i,否则取0
#     return dict_str
# dict_str = count_str("AAABBCCAC")
# str_count_data = ""
# for k, v in dict_str.items():
#     str_count_data += k + str(v)
# print(str_count_data)

#装饰器带参数的
# def new_func(func):
#     def wrappedfun(username, passwd):
#         if username == 'root' and passwd == '123456789':
#             print('通过认证')
#             print('开始执行附加功能')
#             return func()
#        	else:
#             print('用户名或密码错误')
#             return
#     return wrappedfun
# @new_func
# def origin():
#     print('开始执行函数')
# origin('root','123456789')

#sorted使用以及key需要的是一个函数

#求list平均分并排序
# from random import randint
# def sortList():
#     a=[randint(1,100) for i in range(40)]
#     c=round(sum(a)/len(a),1)
#     b=[j for j in a if j<c]
#     print(c,':',b)
#     a.sort(reverse=True)
#     print(a)

#贪婪模式兑换硬币

# def Get_Num(money):
#     coins= [1, 2, 5,10,20,50,100]#1分，2分，5分，1角，2角，5角，1元
#     coins.sort(reverse=False)
#     money=money*100#化为整数
#     money_dict={}
#     while True:
#         the_coin=coins.pop()
#         count,money=divmod(money,the_coin)
#         if money==0:
#             the_coin=the_coin/100
#             money_dict[str(the_coin)+'元'] = int(count)
#             return money_dict
#         if count==0:
#             continue
#         the_coin = the_coin / 100
#         money_dict[str(the_coin)+'元']=int(count)
# 最佳置换
# def changeCoins(coins, n):
#     if n < 0: return None
#     dp, path = [0] * (n + 1), [0] * (n + 1)  # 初始化
#     for i in range(1, n + 1):
#         minNum = i  # 初始化当前硬币最优值
#         for c in coins:  # 扫描一遍硬币列表，选择一个最优值
#             if i >= c and minNum > dp[i - c] + 1:
#                 minNum, path[i] = dp[i - c] + 1, i - c
#         dp[i] = minNum  # 更新当前硬币最优值
#     print('dp')
#     print('最少硬币数:', dp[-1])
#     print('可找的硬币', end=': ')
#     while path[n] != 0:
#         print(n - path[n], end=' ')
#         n = path[n]

# def odd(x):return x%2==1#筛选条件，用filter
# def event(x):return x%2==0
# x=[i for i in range(15)]
# a,b=filter(odd,x),filter(event,x)
# c,d=[],[]
# while True:
#     try:
#         c.append(a.__next__()),d.append(b.__next__())
#     except Exception as e:
#         break
# print(c,d)

#斐波那契
# def Fibonacii(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return Fibonacii(n-1)+Fibonacii(n-2)
# print(Fibonacii(6))
#
# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#     return a
# print('fib:',fib(6))

# word=input('输入')
# a=word.split(' ')
#
# a.reverse()
# res=' '.join(a)
# print(res)
# a='a'
# print('ha%(args)s'%{'args':a})
# print('sads{arsg}'.format(arsg=a))
# print('as{0}'.format(a))


#a=[1,2,3,4]
#c=map(lambda x:x*x,a)#返回一个迭代器，前者是执行的函数，后者为序列

#垃圾回收机制    1.引用计数     2.标记清除机制  对象引用视为节点，边（按需分配，标记节点）  3.分代技术


# 对于除法 /是指除以，//是取商，%取余数       python2是有float是除以





#添加0000000000-99999999id 不包含3,4,7
# import time
# def shengguo():
#     #available_num:recard use id
#     #
#     #res not print beacuse it use some time
#     available_num=0
#     starttime=time.time()
#     for i in range(1000):
#         if str(i)=='0':
#             left_number='0000'
#         else:
#             left_number=(4-len(str(i)))*'0'+str(i)
#         if '3' in left_number or '4' in left_number or '7' in left_number:
#             continue#继续循环
#         for j in range(1000):
#             if str(j) == '0':
#                 right_number = '0000'
#             else:
#                 right_number = (4 - len(str(j))) * '0' + str(i)
#             if '3' in right_number or '4' in right_number or '7' in right_number:
#                 continue
#             available_num+=1
#             res=left_number+right_number
#
#     endtime=time.time()
#     return available_num,endtime-starttime
# a,usetime=shengguo()
# print('可以使用的id:%s,本次使用时间为:%s'%(a,usetime))





