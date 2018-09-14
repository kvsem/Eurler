class Euler(object):
    num = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):
        result_list = list()
        target_num = 2
        while 1:
            is_able = True
            target_list = list(str(target_num))

            for i in range(2, self.num+1):
                exc_num = target_num * i
                for j in str(exc_num):
                    if j not in target_list:
                        is_able = False
                        break
                if is_able is False:
                    break

            if is_able is True:
                result_list.append(target_num)
                print(result_list)
            target_num += 1


if __name__ == "__main__":
    input_num = 6
    euler = Euler(input_num)
    euler()
