### 一、文件读写【重点掌握】

> 常见文件的读写分类：
>
> ​	1.普通文本文件：txt   py   md   html    doc等
>
> ​	2.csv文件：.csv，需要借助于系统模块csv
>
> ​	3.二进制文件：图片，音频，视频，压缩包等
>
> ​	4.对象的序列化和反序列化：pickle和json
>
> ​	5.excel文件：需要借助于第三方模块

#### 1.普通文件读写

##### 1.1写入

> ```Python
> # 1.打开文件：open()
> """
> open(file,mode,encoding)
>     file:需要打开的文件名称或文件的路径
>         文件名称：需要打开的文件和当前py文件在同一个目录下，不常用
>         文件路径：需要打开的文件和当前py文件不在同一个目录下，可以使用相对路径或绝对路径
>             相对路径：相对当前工程的路径,如：aaa/file1.txt,推荐
>             绝对路径：从系统盘符开始的路径，如：c:/users/xxxx/Desktop/Coding5/Day21Code/aaa/file1.txt
>     mode:打开文件的模式
>         'r'       open for reading (default)，普通文件的读取
>         'w'       open for writing, truncating the file first，普通文件的写入【删除原文件，生成一个新的文件】
>         'a'       open for writing, appending to the end of the file if it exists，普通文件的写入【追加】
>         'rb'      打开二进制文件用于读取
>         'wb'      打开二进制文件用于写入
>     encoding：文件的编码格式
>         常用的编码格式：utf-8/gbk
>
> 注意：
>     a.打开文件的时候，encoding的设置一定要和文件本身的编码格式保持一致，否则写入会出现乱码的情况，读取直接报错UnicodeDecodeError
>     b.如果要写入内容，mode可以使用w或a,w:覆盖，a:追加
>     c.写入内容的时候，文件的路径建议使用相对路径
> """
> # a.用w打开文件，文件已经存在,可以直接打开
> # f1 = open('aaa/file1.txt','w',encoding='utf-8')
> # b.用w打开文件，文件不存在,创建文件
> # f2 = open('aaa/file2.txt','w',encoding='gbk')
> f3 = open('aaa/file1.txt','a',encoding='utf-8')
>
> # 2.写入内容
> # a.直接写入 :write()      ******
> # f1.write("计算机abcd")
> # f2.write("你好hello")
> # f3.write("轻轻地我走了~~~")
> # 表示刷新，当需要写入的内容较多的时候，可以提高写入的效率
> # f3.flush()
>
> # b.写入多行,使用\n表示换行
> f3.writelines('aaaa\n你好\n34678ghjwg')
> f3.flush()
>
> # 3.关闭文件:close()
> f3.close()
> ```

##### 1.2读取

> ```Python
> # 1.打开文件：open()
> # 注意：打开文件用于读取，则文件必须存在，否则报错FileNotFoundError
> # f = open('aaa/file2.txt','r',encoding='gbk')
> f = open('aaa/致橡树.txt','r',encoding='gbk')
>
> # 2.读取内容
> # a.read()：默认全部读取，结果是一个字符串          *****
> # 注意：适用于读取内容较少的文件，如果内容较多，则可以选择循环读取
> # r = f.read()
> # print(r)
>
> # b.readline():一次只能读取一行
> # r = f.readline()
> # print(r)
>
> # c.readlines()：默认全部读取，返回一个列表,其中的元素是每一行内容           ******
> r = f.readlines()
> print(r)
>
> # 3.关闭文件：close()
> f.close()
>
> """
> 不管读取还是写入，最后操作完毕之后建议关闭文件
> 原因：通过open打开一个文件,实际上是在内存中打开了一个文件的对象，
>     会占用一定的内存空间，最后操作完毕之后如果不关闭，则浪费内存空间
> """
> ```

##### 1.3循环操作【了解】

> ```Python
> import  os,math
>
> # 1.read(size):适用于文件内容量非常大的情况下，使用循环可以提高读取效率
> # 方式一
> """
> path = r"致橡树.txt"
> f = open(path,'r',encoding='gbk')
> # 获取文件的总字节数
> total_size = os.path.getsize(path)
> # 设定一次读取的字节数
> sub_size = 1024  # 建议设置为2的次方
> while total_size > 0:
>     r = f.read(sub_size)
>     print(r)
>     total_size -= sub_size
> f.close()
> """
>
> # 方式二
> path = r"致橡树.txt"
> f = open(path,'r',encoding='gbk')
> # 获取文件的总字节数
> total_size = os.path.getsize(path)
> # 设定一次读取的字节数
> sub_size = 1024
> n = 0
> while  n <= math.ceil(total_size / sub_size):
>     r = f.read(sub_size)
>     print(r)
>     n += 1
> f.close()
>
>
> # 2.readline():了解工作原理，在实际中很少用
> path = r"致橡树.txt"
> f = open(path,'r',encoding='gbk')
> r = f.readline()
> print(r)
> while r:
>     r = f.readline()
>     print(r)
> f.close()
> ```

##### 1.4with上下文

> ```Python
> """
> 语法：
> with open()  as  变量:
>     读取/写入
>
> 说明：
>     a.with上下文其实是简化了文件读写的三步曲
>     b.使用with的方式之后，读取和写入文件之后，无需手动关闭文件，当with代码块执行完毕，对应的文件会自动关闭
>     c.变量表示文件描述符,也就是文件对象
>     d.当通过with的方式打开文件，则文件读取和写入的操作一定要在with代码块中完成，
>       否则文件会被关闭掉，无法操作【ValueError: I/O operation on closed file.】
> """
> # 1.读取
> with open('aaa/致橡树.txt','r',encoding='gbk') as f:
>     r = f.read()
>     print(r)
>
> # 2.写入
> with  open('aaa/file1.txt','a',encoding='utf-8') as f1:
>     f1.write("ghajgh")
>     f1.flush()
> ```

#### 2.二进制文件读写

> ```Python
> """
> 注意：
>     a.读取和写入分别使用'rb'和'wb'
>         'rb'      打开二进制文件用于读取
>         'wb'      打开二进制文件用于写入
>     b.因为二进制文件是由二进制【字节】组成，没有编码一说，所以需要省略encoding参数
> """
>
> # 1.读取
> with open("aaa/logo.png",'rb') as f1:
>     r = f1.read()
>     print(r)
>
> # 2.写入
> with open('aaa/img1.png','wb') as f2:
>     f2.write(r)
>     f2.flush()
> ```

#### 3.CSV文件读写

> CSV（Comma Separated Values逗号分隔值）
>
> .csv是一种文件格式（如.txt、.doc等），也可理解.csv文件就是一种特殊格式的纯文本文件。即是一组字符序列，字符之间用英文字符的逗号或制表符（Tab）分隔
>
> 所以，CSV文件本身就是是个纯文本文件，这种文件格式经常用来作为不同程序之间的数据交互的格式
>
> 在windows系统环境上.csv文件打开方式有多种，如记事本、excel、Notepad++等，只要是文本编辑器都能正确打开

##### 3.1读取

> ```Python
> import  csv
>
> # 一、读取
> # 1.打开
> f1 = open('aaa/t1.csv','r',encoding="utf-8")
> # 2.读取
> """
> csv.reader(iterable)  ----->iterator
> """
> reader = csv.reader(f1)   # 相当于f1.read()
> print(list(reader))
> # for row in reader:
> #     print(row)
>
> # 3.关闭文件
> f1.close()
> ```

##### 3.2写入

> ```Python
> # 二、写入
> # 1.打开文件
> f2 = open('aaa/t3.csv','w',encoding='utf-8')
>
> # 2.写入内容
> writer = csv.writer(f2)     # 相当于f2.write()
> data = [['uname', 'pwd', 'age', 'address'], ['zhangsan', 'aaa', '10', 'shanghai'], ['lisi', 'bbb', '20', '北京'], ['王五', 'ccc', '12', '深圳']]
> # a.单行写入：writerow()
> # for row in data:
> #     writer.writerow(row)
>
> # b.多行写入:writerows()
> writer.writerows(data)
>
> # 3.关闭文件
> f1.close()
> ```

#### 4.对象的序列化和反序列化

> Python中一切皆对象

> 对象的序列化：将Python中的对象持久化到磁盘上
>
> 对象的反序列化：将磁盘上一个文件中的内容转换为Python对象
>
> 注意：
>
> ​	1.对象的序列化【写入】和反序列化【读取】通过pickle模块和json模块完成
> ​	2.Python中一切皆对象，可以使用pickle或json模块的类型：数字，字符串，列表，字典。元组，集合，类，函数，模块等

##### 4.1pickle模块

> ```Python
> import pickle
>
> class Person():
>     def __init__(self,name,age):
>         self.name = name
>         self.age = age
>     def show(self):
>         print(f"姓名：{self.name}，年龄:{self.age}")
> per = Person("张三",10)
>
> # with open('file3.txt','w',encoding='utf-8') as f:
> #     f.write(10)  # TypeError: write() argument must be str, not int
>
> # 1.序列化【写入】
> """
> pickle.dump(obj,file)
>     obj:需要序列化的对象
>     file:需要序列化到的文件对象，注意：必须以位二进制的方式打开文件，wb
> """
> with open('aaa/per.txt','wb') as f1:
>     pickle.dump(per,f1)
>
> # 2.反序列化【读取】
> """
> pickle.load(file)
>     file:需要反序列化到的文件对象，注意：必须以位二进制的方式打开文件，rb
> """
> with open('aaa/per.txt','rb') as f2:
>     r = pickle.load(f2)
>     print(r)
>     r.show()
> ```

##### 4.2json模块

> JSON:JavaScript  Object Notation,是一种轻量级的用于创建js的方式，因为json易于阅读和编写，所以经常用于数据的交换
>
> 好处：
>
> ​	a.可以在不同的操作系统之间进行数据交换
>
> ​	b.可以在不同的程序之间进行数据交换
>
> ​	c.可以在不同的编程语言之间进行数据交换
>
> JSON和Python中的数据类型对比
>
> |    Python类型     |       JSON类型       | 说明    |
> | :-------------: | :----------------: | ----- |
> |      dict       |       object       | 字典/对象 |
> |      list       |       array        | 列表/数组 |
> |       str       |       string       | 字符串   |
> |    int/float    |       number       | 数字    |
> | bool:True/False | boolean:true/false | 布尔值   |
> |      None       |        null        | 空值    |

> ```Python
> {
>     "name": "中国",
>     "province": [{
>         "name": "黑龙江",
>         "cities": {
>             "city": ["哈尔滨", "大庆"]
>         }
>     }, {
>         "name": "广东",
>         "cities": {
>             "city": ["广州", "深圳", "珠海"]
>         }
>     }, {
>         "name": "台湾",
>         "cities": {
>             "city": ["台北", "高雄"]
>         }
>     }, {
>         "name": "新疆",
>         "cities": {
>             "city": ["乌鲁木齐"]
>         }
>     }]
> }
> ```

> 使用json进行对象的序列化和反序列化，主要是将Python对象和json字符串进行相互的转化
>
> json.dump():将Python中的字典或列表对象序列化到指定的文件中
> json.dumps()：将Python中的字典或列表对象序列化为json字符串
>
> json.load():将指定的文件中的json字符串反序列化为Python中的字典或列表对象
> json.loads()：将json字符串反序列化为Python中的字典或列表对象
>
> ```Python
> import  json
>
> info_dict = {
>     "name": "中国",
>     "province": [{
>         "name": "黑龙江",
>         "cities": {
>             "city": ["哈尔滨", "大庆"]
>         }
>     }, {
>         "name": "广东",
>         "cities": {
>             "city": ["广州", "深圳", "珠海"]
>         }
>     }, {
>         "name": "台湾",
>         "cities": {
>             "city": ["台北", "高雄"]
>         }
>     }, {
>         "name": "新疆",
>         "cities": {
>             "city": ["乌鲁木齐"]
>         }
>     }]
> }
> print(info_dict)
> print(type(info_dict))
>
> # 1.序列化：Serialize
> """
> json.dump(obj,file):将Python中的字典或列表对象序列化到指定的文件中
>     obj:需要序列化的Python对象
>     file:需要序列化到的文件对象
> json.dumps(obj)：将Python中的字典或列表对象序列化为json字符串
> """
> # a.
> # 注意1：通过dumps将Python中的对象转换为JSON格式化字符串
> # 注意2：ensure_ascii默认为True，表示中文默认会被编码，但是如果需要中文正常显示，则设置ensure_ascii=False
> r1 = json.dumps(info_dict,ensure_ascii=False)
> print(r1)
> print(type(r1))  # json字符串
>
> # b.
> with open('country.json','w',encoding='utf-8') as f:
>     json.dump(info_dict,f,ensure_ascii=False)
>
> # 2.反序列化:Deserialize
> """
> json.load():将指定的文件中的json字符串反序列化为Python中的字典或列表对象
> json.loads()：将json字符串反序列化为Python中的字典或列表对象
> """
> # a.
> r2 = json.loads(r1)
> print(r2)
> print(type(r2))
>
> # b
> with open("country.json",'r',encoding='utf-8') as f:
>     r3 = json.load(f)
>     print(r3)
>     print(type(r3))
> ```
