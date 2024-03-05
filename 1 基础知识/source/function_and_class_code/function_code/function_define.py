def function_define():
    print("函数定义")


def function_return():
    return 'function return'


def function_param(name, age):
    print('name = %s, age = %s' % (name, age))


def function_param_default(name, age=None):
    print('name = %s, age = %s' % (name, age))


def function_param_indefinite_default(name, age=26, *args, **kwargs):
    print('name = %s, age = %s, type(args) = %s, args = %s, type(kwargs) = %s, kwargs = %s' % (
        name, age, type(args), args, type(kwargs), kwargs))


def function_return_param():
    return 1, 2, 3, 'hello'


def function_pass():
    pass


# 函数中未使用 return 该函数默认会返回 None
# function_define()

# ret = function_return()
# print(type(ret), ret)

# function_param('tan', 25)
# function_param(name='tan', age=25)

# 如果形参有多个 可以必需参数和默认参数混合使用 但是在形参中 默认参数靠后书写
# function_param_default('tan')
# function_param_default('tan', 26)

# 不定参数
# *args 中 args 会被当做元组处理，在调用函数的时候，实参可以传递任意个参数
# **kwargs 中 kwargs 会被当做字典处理，所以实参需要以key=value的方式传参,key一定是一个合法的变量名
# 说明: 不定长参数经常会同时使用 格式: def xxx(*args,**kwargs):
# function_param_indefinite_default('tan', 45, 56, 'hello', 7, k1='v1', k2='v2')

'''
参数的传递: 值传递和引用传递
值传递: 传参的时候 传递的是不可变的数据类型 如int/float/str/tuple/bool,当形参发生修改，对实参没有影响
引用传递：传参的时候，传递的是可变的数据类型，如：list/dict/set等，当形参中的元素发生修改，则实参会随着修改
'''

# 返回多个数 最终按照元组处理
# return_param = function_return_param()
# print(type(return_param), return_param)

# 空函数
# function_pass()

# 主函数 main() 类似于 Java 的 main() 函数
# Python 其实没有主函数的概念，但是，为了代码的可读性和可复用性
# 结合模块的使用，将函数的调用书写到if __name__== "__main__":中
# if __name__ == '__main__':
#     print("hello  main()...")

# 匿名函数
# 格式：lambda 形参列表:返回值
# lambda_return = lambda hello, world: hello + '---' + world
# print(lambda_return('hello', 'xixi'))
# 匿名函数本质是一个 function
# temp = []
# for i in range(10):
#     temp.append(lambda i: i * i)
# <class 'function'> 9
# print(type(temp[0]), temp[0](3))

# 闭包
# 函数只是一段可执行代码，编译后就“固化”了，每个函数在内存中只有一份实例
# 得到函数的入口点便可以执行函数了。函数还可以嵌套定义，即在一个函数内部可以定义另一个函数
# 有了嵌套函数这种结构，便会产生闭包问题
# def func1(): return 45
# def func2(num):
#     print(func1() + num)
# func2(5)

# def func1(num):
#     def func2(): return 35
#     return func2() + num
# print(func1(5))

# def func1():
#     def func2():
#         print('func2()')
#     func2()
# func1()

# 闭包的概念：如果两个函数嵌套定义，如果在内部函数中访问了外部函数中的变量，则会形成一个闭包
# def fun1(num1):
#     print(num1)
#     def func2(num2):
#         return num1 + num2
#     return func2
# fun_1 = fun1(1)
# print(type(fun_1), fun_1)
# print(fun_1(2))
# print(fun_1(3))

# def func1(num):
#     def func2():
#         print(num)
#     return func2
# func_1 = func1(10)
# func_1()
# func_1()

# def check_age(f):
#     print("外部函数~~~~~~~")
#     def inner(x):
#         print("内部函数~~~~~")
#         # 增加的新的功能：对年龄完成校验
#         if x < 0:
#             x = -x
#         # 调用原函数
#         f(x)
#     return inner
# @check_age  # 相当于调用外部函数，r = check_age(get_age)
# def get_age(age):
#     print(f"年龄：{age}")
# print(get_age)
# get_age(-34)  # 相当于调用内部函数，a = r(-34)

# def wrapper(func):
#     print('wrapper~~~~')
#     # args：元组  kwargs：字典
#     def inner(*args, **kwargs):  # 打包  （45,2）
#         func(*args, **kwargs)  # 原函数   拆包
#         print("new~~~~~~")
#     return inner
# @wrapper
# def f1():
#     print('11111')
# @wrapper
# def f2(a, b):  # a,b = 45,2
#     print('2222', a + b)
# @wrapper
# def f3(a, b, c, d):
#     print('3333', a, c, d)
# f1()
# f2(45, 2)
# f3(45, 6, 7, 8)
