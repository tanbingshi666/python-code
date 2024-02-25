### 练习

> ```Python
> # 在Python中表示空类型的是（NoneType）。   # NoneType类型：其中只有一个值None
>
> # 已知x = 3 == 3,执行结束后，变量x的值为（True）。
>
> # 表达式 9 ** 0.5的值为（3.0）
> print(9 ** 0.5)
>
> # 从控制台输入一个三位数，分别拆分出个位数，十位数和百位数，
> # 将拆分结果输出，格式为：百位：xx,十位：xx，个位：xx
> # 方式一：字符串   扩展
> # 字符串[索引]：可以获取指定位置的字符
> # num = input("请输入一个三位数：")  # 156
> # bw = num[0]
> # sw = num[1]
> # gw = num[2]
> # print(f"百位：{bw},十位：{sw}，个位：{gw}")
>
> # 方式二：算术运算符
> # num = int(input("请输入一个三位数："))   # 253
> # bw = num // 100
> # sw = num // 10 % 10    # num % 100 // 10
> # gw = num % 10
> # print(f"百位：{bw},十位：{sw}，个位：{gw}")
>
> # int(value,base):base是为了标记value的进制，当value为指定的进制，然后通过int转换为十进制
> print(int('110'))
> print(int('110',base=10))  # '110'中的110是十进制，经过int转换，转换为十进制
> print(int('110',10))
>
> print(int('110',base=2))  # '110'中的110是二进制，经过int转换，转换为十进制
> print(int('1111',base=2))
>
> print(int("0b1120",base=16))
> print(int("0b1110",base=2))
> ```

> Python 中语句的结构：顺序结构，分支结构【if语句】，循环结构【while语句和for语句】

### 一、分支语句【重点掌握】

#### 1.概念

> 在生活中，所谓的判断，指的是如果某些条件满足才能做某件事情；条件不满足时则不能做
>
> 在编程中，判断所给定的条件是否满足，根据判断的结果对应执行不同的语句，Python中的分支语句只有if语句
>

#### 2.使用

##### 2.1if单分支

> 语法：
>
> ```
> if 表达式：
> 	语句
> ```
>
> 说明：当程序执行到if语句时，首先判断“表达式”的值，如果表达式的值为“真”，则执行缩进的语句；如果表达式的值为“假”，则跳过整个if语句继续向下执行
>
> ```Python
> """
> if 条件：
> 	语句
> """
> """
> 注意：
>     1.if语句中条件可以是常量，变量或表达式
>       在Python中，表示假的数据：0  0.0  ""  False  None  []  ()  {} 等
>     2.在Python中，通过缩进区分代码块的，在编写程序的时候，要注意缩进的问题
>     3.if单分支的工作原理：如果条件成立，则执行代码块中的语句
>       如果条件不成立，则整个if语句会被跳过，继续执行后面的代码
>     4.总结：代码块要么执行，要么不执行
> """
> print('start~~~~~~')
> # 1.基本语法
> # a.常量
> if 0:
>     print('ok~~~1111')
>
> # b.变量
> # num = int(input("请输入一个数字："))
> # if num:
> #     print('ok~~~222')
>
> # c.表达式
> # if num == 10:
> #     print('ok~~~3333')
>
> print('end~~~~~~~')
>
> # 2.应用
> # a.需求：未成年人禁止进入网吧
> # age = int(input("请输入你的年龄："))
> # if age < 18:
> #     print("未成年人禁止进入网吧")
>
> # b.需求：从控制台输入一个数字，判断该数字是否是偶数
> num = int(input("请输入一个数字："))
> if  num % 2 == 0:    # 注意：区分=和==的使用
>     print(f"{num}是一个偶数")
> ```

##### 2.2if双分支

> 语法：
>
> ```
> if 表达式：
> 	语句1
> else：
> 	语句2
> ```
>
> 说明：当程序执行到if-else语句时，首先判断“表达式”的值，如果表达式的值为“真”，则执行语句1；如果表达式的值为“假”，则执行语句2
>
> ```Python
> """
> if 条件：
>     语句1
> else：
>     语句2
> """
>
> """
> 总结：
>     1.if-else中的条件和if单分支的使用完全相同
>     2.工作原理：根据条件是否成立，如果条件成立，则执行if分支，如果条件不成立，则执行else分支
>     3.总结：if-else实现二选一的操作
> """
> # 1.基本语法
> # num = int(input("请输入一个数字："))
> # if num > 10:
> #     print('yes')
> # else:
> #     print('no')
>
> # 2.应用
> # a.需求：未成年人禁止进入网吧
> # age = int(input("请输入你的年龄："))
> # if age < 18:
> #     print("未成年人禁止进入网吧")
> # else:
> #     print("欢迎光临，欢迎充值")
>
> # b.需求：从控制台输入一个数字，判断该数字是否是偶数
> # num = int(input("请输入一个数字："))
> # if  num % 2 == 0:
> #     print(f"{num}是一个偶数")
> # else:
> #     print(f"{num}是一个奇数")
>
> # 扩展：Python中获取随机数的方式
> """
> 方式一：
>     第一步：import  random
>     第二步：num = random.randint(start,end)，step只能是1，包头包尾【闭区间】
> 方式二
>     第一步：import  random
>     第二步：num = random.choice(range(start,end,step))，包头不包尾【前闭后开区间】
>     range(start,end,step):根据指定的数字区间，指定的步长产生一个容器
>         start:开始数字，可以省略，默认为0
>         end:结束数字，不可以省略，
>         step:步长，可以省略，默认为1    
>         
>     注意：如果end和step未被省略，则start也不能省略
> """
> # import  random
> # print(random.randint(10,100))   # 获取10~100之间的任意一个整数随机数
> # print(random.choice(range(10,101)))  # 获取10~100之间的任意一个整数随机数
> # print(random.choice(range(101)))  # 获取0~100之间的任意一个整数随机数
> # print(random.choice(range(1,101,2)))  # 获取1~100之间的任意一个奇数随机数
> # print(random.choice(range(0,101,2)))  # 获取0~100之间的任意一个偶数随机数
> # print(random.choice(range(100,0,-1))) # 获取100~1之间的任意一个整数随机数
>
> # c.需求:模拟彩票中奖操作：让程序随机产生一个数【0~100】，和用户输入的数进行比较，如果相等，则表示中奖
> import  random
> # 第一步：获取随机数
> # random_num = random.randint(0,100)  # 方式一
> random_num = random.choice(range(101))  # 方式二
> print(random_num)
> # 第二步：从控制台输入一个数
> input_num = int(input("请输入一个0~100之间的数："))
> if random_num == input_num:
>     print("恭喜你，中奖了")
> else:
>     print("谢谢参与")
> ```

##### 2.3if多分支

> 语法：
>
> ```python
> if 表达式1：
> 	语句1
> elif 表达式2：
> 	语句2
> elif 表达式3：
> 	语句3
> ….
> elif 表达式n：
> 	语句n
> else：
> 	语句m
>     
> else if  ---->elif
> ```
>
> 说明：当程序执行到if-elif语句时，首先计算表达式1的值，如果表达式1的值为真，那么执行语句1，执行完语句1则直接跳出整个if-elif语句，代码继续向下执行；
>
> ```Python
> """
> if 表达式1：
> 	语句1
> elif 表达式2：
> 	语句2
> elif 表达式3：
> 	语句3
> ….
> elif 表达式n：
> 	语句n
> else：
> 	语句m
> """
>
> """
> 总结：
>     1.如果需要操作的情况在3种及3种以上，则使用if多分支
>     2.if-elif....else语句实现的是多选一的操作
>     3.如果if和所有的elif后面的条件都不成立，则执行else中语句
>     4.不管多分支中有多少个条件成立，都只会执行其中的一个分支
> """
>
> # 1.基本语法
> # a
> week = input("请输入星期的数字：")
> if week == '1':
>     print("Mon")
> elif week == '2':
>     print("Tues")
> elif week == '3':
>     print("Wed")
> elif week == '4':
>     print("Thur")
> elif week == '5':
>     print("Fri")
> elif week == '6':
>     print("Sat")
> elif week == '7':
>     print("Sun")
> else:
>     print("没有该星期")
>
> # b
> n = 3
> if n > 0:
>     print('a')
> elif n > 1:
>     print('b')
> elif n > 2:
>     print('c')
> elif n > 3:
>     print('d')
> else:
>     print('e')
>
> # 2.应用
> # 需求：从控制台输入两个数，比较两个数的大小，如果大于，则输出1，如果小于，则输出-1，如果相等，则输出0
> num1 = int(input("first number:"))
> num2 = int(input("second number:"))
> if num1 > num2:
>     print(1)
> elif num1 < num2:
>     print(-1)
> else:
>     print(0)
> ```

##### 2.4三者的区别

> ```Python
> """
> 【面试题】if语句中的单分支，双分支和多分支的区别
> 单分支：只能处理一种情况，特点：要么执行，要么不执行
> 双分支：处理两种情况，特点：实现的是二选一的操作
> 多分支：处理3种及3种以上的情况，特点：实现的是多选一的操作
> """
> # 多分支
> n = 3
> if n > 0:
>     print('a')
> elif n > 1:
>     print('b')
> elif n > 2:
>     print('c')
> elif n > 3:
>     print('d')
> else:
>     print('e')
> # a
>
> # 单分支
> if n > 0:
>     print('a')
> if n > 1:
>     print('b')
> # a  b
>
> # 双分支
> if n > 2:
>     print('c')
> else:
>     print('e')
> # c
> ```

##### 2.5嵌套if语句

> ```Python
> # 单分支，双分支和多分支两两之间可以相互嵌套
>
> # 注意1：在嵌套的if语句中，注意缩进问题
> # 注意2：理论上来说，嵌套的层数没有限制，但是为了代码的可读性，建议嵌套的层数不要超过4层
>
> # 1.基本语法
> a = 10
> b = 20
> if a > 5:
>     print("ok~~~~11111")
>     if b == 20:
>         print("ok~~~2222")
>     else:
>         print("no~~~2222")
> else:
>     print('no~~~1111')
>
> # 2.应用
> # 需求：有人加你好友，如果是女生，且年龄小于18，且漂亮，则欣然同意，否则残忍拒绝
> gender = input("请输入你的性别：")  # male   female
> age = int(input("请输入你的年龄："))
> face_value = int(input("请输入颜值:"))  # 颜值为8分以上为漂亮
> # 方式一
> if gender == 'female':
>     if age < 18:
>         if face_value >= 8:
>             print("欣然同意")
>         else:
>             print("残忍拒绝")
>     else:
>         print("残忍拒绝")
> else:
>     print("残忍拒绝")
>
> # 方式二
> if gender == 'female' and age < 18 and face_value >= 8:
>     print("欣然同意")
> else:
>     print("残忍拒绝")
> ```