def my_decorator(func):
    def inner_func(*args, **kwargs):
        print("现在计算的是", *args, "的和")
        return func(*args)

    return inner_func


def return_decorator(flag):
    def my_01_decorator(func):
        def inner_func(*args, **kwargs):
            print("使用的flag是：", flag)
            return func(*args)

        return inner_func

    return my_01_decorator


@my_decorator
def num_add(a, b, c):
    """
    使用普通的装饰器
    :param a:
    :param b:
    :return:
    """
    return a + b + c


@return_decorator("-")
def num_sub(a, b):
    """
    使用带参数的装饰器
    :param a:
    :param b:
    :return:
    """
    return a - b


class Tang:
    def __init__(self):
        return

    @my_decorator
    def add_num(self, a, b):
        return a + b

    @return_decorator("-")
    def sub_num(self, a, b):
        return a - b


if __name__ == '__main__':
    # print(num_add(10, 2, 10))
    # print(num_sub(10, 2))
    tang = Tang()
    print(tang.add_num(11, 10))
    print(tang.sub_num(10, 5))
