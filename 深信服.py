# -*- coding: utf-8 -*-
#Author :The Y Devil

'''
1.从字符串string开始完整匹配子串sub，返回匹配到的字符个数。

sub中如果出现'?'表示可以匹配一到三个除'\0'以外的任意字符。
如果sub还有找不到匹配的字符，则说明不能完整匹配。

如果能完整匹配，返回匹配到的字符个数，如果有多种匹配方式，返回匹配字符数最少的那个，如果不能完整匹配，返回-1
'''
#这是看完一个老哥写的 真的很简单 我当时根本没想着去用正则
import re
def get_index():
    string=input()
    part=input()
    sub_part=part.replace('?','.{1,3}')#替换?,生成正则表达式的子串
    try:
        res = re.search(sub_part, string).span()
        b = res[1]
        a = res[0]
        res_len = b - a
        print(res_len)
    except Exception:
        print(-1)



'''
2.
有K种颜色的小球(K<=10)，每种小球有若干个，总数小于100个。
现在有一个小盒子，能放N个小球(N<=8)，现在要从这些小球里挑出N个小球，放满盒子。
想知道有哪些挑选方式。注：每种颜色的小球之间没有差别。

请按数字递增顺序输出挑选小球的所有方式。

如有3种颜色，每种颜色小球的个数分别为a:1,b:2,c:3，挑出3个小球的挑法有：
003,012,021,102,111,120
'''
# K,N=map(int,input('输入种类和数量：').split(' '))
def ball(i,mydic,num,res,s):
    #种类  取值  盒子的数量  存放可能的情况  为每次生成一个数列
    if i==K and num==N:
        res.append(''.join(s))
    elif i<K:
        for use in range(mydic[i]+1):
            if use<=N-num:
                s.append(str(use))
                ball(i+1,mydic,num+use,res,s)
                s.pop()
            else:
                break
# if __name__ == '__main__':
#     res=[]
#     mydic={} #存放球类的字典以及他们的数量
#     val=input().split(' ')
#     for i in range(K):
#         mydic[i]=int(val.pop(0))
#     ball(0,mydic,0,res,[])
#     for r in res:
#         print(r)


