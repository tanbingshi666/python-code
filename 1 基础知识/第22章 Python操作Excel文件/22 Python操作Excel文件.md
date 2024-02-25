### 练习

> ```Python
> """
> 开房查询，从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，
> 如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中
> """
> # 一、封装函数
> # 1.读取文件内容
> def read_data():
>     with open("kaifanglist.txt",'r',encoding="utf-8") as f:
>         all_list = f.readlines()
>     return all_list
>
> # 2.查询指定姓名的人的信息
> def search_data(name):
>     # 获取所有人的信息
>     all_list = read_data()
>     # 存储查询到的指定的人的信息
>     single_list = []
>     for info in all_list:
>        if info.split(',')[0] == name:
>            single_list.append(info)
>     return single_list
>
> # 将查询到的结果写入到指定文件
> def write_data():
>     name = input("请输入你要查询的人的姓名：")
>     # 获取查找到的信息
>     single_list = search_data(name)
>     if single_list:
>         # 有结果
>         print(f"{name}果然去开房了。。。")
>
>         # 写入
>         des_path = name + '.txt'
>         with open(des_path,'w',encoding='utf-8') as f:
>             for info in single_list:
>                 f.write(info)
>                 f.flush()
>         print("数据写入成功！")
>     else:
>         print(f"{name}是个好人，请好好珍惜。。。")
>
> # 调用函数
> if __name__ == '__main__':
>     write_data()
>
> # 也可以使用csv进行读写
> ```

### 一、Excel 简介

> ​	Excel是Microsoft(微软)为使用Windows和macOS操作系统开发的一款电子表格软件。Excel凭借其直观的界面、出色的计算功能和图表工具，再加上成功的市场营销，一直以来都是最为流行的个人计算机数据处理软件。当然，Excel也有很多竞品，例如Google Sheets、LibreOffice Calc、Numbers等，这些竞品基本上也能够兼容Excel，至少能够读写较新版本的Excel文文件
>
> ​	 掌握用Python程序操作Excel文件，可以让日常办公自动化的工 作更加轻松愉快，而且在很多商业项目中，导入导出Excel文文件都是特别常⻅的功能
>
> Excel 的组成：工作簿----》工作表------》单元格

### 二、常用库简介

#### 1.常用库

> Python中的模块分为三大类：
>
> ​	a.系统模块：直接import  xxx
>
> ​	b.自定义模块:自定义py文件
>
> ​	c.第三方模块,必须先安装，然后再使用

> 操作excel的第三方模块：
>
> 1. pandas：是进行数据处理和数据分析的模块，可以用来处理excel
>
> 2. xlrd,xlwt:可以进行基本的excel的操作，xlrd负责读取，xlwt负责写入，针对的是.xls
>
> 3. xlwings:不但可以进行内容的读写，还可以进行单元格格式的修改
> 4. xlsxwriter:用于写文本，数字，公式，还可以进行单元格格式化，图片，图表，自动过滤等特性，针对的是.xlsx
>
> 5. openpyxl:对 Excel文件进行读写，修改，可以调整样式，设置单元格等操作

#### 2.安装第三方库

> 第三方库的安装和卸载：
>
> ​	a.安装
>
> ​		方式一：在cmd中，执行 pip   install   xxxx，默认的pip源在国外，下载速度较慢，注意：Mac使用pip3
>
> ​		方式二：在 pycharm 中直接添加
>
> ​	b.如果修改pip镜像源，可以将pip镜像源修改到国内，执行命令：pip   install   xxxx  -i   镜像源
>
> ​	 常用的国内镜像源如下：
>
> ​	（1）阿里云 http://mirrors.aliyun.com/pypi/simple/
> ​	（2）豆瓣http://pypi.douban.com/simple/
> ​	（3）清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
> ​	（4）中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
> ​	（5）华中科技大学http://pypi.hustunique.com/
>
> ​	（6）Python官方https://pypi.python.org/simple
>
> ​	c.如果要卸载第三方模块，则执行pip  uninstall   xxx
>
> ```
> 不使用镜像：
> 	pip/pip3   install   xlrd
> 	pip/pip3   install   xlwt
> 	pip/pip3   install   xlwings
> 	pip/pip3   install   xlsxWriter
> 	pip/pip3   install   openpyxl
> 	pip/pip3   install    pandas
> 	
> 使用镜像：
> 	pip/pip3   install  xlrd   -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> 	pip/pip3   install  xlwt  -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> 	pip/pip3   install  xlwings  -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> 	pip/pip3   install  xlsxWriter  -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> 	pip/pip3   install  openpyxl  -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> 	pip/pip3   install  pandas  -i  https://pypi.tuna.tsinghua.edu.cn/simple/
> ```

### 三、xlrd和xlwt 模块

> ​	如果要处理Excel 2010文档更早格式的Excel文档，需要用到其它库(如:xlrd、xlwt等)，特别是.xls 文件

#### 1.xlrd

> ```Python
> import  xlrd
>
> # xlrd:读取
> # a.打开工作簿
> wb = xlrd.open_workbook("info.xls")
> # b.获取所有的工作表
> print(wb.sheet_names())
> # c.根据索引获取指定的工作表对象
> sheet1 = wb.sheet_by_index(0)
> print(sheet1)
> # d.根据名称获取指定的工作表对象
> sheet2 = wb.sheet_by_name('Sheet2')
> print(sheet2)
> # e.获取工作表的行数和列数
> print(sheet1.nrows)
> print(sheet1.ncols)
>
> # f.获取单元格
> cell = sheet1.cell(0,0)
> print(cell)
> print(cell.value)   # 获取单元格的文本值
> ```

#### 2.xlwt

> ```Python
> import  xlwt
>
> # xlwt:写入
> # a.创建工作簿对象
> wb = xlwt.Workbook()
> # print(wb)
>
> # b.增加一张工作表
> # 注意：一个工作簿中至少需要有一张工作表
> sheet = wb.add_sheet("学生成绩信息")
> # print(sheet)
>
> # c.向工作表中写入数据
> # 注意：向excel中写入数据，文件必须处于关闭状态，行和列都是从0开始计算的
> # 写入表头
> headers = ['姓名',"性别",'成绩']
> for index,header in enumerate(headers):
>     # sheet.write(row,col,value)
>     sheet.write(0,index,header)
>
> # 写入正文
> data = [
>     ['张三','男',66],
>     ['小明','男',100],
>     ['李四','女',70],
>     ['jack','男',34]
> ]
> # 第1~4行  第0~2列
> for row in range(len(data)):
>     for col in range(len(data[row])):
>         sheet.write(row + 1,col,data[row][col])
>
> # d.保存工作簿
> wb.save("info.xls")
> ```

### 四、openpyxl操作Excel

> ​	openpyxl是一个开源项目，openpyxl模块是一个读写Excel 2010文档的Python 库，这是openpyxl比较其他模块的不足之处。openpyxl是一款比较综合的工具，不仅能够同时读取和修改Excel文档，而且可以对Excel文件内单元格进行详细设置，包括 单元格样式等内容，甚至还支持图表插入、打印设置等内容，使用openpyxl可以 读写xltm, xltx, xlsm, xlsx等类型的文件，且可以处理数据量较大的Excel文件，跨平台处理大量数据是其它模块没法相比的。因此，openpyxl成为处理Excel复杂问题的首选库函数
>
> 在使用openpyxl前先要掌握三个对象，即:
>
> - Workbook：工作簿，一个包含多个Sheet的Excel文件
> - Worksheet：工作表，一个Workbook有多个Worksheet，表名识别，如 “Sheet1”,“Sheet2”
> - Cell：单元格，存储具体的数据对象

> 具体的使用流程是:
>
> 1. 导入openpyxl模块
>
> 2. 调用openpyxl.load_workbook()函数或openpyxl.Workbook()，取得
>
>    Workbook工作簿对象。
>
> 3. 调用get_active_sheet()或get_sheet_by_name()工作簿方法,取得Worksheet
>
>    工作表对象。
>
> 4. 使用索引或工作表的cell()方法，带上row和column关键字参数,取得Cell对象,
>
>    读取或编辑Cell对象的value属性

#### 1.读取excel文档

> ```Python
> import  openpyxl
>
> # 1.打开工作簿，获取工作簿对象
> wb = openpyxl.load_workbook("student-score.xlsx")
> # print(wb)
>
> # 2.获取工作表对象
> print(wb.sheetnames)
>
> # 方式一：wb[工作表名称]    推荐使用
> sheet1 = wb['成绩表']
> print(sheet1)
>
> # 方式二：wb.get_sheet_by_name(工作表名称)  Python高版本中废弃
> # sheet2 = wb.get_sheet_by_name("第3小学")
> # print(sheet2)
>
> # 3.获取指定表的指定行
> # sheet[行号]
> row = sheet1[3]
> print(row,type(row))   # tuple
> for cell in row:
>     print(cell.value)   # 获取单元格的值
>
> # 4.获取指定列
> col = sheet1['C'][2:]
> # print(col)  # tuple
> # 需求：统计不重复的学校名称
> school_name = set([cell.value for cell in col])
> print(school_name)
>
> # 5.获取单元格，需求：获取B5单元格
> # 方式一：sheet["行号列号"]
> cell1 = sheet1['B5']
> print(cell1.value)
> # 方式二：sheet.cell(行号，列号),注意：列号需要使用数字表示，A--->1,B--->2。。。
> cell2 = sheet1.cell(5,2)
> print(cell2.value)
>
> # 6.关闭工作簿
> wb.close()
> ```

#### 2.写入excel文档

> ```Python
> import  openpyxl
>
> # 1.创建工作簿【文档】
> """
> # 注意：openpyxl.Workbook()表示创建一个空的工作簿对象
> wb = openpyxl.Workbook()
> # 获取工作簿中所有工作表的名称，默认情况下新建的Excel文件中只有一张名称为"Sheet"的工作表
> print(wb.sheetnames)   # ['Sheet']
> # 获取活跃表
> sheet = wb.active
> print(sheet)
> # 修改表的名称
> sheet.title = "用户信息表"
> wb.save('text01.xlsx')
> """
>
> # 2.添加或删除工作表
> """
> wb = openpyxl.Workbook()
> print(wb.sheetnames)   # ['Sheet']
> # 新增一张工作表
> wb.create_sheet()
> print(wb.sheetnames)   # ['Sheet', 'Sheet1']
> # 获取当前活动工作表
> current_sheet = wb.active
> current_sheet.title = "学生信息表"
> print(wb.sheetnames)   # ['学生信息表', 'Sheet1']
> # 复制表
> wb.copy_worksheet(current_sheet)
> print(wb.sheetnames)   # ['学生信息表', 'Sheet1', '学生信息表 Copy']
> wb.create_sheet("财务")
> print(wb.sheetnames)  # ['学生信息表', 'Sheet1', '学生信息表 Copy', '财务']
>
> # 在指定位置创建一张新的工作表
> wb.create_sheet(index=0,title='销售')
> print(wb.sheetnames)  # ['销售', '学生信息表', 'Sheet1', '学生信息表 Copy', '财务']
>
> # 删除工作表
> wb.remove(wb['Sheet1'])
> print(wb.sheetnames)
>
> wb.save("text02.xlsx")
> """
>
> # 3.修改和追加单元格                *******
> """
> wb = openpyxl.load_workbook('text01.xlsx')
> print(wb.sheetnames)
> # 语法：sheet["行号列表"] = 值   或者  sheet.cell(行号，列号,值)
> sheet = wb['用户信息表']
> sheet['A1'] = "姓名"
> sheet['B1'] = "年龄"
> sheet.cell(1,3,"性别")
> data_list = [
>     ['张三',10,'male'],
>     ['李四',12,'female'],
>     ['王五',14,'male'],
>     ['小明',11,'male']
> ]
> for data in data_list:
>     # sheet.append(列表):追加一行
>     sheet.append(data)
>
> # 修改工作表最后一定要注意保存
> wb.save('text01.xlsx')
> """
>
> # 4.添加删除行和列
> wb = openpyxl.load_workbook('text01.xlsx')
> sheet = wb['用户信息表']
> # 插入行,insert_rows(id,num),如果省略num，默认在id的前面插入一行，否则插入指定行
> # sheet.insert_rows(1)
> # sheet.insert_rows(4,2)
>
> # 插入列
> # sheet.insert_cols(2,5)
>
> # 删除行或列
> # sheet.delete_rows(4,2)
> sheet.delete_cols(2,5)
> wb.save('text01.xlsx')
> ```

#### 3.设置单元格样式【了解】

> ​	实际生活中，咱们可以通过软件来操作单元格中的内容的样式包括:字体、颜色 等，也可以对列或者行进行合并操作，还可以添加公式以及调整行高和列的宽度。 同样的，这些操作 openpyxl 也可以实现。 用表格展示数据的时候，有的时候我 们可能需要对不同的数据以不同的⻛格进行展示从而达到分区或者强调的作用。如 果想要自定义单元格的⻛格，需要从 openpyxl.styles 模块中导入相应的类	
>
> ```Python
> import  openpyxl
> from openpyxl.styles import  Font,PatternFill,Border,Side,Alignment
>
> # 1.打开工作簿
> wb = openpyxl.load_workbook('student-score.xlsx')
> sheet = wb['第2小学']
>
> # 2.设置单元格样式
> # a.设置字体
> # 1>创建字体对象
> font = Font(
>     size=20,
>     italic=True,
>     color="EE82EE",   # 此处的颜色必须是rgb的十六进制表示，不能使用颜色的单词
>     bold=True
> )
> # 2>给指定单元格对象设置字体
> sheet['A1'].font = font
>
> # b.设置单元格的填充
> """
>  # 填充样式
> {'lightVertical', 'darkVertical', 'darkHorizontal', 'lightUp', 
> 'lightDown', 'gray125', 'darkGrid', 'lightGray', 'gray0625', 'darkUp',
>  'lightGrid', 'lightTrellis', 'darkGray', 
> 'darkTrellis', 'mediumGray', 'darkDown', 'solid', 'lightHorizontal'}
> """
> fill = PatternFill(
>     fill_type="darkGray",
>     start_color="0000FF"
> )
> sheet['B2'].fill = fill
>
> # c.设置单元格对齐样式
> align = Alignment(
>     horizontal="center",    # 水平方向：left  center right
>     vertical="center"         # 垂直方向：top  center  bottom
> )
> sheet['C1'].alignment = align
>
> # d.设置边框样式
> """
> 边框样式
> ('dashDot','dashDotDot', 'dashed','dotted',
>                             'double','hair', 'medium', 'mediumDashDot', 'mediumDashDotDot',
>                             'mediumDashed', 'slantDashDot', 'thick', 'thin')
> """
> # 创建边对象【四个边框可以共用同一个对象，也可以分别创建多个对象】
> side = Side(border_style="thin",color='00FA9A')
> border = Border(left=side,right=side,bottom=side,top=side)
> sheet["D1"].border = border
>
> # e.设置单元格的宽度和高度
> sheet.column_dimensions['A'].width = 20   # 设置A列的宽度
> sheet.row_dimensions[1].height = 40   # 设置第2行的高度
>
> # 3.保存文件
> wb.save('student-score.xlsx')
> ```

#### 4.画图

> ```Python
> import openpyxl
> from openpyxl.chart import  PieChart,LineChart,BarChart,Reference
>
> # 1.选定工作表
> wb = openpyxl.load_workbook('student-score.xlsx')
> sheet = wb['第5小学']
> print(sheet)
>
> # 2.获取数据,选取第5小学的语文成绩
> data = []
> for row in range(2,60):
>     data.append(sheet.cell(row,3).value)
> print(data)
>
> # 3.处理数据
> score_dict = {'90~100':0,'70~89':0,'60~69':0,'<60':0}
> for score in data:
>     if score >= 90:
>         score_dict['90~100']  += 1
>     elif score >= 70:
>         score_dict['70~89'] += 1
>     elif score >= 60:
>         score_dict['60~69'] += 1
>     else:
>         score_dict['<60'] += 1
> print(score_dict)
>
> # 4.将上述数据添加到表中
> # M:key,N:value
> row = 2
> for key,value in score_dict.items():
>     sheet[f"M{row}"] = key
>     sheet[f"N{row}"] = value
>     row += 1
>
> # 5.绘图
> # a.绘制折线图
> # 选择图表中的数据源
> # values = Reference(sheet,min_col=13,min_row=2,max_row=59)
> # line = LineChart()   # 创建图表对象
> # line.add_data(values)  # 添加数据
> # sheet.add_chart(line,"M7")  # 指定图表添加的位置
>
> # b.绘制条形图/柱状图
> # values = Reference(sheet,min_col=14,min_row=2,max_row=5)
> # bar = BarChart()   # 创建图表对象
> # bar.add_data(values)  # 添加数据
> # sheet.add_chart(bar,"M30")  # 指定图表添加的位置
> # bar.title = "不同阶段分数的人数分布图"
>
> # c.绘制饼图
> labels = Reference(sheet,min_col=13,min_row=2,max_row=5)  # 选取标签
> values = Reference(sheet,min_col=14,min_row=2,max_row=5)  # 选取数据
> pie = PieChart()   # 创建图表对象
> pie.add_data(values)  # 添加数据
> pie.set_categories(labels)  # 设置标签
> sheet.add_chart(pie,"M50")  # 指定图表添加的位置
> pie.title = "不同阶段分数的人数饼图"
>
> wb.save("student-score.xlsx")
> ```