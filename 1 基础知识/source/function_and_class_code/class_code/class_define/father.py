class Father(object):

    def __init__(self, name, age, money=None):
        self.name = name
        self.age = age
        self.__money = money

    @property
    def money(self):
        return self.__money

    def show(self):
        print('我是 %s, 今年 %s 岁了' % (self.name, self.age))

    def hello(self):
        print('hello %s' % self.name)
