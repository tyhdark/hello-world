def my_decorator(func):
    def inner_func(*args, **kwargs):
        print(2023_08_15)
        return func()

    return inner_func


@my_decorator
def update_list():
    # 需要输出，去嵌套，去重，且不破坏顺序的新列表
    old_list = [[1, 2, 3], [6, 3, 5, 8], [2, 3, 5, 8, 9, 0]]
    # new_list = []
    # for i in old_list:
    #     for z in i:
    #         new_list.append(z)
    # new_list = set(new_list)
    # new_list = list(new_list)
    xlist = [x for x in old_list]
    print(xlist)
    new_list = set([item for sublist in old_list for item in sublist])

    return new_list


if __name__ == '__main__':
    print(update_list())
