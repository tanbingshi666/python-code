### 练习

> ```Python
> # 计算1到100以内能被7或者3整除但不能同时被这两者整除的数的个数
> n = 1
> count = 0
> while n <= 100:
>     # if (n % 7 == 0 or n % 3 == 0) and not(n % 7 == 0 and n % 3 == 0):
>     if (n % 7 == 0 or n % 3 == 0) and n % 21 != 0:
>         count += 1
>     n += 1
> print(count)
>
> count = 0
> for n in range(1,101):
>     if (n % 7 == 0 or n % 3 == 0) and n % 21 != 0:
>         count += 1
> print(count)
>
> # 输入任意一个正整数，求他是几位数？注意: 不能使用字符串，只能用循环
> """
> 思路：判断一个正整数是几位数，只需要查看该正整数整除几次10结果为0
> 例如：
>     234 // 10--->23   23 // 10 ---->2    2 // 10 ----->0
> """
> num1 = input("请输入一个正整数：")
> if num1.isdigit():  # 非负数
>     num = int(num1)
>     if num == 0:
>         print('0不是正整数')
>     else:
>         count = 1
>         while num // 10 != 0:
>             count += 1
>             num //= 10
>         print(f"{num1}是一个{count}位数")
> else:
>     print("输入有误，不是正整数")
> ```

### 一、循环【重点掌握】

#### 1.嵌套循环

> 类似于嵌套if语句
>
> 语法：
>
> ```
> while 表达式1：
> 	while 表达式2：
> 		语句
> ```

> ```Python
> # 1.
> # 循环5次，打印0~4
> m = 0
> while m < 5:
>     print(m)
>     m += 1
> # 循环3次，打印0~2
> n = 0
> while n < 3:
>     print(n)
>     n += 1
>
> print("*" * 50)
>
> # 2.
> # a.
> # 外层循环
> m = 0
> while m < 5:
>     # 内层循环
>     n = 0
>     while n < 3:
>         print(f"{m}={n}")
>         n += 1
>     m += 1
> # 外层循环：5次，内层循环：3次，总共打印15条
>
> print("*" * 50)
>
> # b
> m = 0
> n = 0
> while m < 5:
>     while n < 3:
>         print(f"{m}={n}")
>         n += 1
>     m += 1
>
> # 注意：在代码执行的过程中，不管循环语句是否嵌套，都是将循环执行完毕，后面的才有执行的机会
>
> print("*" * 50)
>
> # 3.应用：打印九九乘法表
> """
>                                                 行       列
> 1*1=1                                           1        1
> 1*2=2 2*2=4                                     2        2
> 1*3=3 2*3=6 3*3=9                               3         3
> ......
>
> 1*9=9 2*9=18 3*9=27 4*9=36 .....   9*9=81       9           9
>
> 规律：
>     a.列*行=乘积
>     b.行的取值范围：1~9
>     c.列的取值范围：1~ 当前行数
>     d.使用嵌套循环，外层循环控制的是行， 内层循环控制的是列
> """
> # 外层循环：控制的是行
> row = 1
> while row <= 9:
>     # 内层循环:控制的是列
>     col = 1
>     while col <= row:
>         print(f"{col}*{row}={col * row}",end=" ")
>         col += 1
>     row += 1
>     print()   # 换行
>
> for row in range(1,10):
>     for col in range(1,row + 1):
>         print(f"{col}*{row}={col * row}", end=" ")
>     print()
> ```

#### 2.break和continue

> ```Python
> """
> 【面试题】
> break:打断，表示结束当前循环【break书写在哪个循环中，就结束哪个循环，就近原则】
> continue:继续，表示结束当前循环的本次循环，继续下一次循环
> """
>
> # 1.break     *******
> # a.
> m = 0
> while m < 10:
>     print(m)
>     m += 1
> # 0-9
>
> print("*" * 30)
>
> # b
> # 注意1：break是一个关键字，但是可以单独作为一条语句使用
> # 注意2：如果break应用在单层循环【while和for】中，在满足条件的情况下，表示结束循环
> m = 0
> while m < 10:
>     print(m)
>     if m == 3:
>         break
>     m += 1
>
> print("*" * 30)
>
> # c.
> # 注意3：break应用在循环中，结束的是当前循环【就近原则】
> m = 0
> while m < 5:
>     n = 0
>     while n < 3:
>         if m == 2:
>             break
>         print(f"{m}={n}")
>         n += 1
>     m += 1
> # 唯独没有2=0 2=1 2=2
>
> print("*" * 30)
>
> m = 0
> while m < 5:
>     n = 0
>     while n < 3:
>         print(f"{m}={n}")
>         if n == 1:
>             break
>         n += 1
>     m += 1
>
> print("*" * 30)
>
> # 2.continue
> # m = 0
> # while m < 10:
> #     if m == 3:
> #         # break
> #         continue
> #     print(m)
> #     m += 1
>
> m = 0
> while m < 10:
>     if m == 3:
>         m += 1
>         continue
>     print(m)
>     m += 1
>
> # 练习：验证用户的用户名和密码，当用户名为root,密码为abc的时候，表示验证成功，
> # 否则验证失败，失败时允许重复输入三次
> error_num = 0
> while True:
>     username = input("请输入用户名：")
>     password = input("请输入密码：")
>     if username == 'root' and password == 'abc':
>         print("登录成功！")
>         break
>     else:
>         print('登录失败，用户名或密码错误，请重新输入')
>         error_num += 1
>         # 当error_num == 3则结束循环，否则循环继续
>         if error_num == 3:
>             print("已经错误三次，禁止登录！")
>             break
>         else:
>             continue
> ```

#### 3.else分支

> ```Python
> """
> 语法：
> while  xxx:
>     xxx
> else:
>     xxx
>
> for 变量 in 容器：
>     xxx
> else:
>     xxx
>
> for 变量 in 容器：
>     if xxx:
>         xxx
>     else：
>         xxx
> else:
>     xxx
> """
>
> # 1.注意1：当循环中没有break语句时，循环执行完毕之后，else代码块最后都会被执行，不常用
> m = 0
> while m < 5:
>     print(m)
>     m += 1
> else:
>     print('else被执行了')
>
> for n in range(5):
>     print(n)
> else:
>     print("else被执行~~~~")
>
> print("*" * 50)
>
> # 2.注意2：当循环中有break语句且break语句被执行了，则else不会执行   常用
> # 如果break执行，则else不执行，如果break不执行，else会执行
> m = 0
> while m < 5:
>     print(m)
>     if m > 10:
>         break
>     m += 1
> else:
>     print('else被执行了')
>
> for n in range(5):
>     print(n)
>     if n > 10:
>         break
> else:
>     print("else被执行~~~~")
>
> # pass：占位语句，没有实际含义，只是为了保证代码结构的完整性，在实际操作中，用于暂时性的占位
>
> # 练习：从控制台输入一个数字，判断该数是否是质数
> # 质数【素数】：只能被1或它本身整除的数，最小的质数是2
> num = input("请输入一个数字：")
> if num.isdigit():  # 非负数
>     num = int(num)
>     if num < 2:
>         print(f"{num}不是质数")
>     else:
>         # 思路：判断10是否是质数，只需要在2~9之间找到一个数，能整除10，则说明10不是质数
>         for n in range(2,num):
>             if num % n == 0:
>                 print(f"{num}不是质数")
>                 break    # 如果得到结论，可以提前结束循环
>         else:
>             print(f"{num}是质数")
> else:
>     print("输入有误")
> ```

#### 4.死循环

> ```Python
> # 1.语法
> """
> while  1:
>     pass
>
> while  True:
>     pass
>
> 注意：死循环大多数结合break使用
> """
>
> # 2.练习：猜数字游戏
> """
> a.从控制台输入一个数，和程序产生的随机数进行比较，范围为1~100
> b.根据比较的结果
>     输入的数  >  随机数，提示：你猜大了，往小了猜
>     输入的数  <  随机数，提示：你猜小了，往大了猜
>     输入的数  ==  随机数，提示：恭喜你，猜中了
> """
> import  random
> random_num = random.randint(1,100)
> while True:
>     input_num = int(input("请输入1~100之间的整数："))
>     if input_num > random_num:
>         print("你猜大了，往小了猜")
>     elif input_num < random_num:
>         print("你猜小了，往大了猜")
>     else:
>         print("恭喜你，猜中了")
>         # 猜中表示游戏结束，则结束死循环
>         break
> ```

