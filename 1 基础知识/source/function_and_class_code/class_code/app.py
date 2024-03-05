from class_code.class_define import teacher
from class_code.class_define.animal import Animal
from class_code.class_define.person import Person
from class_code.class_define.son import SonA
from class_code.class_define.student import Student
from class_code.class_define.teacher import Teacher

# student = Student()
# student.run()
# student.eat('花')

# 动态绑定属性和限制绑定
# student.name = 'tan'
# student.age = 25
# student.bobby = 'dance'
# student.show()
# print('name =', student.name)

# __init__ 构造函数
# student = Student('tan', 25)
# student.show()

# __new__ 和 __init__ 工作原理
# student = Student('tan', 25)
# student.show()

# 类属性和实例属性
# person = Person('tan', 25)
# print(Person.name)
# print(person.name)
#
# Person.name = 'PersonName'
# print(Person.name)
# print(person.name)

# 私有属性
# animal = Animal('animal', 1, 165)
# print(animal.name)
# print(animal.high)
# print(animal.get_high()
# animal.show()
# animal.set_high(172)
# print(animal.get_high())

# @properties
# animal.age = 12 # 不能设置 @properties 修饰的属性
# print(animal.age)
# animal.age = 25
# print(animal.age)

# 继承
# son_a = SonA('tan', 25)
# son_a.show()
# son_a.hello()

# 运算符重载
# print(1 + 2)
# print('1' + '2')
# print('2'.__add__('3'))
# print([34, 66] + [1, 2])
# print([34, 66].__add__([1, 2]))
# print((34, 66) + (1, 2))
# print((34, 66).__add__((1, 2)))
# print(dir('hello'))
# print(__name__)

# 类方法和静态方法
# tim = Teacher('tim', 23)
# Teacher.show_info(tim)
teacher.class_method_no_class('桀桀桀')
Teacher.class_method()
Teacher.static_method()
