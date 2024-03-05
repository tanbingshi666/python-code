class Student(object):
    print('this is class student')

    __slots__ = 'name', 'age', 'bobby'

    # def __new__(cls, *args, **kwargs):
    #     print('new 函数被调用')
    #     return super.__new__(cls)

    def __init__(self, name, age):
        print('构造函数被调用...')
        print('init 函数 self = ', id(self))
        self.name = name
        self.age = age
        self.bobby = None

    def run(self):
        print('this is run student')

    def eat(self, name):
        print('this is eat %s' % (name))

    def show(self):
        print(f'this is show {self.name}, {self.age}, {self.bobby}')
