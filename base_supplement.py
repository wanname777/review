def demo_rest():
    values = 1, 2, 3, 4, 5
    # python的新特性，*rest可作为剩余参数的代表，你也可以使用*_，怎样都可以
    a, b, *rest = values
    print(a)
    print(b)
    print(rest)


def demo_some_functions():
    b = ['saw', 'small', 'He', 'foxes', 'six']
    b.sort(key=len)
    print(b)
    numbers = []
    values = []
    for i, value in enumerate(b):
        # print(i,value)
        numbers.append(i)
        values.append(value)
    for i in zip(numbers, values):
        print(i)
    print(hash('nihaoaaa'))


def demo_more_lists():
    strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
    temp_a = [i.upper() for i in strings if len(i) > 2]
    print(temp_a)
    temp_b = set(map(len, strings))
    print(temp_b)
    all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
                ['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
    temp_name = [j for i in all_data for j in i if j.count('e') >= 2]
    print(temp_name)
    some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    # 生成了二维的list而不是一维，这是一件神奇的事
    to_lists = [[x for x in tup] for tup in some_tuples]
    print(to_lists)


def demo_set():
    a = set([2, 2, 2, 1, 3, 3])
    b = {3, 4, 5, 6, 7, 8}
    print(a | b)
    print({1, 2, 3}.issubset(a | b))
    print({1, 2, 3} == {3, 2, 1})


if __name__ == '__main__':
    demo_rest()
    demo_some_functions()
    demo_set()
    demo_more_lists()
