import numpy as np
import matplotlib.pyplot as plt


def demo_random():
    # 里面可以加维度，默认是一维的一个
    temp_data = np.random.randn(2, 3)
    print(temp_data)
    samples = np.random.normal(loc=5, scale=2, size=(4, 4))
    print(samples)


def demo_arrange():
    temp_a = np.array([['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']])
    print(temp_a)
    print(type(temp_a))
    print(temp_a.dtype)
    # astype会创建数组备份
    temp_b = temp_a.astype(np.int32)
    print(temp_b)


def demo_dot():
    # 要注意np中集合的默认运算并不是点乘的
    a = np.arange(0, 9).reshape(3, 3)
    print(a)
    b = a.copy() + 1
    print(b)
    print(a + b)
    print(a - b)
    print(a * b)
    print(np.dot(a, b))
    print(a > b)


def demo_slice():
    a = np.arange(0, 9).reshape(3, 3)
    # 尽管是在二维空间中选择，但是np中如果只选择一列，结果仍会转换成一维
    print(a[:, 0])
    b = a.copy()
    print(a[~(b < 5)])
    print(a[[1, 2], :])


def demo_meshgrid_and_where():
    a = np.arange(0, 3, 0.01)
    xs, ys = np.meshgrid(a, a)
    print(xs)
    print(ys)
    z = np.sqrt(xs ** 2 + ys ** 2)
    print(z)
    plt.imshow(z)
    plt.colorbar()
    plt.title("Image plot of $\sqrt{x^2+y^2}$")
    plt.show()
    b = np.arange(0, 9).reshape(3, 3)
    print(b)
    b = np.where(b > 3, 3, -1)
    print(b)


if __name__ == '__main__':
    demo_random()
    demo_arrange()
    demo_dot()
    demo_slice()
    demo_meshgrid_and_where()
