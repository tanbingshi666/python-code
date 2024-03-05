class Animal(object):
    def __init__(self, name, size, high, age=None):
        self.name = name
        self.size = size
        self.__high = high
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def show(self):
        print('name = %s, size = %s, high = %s' % (self.name, self.size, self.__high))

    def __high__(self):
        return self.__high

    def get_high(self):
        return self.__high

    def set_high(self, high):
        self.__high = high
