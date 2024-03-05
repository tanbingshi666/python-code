def class_method_no_class(name):
    print("I am a class method " + name)


class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)

    @classmethod
    def class_method(cls):
        t = cls(name="tanbs", age=24)
        t.show_info()
        print("I am teacher a class method")

    @staticmethod
    def static_method():
        print("I am a static method")
