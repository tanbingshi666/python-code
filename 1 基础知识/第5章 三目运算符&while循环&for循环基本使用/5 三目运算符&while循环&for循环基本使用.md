### 练习

> ```Python
> # 1 从控制台输入一个年份，判断该年是否是闰年，
> # 是闰年的条件: 能被4整除但是不能被100整除  或者  能够被400整除的年
> # year = int(input("请输入一个年份："))
> # if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0:
> #     print(f"{year}是闰年")
> # else:
> #     print(f"{year}是平年")
>
> # 2 从控制台输入三个数，输出较大的值
> # 方式一
> # num1 = int(input("first:"))
> # num2 = int(input("second:"))
> # num3 = int(input("third:"))
>
> # 方式二
> # 扩展：eval(字符串)，可以识别字符串中有效的Python表达式
> # r = eval(input("请输入3个数，用逗号分隔："))
> # print(r)   # 三个数字用逗号隔开，r是一个元组
> # num1,num2,num3 = r      # 对元组进行拆包
> # print(num1,num3)
> # num1,num2,num3 = eval(input("请输入3个数，用逗号分隔："))
> # print(type(num1))
> # 假设法：定义一个新的变量max_value,其中存储最大值，假设num1为最大值
> # 在比较的过程中，验证+推翻假设
> # max_value = num1
> # if num2 > num1:
> #     max_value = num2
> # if num3 > max_value:
> #     max_value = num3
> # print(f"num1,num2和num3的最大值为{max_value}")
>
> # 3 从控制台输入一个三位数，如果是水仙花数就打印“是水仙花数”，否则打印“不是水仙花数”，
> # 例如：153 = 1的三次方 + 5的三次方 + 3的三次方，则153是水仙花数
> # 方式一
> # num = input("请输入一个三位数：")
> # bw = int(num[0])
> # sw = int(num[1])
> # gw = int(num[2])
> # total = bw ** 3 + sw ** 3 + gw ** 3
> # if int(num) == total:
> #     print(f"{num}是一个水仙花数")
> # else:
> #     print(f"{num}不是一个水仙花数")
>
> # 方式二：算术运算符
> # num = int(input("请输入一个三位数："))   # 253
> # bw = num // 100
> # sw = num // 10 % 10    # num % 100 // 10
> # gw = num % 10
> # total = bw ** 3 + sw ** 3 + gw ** 3
> # if num == total:
> #     print(f"{num}是一个水仙花数")
> # else:
> #     print(f"{num}不是一个水仙花数")
>
> # 扩展：
> num = input("请输入一个三位数：")
> # 字符串.isdigit():判断字符串是否非空且全部由数字组成，如果是全数字，则结果为True
> if num.isdigit():
>     # len(字符串)：获取字符串的长度
>     if len(num) == 3:
>         num = int(num)
>         bw = num // 100
>         sw = num // 10 % 10  # num % 100 // 10
>         gw = num % 10
>         total = bw ** 3 + sw ** 3 + gw ** 3
>         if num == total:
>             print(f"{num}是一个水仙花数")
>         else:
>             print(f"{num}不是一个水仙花数")
>     else:
>         print("不是一个3位数")
> else:
>     print("输入有误")s
> ```

### 一、if语句

#### 1.三目运算符

> Python中本身没有三目运算符，我们可以通过if-else模拟三目运算符
> 三目运算符的特点：实现二选一的操作，可以简化if-else语句
> 注意：三目运算符只有一行代码，所以只能实现简单的逻辑
>
> ```Python
> # 作用：实现二选一
> # 语法：r = 值1 if 条件 else 值2
> # 工作原理：如果条件成立，则整个表达式的值为 值1，如果条件不成立，则整个表达式的值为  值2
> # 优点：简化if-else语句
> # 缺点：因为只有一行代码，所以只能实现简单的逻辑
>
> # 1
> num = int(input("请输入一个数字："))
> if num % 2 == 0:
>     print(f"{num}是偶数")
> else:
>     print(f"{num}是奇数")
>
> r1 = '偶数' if num % 2 == 0 else "奇数"
> print(r1)
> r1 = True if num % 2 == 0 else False
> print(r1)
>
> # 2.
> year = int(input("请输入一个年份："))
> if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0:
>     print(f"{year}是闰年")
> else:
>     print(f"{year}是平年")
>
> r2 = '闰年' if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0 else "平年"
> print(r2)
> r2 = True if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0 else False
> print(r2)
> r2 = 1 if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0 else 0
> print(r2)
> ```

### 二、循环语句【重点掌握】

#### 1.概念

> 在生活中，循环指的是一个现象周期性或者重复性的出现
>
> 在编程中，在满足条件的情况下，反复执行某一段代码，在编程语言中出现的这种现象被称为循环，这段被重复执行的代码被称为循环体
>
> Python中提供的循环语句有：while语句和for语句

#### 2.while基本语法

> 语法：
>
> ```
> while 表达式：
> 	语句
> ```
>
> 说明：当程序在从上往下执行的过程中，遇到while语句时，首先计算表达式的值，如果表达式的值为假，则跳过整个while语句，程序继续向下执行；如果表达式的值为真，则执行对应的语句；执行完语句，再去计算表达式的值，如果表达式的值为假，则跳过整个while语句，程序继续向下执行；如果表达式的值为真，则执行对应的语句。。。如此循环往复，直到表达式的值为假，整个循环才停止
>
> ```Python
> # 1.
> """
> if 条件：
> 	语句
>
> while 条件：
> 	语句
>
> 注意：
>     1.while语句和if语句的条件相似，都可以使用常量，变量或表达式充当
>     2.虽然while语句和if单分支的语法相似，但是在条件成立的情况下，if语句只会执行一次，while可能会执行多次
>     3.书写循环语句需要考虑的核心问题：控制循环的次数，让循环在适当的时机可以停止下来，否则会行程死循环
> """
> # if 1:
> #     print("ok~~111")
> # while 1:
> #     print("ok~~~222")
>
> # 2.while的常用语法
> # 需求：打印10遍hello world
> # print('hello world')
> # print('hello world')
> # print('hello world')
> # print('hello world')
> # print('hello world')
> # print('hello world')
> # print('hello world')
> # print('hello world')
>
> # 解决方案：循环体只需要书写一次，但是可以执行多次
> print("start~~~~")
>
> # a.初始化表达式,注意：需求中没有明确要求的情况下，n的初始值可以任意书写，
> # 但是为了方便计算，如果需求中没有要求，一般从0开始
> n = 0
> # b.条件表达式
> while n < 10:
>     # c.循环体
>     print('hello world')
>     # d.循环之后的操作表达式
>     n += 1
>
> print("over~~~~~")
>
> n = 9
> while n >= 0:
>     print('hello world')
>     n -= 1
> ```

#### 3.for基本语法

> 语法：	
>
> ```
> for 变量名 in 序列：
> 	语句
> ```
>
> 功能：for循环主要用于遍历任何序列【容器】，比如列表，字符串，元组，字典和集合等
>
> 遍历：指的是依次访问序列中的每一个元素，获取每个元素值
>
> 说明：按照顺序获取序列中的每个元素，赋值给变量名，再执行循环体，如此循环往复，直到取完序列中所有的元素为止
>
> ```Python
> """
> while 条件:循环的次数由条件控制
> for 变量 in  容器:循环的次数由容器中数据的个数决定
> """
> # 1.基本使用
> """
> 注意：
>     a.变量根据需求自定义，只要是一个合法标识符即可
>     b.
> """
> # a.字符串
> for ch in 'abcd':
>     print(ch)
> """
> 工作原理：将字符a取出，赋值给ch，然后打印，接着将字符b取出，赋值给ch,打印。。。。。
>         当字符串中所有的字符全部被取出，则循环结束 
> """
> # b.列表
> for num  in [3,4,5,6,10]:
>     print(num)
> """
> 工作原理：将数字3取出，赋值给num，然后打印，接着将数字4取出，赋值给num,打印。。。。。
>         当列表中所有的数字全部被取出，则循环结束 
> """
>
> # 2.range(start,end,step):根据指定的数字区间，指定步长生成一个容器
> # print(list(range(10)))
> # print(list(range(1,10)))
> # print(list(range(0,10,2)))
> # print(list(range(1,10,2)))
> # 需求：打印10遍hello world
> # for ch in 'hgajgha345':
> #     print("hello world")
> # 注意：如果for循环仅仅是为了控制循环的次数，则变量书写为_
> for _ in range(10):
>     print("hello world")
>
> for i in range(10):
>     print(i)
> for i in range(1,10):
>     print(i)
> for i in range(1,10,2):
>     print(i)
> for i in range(0,10,2):
>     print(i)
>
> """
> 总结：
>     a.在实际项目开发中，常用for
>     b.如果确定循环的次数，则使用for【列表，元组，字符串，range()等】
>     c.如果不确定循环的次数，则使用while【死循环】
> """
> ```

#### 4.while和for基本使用练习

> ```Python
> # 1.打印0~9的数字
> # 2.求1~100之间所有整数的和
> # 3.统计1~100之间3的倍数的个数
> ```

> ```Python
> # 1.打印0~9的数字
> n = 0
> while n <= 9:  # n < 10
>     print(n)
>     n += 1
> for n in range(10):
>     print(n)
>
> # 2.求1~100之间所有整数的和
> n = 1
> total = 0   # 记录和
> while n <= 100:
>     total += n
>     n += 1   # 步长
> print(total)
>
> total = 0
> for n in range(1,101):
>     total += n
> print(total)
>
> # 3.统计1~100之间3的倍数的个数
> # 方式一
> n = 3
> count = 0
> while n <= 100:
>     count += 1
>     n += 3
> print(count)
>
> count = 0
> for n in range(3,101,3):
>     count += 1
> print(count)
>
> # 方式二
> n = 1
> count = 0
> while n <= 100:
>     if n % 3 == 0:
>         count += 1
>     n += 1
> print(count)
>
> count = 0
> for n in range(1,101):
>     if n % 3 == 0:
>         count += 1
> print(count)
>
> # 4.找出2000~2020年之间的所有的闰年
> year = 2000
> while year <= 2020:
>     if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0:
>         print(f"{year}是闰年")
>     year += 1
>
> for year in range(2000,2021):
>     if (year % 4 == 0 and year % 100 != 0)  or  year % 400 == 0:
>         print(f"{year}是闰年")
> ```

