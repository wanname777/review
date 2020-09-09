# 或许可以用object当总父类，但是我忘了
class Dog(object):
    def __init__(self, name, age=0):
        # 决定了生成时需要传递的参数,仍然是有默认值的参数放后面
        # __name表示私有成员
        self.__name = name
        self.age = age

    def get(self):
        print(self.__name.title() + str(self.age))

    def __this(self):
        # __this表示私有函数
        print('hi')


class Ddog(Dog):
    def __init__(self, name, age, dd):
        super().__init__(name, age)
        self.dd = dd

    def get(self):
        super().get()
        print(self.dd)


if __name__ == '__main__':
    temp_dog = Dog('aa')
    temp_dog.get()
    # 将name设置为私有，外部修改时不会报错，当然也不会修改
    # 必须用_class__attribute/way来调用或修改
    # 调用私有方法时似乎警告了些什么
    temp_dog._Dog__name = 'bb'
    temp_dog.get()
    temp_dog._Dog__this()
    temp_Ddog = Ddog('cc', 1, 22)
    temp_Ddog.get()
