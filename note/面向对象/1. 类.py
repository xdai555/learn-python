# 类
# class 类名:
#     静态变量 = '值'
#     def 函数(self):
#        '函数体的内容'
#        pass
# 所有的变量和函数的内存地址都存储在类的命名空间里
# 对象
    # 对象 = 类名()
# 怎么用
    # 类可以实例化对象，类能操作静态变量
    # 操作类中的变量：类名.名字 = '值'
    # 操作对象的变量：对象.名字 = '值' / self.名字 = '值'

# 组合：类的对象是另一个类的属性
# 什么时候用？两个类之间 有什么有什么的关系  学生和班级、班级和课程、圆形和圆环
# class Course:
#     def __init__(self, name, period, price):
#         self.price = price
#         self.name = name
#         self.period = period
#
#
# class _Class:
#     def __init__(self, course):
#         self.course = course
#
#
# course_python = Course('python111', '6m', '2w')
# course_linux = Course('linux', '3m', '1.8w')
# python111 = _Class(course_python)
#
# linux111 = _Class(course_linux)
#
# print(linux111.course.period)
# print(python111.course.period)
# course_python.period = '10m'
# print(python111.course.period)

#
# from math import pi
# class Circle:
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         return pi*self.r**2
#     def perimeter(self):
#         return 2*pi*self.r
#
# class Ring:
#     def __init__(self, outer_r, inner_r):
#         outer_r, inner_r = (outer_r, inner_r) if outer_r > inner_r else (inner_r, outer_r)
#         self.outer_c = Circle(outer_r)
#         self.inner_c = Circle(inner_r)
#     def area(self):
#         return self.outer_c.area() - self.inner_c.area()
#     def perimeter(self):
#         return self.outer_c.perimeter() + self.inner_c.perimeter()
#
# ring1 = Ring(2,10)
# print(ring1.area())
# print(ring1.perimeter())
