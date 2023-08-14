class Tang:
    test_dict = [1, 2, 3, 4]
    x = 5

    def print_dict(self):
        print("dict=", self.test_dict)
        print("x=", self.x)
        return

    def update_dict(self):
        self.test_dict[2] = 10
        self.x = 20
        print('修改后的dict---->', self.test_dict)
        print('修改后的x------>', self.x)
        return

    def test_lambda(self):
        numbers = [1, 3, 6]
        # new_numbers = tuple(map(lambda x: x, numbers))
        # print(new_numbers)
        print(tuple(map(lambda x: x, numbers)))

if __name__ == '__main__':
    my = Tang()
    # my.print_dict()
    # my.update_dict()
    my.test_lambda()

