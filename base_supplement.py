def demo_rest():
    values=1,2,3,4,5
    # python的新特性，*rest可作为剩余参数的代表，你也可以使用*_，怎样都可以
    a,b,*rest=values
    print(a)
    print(b)
    print(rest)
if __name__ == '__main__':
    demo_rest()