class Euler(object):
    num = 0
    a_list = list()

    def __init__(self, num):
        self.num = num

    def __call__(self):
        a = 11
        while 1:
            # is_able = False
            length = len(str(a))
            # for i in range(2, length+1):
            #     n_sqrt = pow(a, 1/i)
            #     if (n_sqrt % 1) == 0:
            #         is_able = True

            str_a = str(a)
            sum_of_all = 0
            for i in range(0, length):
                sum_of_all += int(str_a[i])

            if sum_of_all == 1:
                a += 1
                continue
            # if sum_of_all == 1 or is_able is False:
            #     a += 1
            #     continue

            pow_times = 2
            while 1:
                pow_of_sum = pow(sum_of_all, pow_times)

                if pow_of_sum > a:
                    break
                elif pow_of_sum == a:
                    self.a_list.append(a)
                    print(f"{len(self.a_list)} - {a} INSERTED")

                pow_times += 1

            if len(self.a_list) > self.num-1:
                print(self.a_list)
                return True

            a += 1


if __name__ == "__main__":
    input_num = 30
    euler = Euler(input_num)
    euler()
