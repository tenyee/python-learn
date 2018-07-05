#!/bin/env python
# -*- coding:utf-8 -*-

'''
本节主要学习一下Python中如何创建类以及实例化对象
'''
'''
example-1 
一个简单的类

__init__是一个内置方法，相当于类创建对象时的构造函数，一定会被调用
方法内，我们为类的每个对象创建了一个属性:name
注意到每个方法的第一个参数都是self，这个函数指示了对象本身，相当于指针。
函数__init__不是必要的，如果不写，系统会生成一个默认的
通常在__init__中会定义对象的属性
'''
class CHuman:
	def __init__(self, name = "abc", age = 0):
		self.name = name

	def GetName(self):
		return self.name

	def SetName(self, name=""):
		self.name = name

	#不确定什么时候会被调用，python有gc机制，要显示调用可以用关键字del 
	def __del__(self):
		print("del CHuman Object:", self.name)

#1.创建对象
tom = CHuman()
print(tom.GetName())
#显示删除
del tom

#离开作用域自动删除
def foo():
	a = CHuman("FOO")

foo()



'''
example-2
类定义块中，其实也是一段可执行代码，解释器在生成类时，会执行类体内的代码，如下：

'''
class CTest:
	print("CTest...")

	def Show(self):
		print("haha...")

#2.创建对象
t1 = CTest()
t1.Show()
t2 = CTest()
t2.Show()
#输出结果为：
#CTest...
#haha...
#haha...
#可见CTest只输出一次，这说明，类只会初始化一次

'''
example-3
类属性，其实就是类作用域的变量，下面做一个有对象计数器的类

通过类名的方式来引用类属性
'''
class CCounter:
	count = 0

	def __init__(self):
		CCounter.count = CCounter.count + 1

	def GetCount(self):
		return CCounter.count

#3.创建对象
c1 = CCounter()
print("count:", c1.GetCount())
c2 = CCounter()
print("count:", c2.GetCount())






