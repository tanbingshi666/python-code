from class_code.class_define.father import Father


class SonA(Father):

    # def __init__(self, name, age, friends):
    #     super().__init__(name, age)
    #     self.__friends = friends

    # def get_friends(self):
    #     return self.__friends
    def show(self):
        print('我是 SonA %s, 今年 %s 岁了' % (self.name, self.age))
