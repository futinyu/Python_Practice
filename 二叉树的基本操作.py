# -*- coding: utf-8 -*-
#Author :The Y Devil
#二叉树的创建
# class Node(object):
#     def __init__(self,data):
#         self.data=data
#         self.lchild=None
#         self.rchild=None
# class Tree(object):
#     '''遍历的方式使用递归的方法，到达一颗子树，便把子树作为节点传入'''
#     def __init__(self):
#         self.root=None
#     def add(self,data):
#         node=Node(data)
#         if self.root==None:
#             self.root=node
#             return
#         queue=[self.root]
#         while queue:
#             curr_node=queue.pop(0)
#             if curr_node.lchild is None:
#                 curr_node.lchild=node
#                 return
#             else:
#                 queue.append(curr_node.lchild)
#             if curr_node.rchild is None:
#                 curr_node.rchild=node
#                 return
#             else:
#                 queue.append(curr_node.rchild)
#     def breath_travel(self):
#         if self.root==None:
#             return
#         queue=[self.root]
#         while queue:
#             curr_node=queue.pop(0)
#             print(curr_node.data,end=' ')
#             if curr_node.lchild is not None:
#                 queue.append(curr_node.lchild)
#             if curr_node.rchild is not None:
#                 queue.append(curr_node.rchild)
#     def preorde(self,node):
#         if node is None:
#             return
#         print(node.data,end=' ')
#         self.preorde(node.lchild)
#
#         self.preorde(node.rchild)
#     def midorder(self,node):
#         if node is None:
#             return
#         self.midorder(node.lchild)
#         print(node.data,end=' ')
#         self.midorder(node.rchild)
#     def postorder(self,node):
#         if node is None:
#             return
#         self.postorder(node.lchild)
#         self.postorder(node.rchild)
#         print(node.data,end=' ')
# if __name__ == '__main__':
#     tree=Tree()
#     for i in range(10):
#         tree.add(i)
#     tree.breath_travel()
#     print('\n先序')
#     tree.preorde(tree.root)
#     print('\n后续')
#     tree.postorder(tree.root)
#     print('\n中序')
#     tree.midorder(tree.root)

# class Node(object):
#     def __init__(self,data):
#         self.data=data
#         self.lchild=None
#         self.rchild=None
# class Tree(object):
#     def __init__(self):
#         self.root=None
#     def add(self,data):
#         node=Node(data)
#         if self.root==None:
#             self.root=node
#             return
#         queue=[self.root]
#         while queue:
#             curr_node=queue.pop(0)
#             if curr_node.lchild==None:
#                 curr_node.lchild=node
#                 return
#             else:
#                 queue.append(curr_node.lchild)
#             if curr_node.rchild==None:
#                 curr_node.rchild=node
#                 return
#             else:
#                 queue.append(curr_node.rchild)
#     def breath_travel(self):
#         if self.root==None:
#             return
#         queue=[self.root]
#         while queue:
#             curr_node=queue.pop(0)
#             print(curr_node.data,end=' ')
#             if curr_node.lchild!=None:
#                 queue.append(curr_node.lchild)
#             if curr_node.rchild!=None:
#                 queue.append(curr_node.rchild)
#     def preorder(self,node):
#         if node is None:
#             return
#         print(node.data,end=' ')
#         self.preorder(node.lchild)#迭代查看值
#         self.preorder(node.rchild)
#     def midorder(self,node):
#         if node is None:
#             return
#         self.midorder(node.lchild)  # 迭代查看值
#         print(node.data, end=' ')
#         self.midorder(node.rchild)
#     def postorder(self,node):
#         if node==None:
#             return
#         self.postorder(node.lchild)
#         self.postorder(node.rchild)
#         print(node.data,end=' ')
#     def find_child(self,node,data):
#         if node==None:
#             return
#         if self.root.data==data:
#             msg='这是根节点'
#             print(msg)
#             return
#         parent=node
#         if node.lchild is None:
#             return
#         else:
#             if node.lchild.data==data:
#                 msg='父节点为：{0},该节点为左孩子'.format(parent.data)
#                 print(msg)
#                 return
#             else:
#                 self.find_child(node.lchild,data)
#         if node.rchild is None:
#             return
#         else:
#             if node.rchild.data==data:
#                 msg='父节点为：{0},该节点为右孩子'.format(parent.data)
#                 print(msg)
#                 return
#             else:
#                 self.find_child(node.rchild,data)
#     def count_node(self,node):#recursion count the nodes
#         if node==None:
#             return 0
#         else:
#             return 1+self.count_node(node.lchild)+self.count_node(node.rchild)
#
#     def no_re_pro(self):#非递归 可以直接使用打印，可以使用非递归方法先序最简单
#         if self.root==None:
#             return
#         t=self.root
#         s=[]#模拟压栈
#         while t is not None or s:
#             while t is not None:
#                 yield t.data#print(t.data,end=' ')
#                 s.append(t.rchild)
#                 t=t.lchild
#             t=s.pop(-1)
#     def mirror(self,node):#镜像反转，利用递归的方法
#         if node==None:
#             return
#         node.lchild,node.rchild=node.rchild,node.lchild
#         self.mirror(node.lchild)
#         self.mirror(node.rchild)
# if __name__ == '__main__':
#     tree=Tree()
#
#     for i in range(10):
#         tree.add(i)
#     print()
#     tree.preorder(tree.root)
#     print()
#     tree.mirror(tree.root)
#     tree.preorder(tree.root)

    # res = tree.nopro()#查看生成器中的值
    # try:
    #     while True:
    #         print(res.__next__(),end=' ')
    # except StopIteration:
    #     pass

    # tree.breath_travel()

    # print()
    # tree.midorder(tree.root)
    # print()
    # tree.postorder(tree.root)
    # print('\n查找孩子：')
    # tree.find_child(tree.root,8)
    # print(tree.count_node(tree.root))
print(10//10)