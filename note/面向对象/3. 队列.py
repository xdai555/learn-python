# 内置的数据结构
# {}    字典
# []    列表
# ()    元组
# {1,}  集合

# 其他一些
    # 队列（queue）：先进先出 First in first out
    # 栈（stack）：后进后出 Last in first out
# 使用列表实现队列和栈
# class QueueDemo(object):
#     def __init__(self):
#         self.data = []
#     def put(self, put_data):
#         self.put_data = self.data.append(put_data)
#     def get(self):
#         return self.data.pop(0)
#
# q1 = QueueDemo()
# print(q1.data)
# q1.put('1')
# q1.put('2')
# print(q1.data)
# print(q1.get())
# print(q1.get())
# q2 = QueueDemo()
# print(q2.data)
# q2.put('333')
# q2.put('444')
# print(q2.data)
# print(q2.get())
# print(q2.get())
#
#
# class StackDemo(object):
#     def __init__(self):
#         self.data = []
#     def put(self, put_data):
#         self.put_data = self.data.append(put_data)
#     def get(self):
#         return self.data.pop()
#
# s1 = StackDemo()
# print(q1.data)
# s1.put('1')
# s1.put('2')
# print(s1.data)
# print(s1.get())
# print(s1.get())
