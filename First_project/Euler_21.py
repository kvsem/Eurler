class Euler(object):
    result_set = set()

    def __init__(self, num):
        self.num = num

    def __call__(self):
        for i in range(0, self.num):
            d = self.get_d(i)
            # print(f"{i} : {self.get_d(i)}")
            if self.get_d(d) == i and d != i:
                self.result_set.add(i)
                self.result_set.add(d)
                print(f"{i} : {d}")

        print(self.result_set)
        print(self.get_sum_of_list(self.result_set))

    def get_d(self, num):
        _list = self.get_measure(num)
        sum_result = self.get_sum_of_list(_list)

        return sum_result

    @staticmethod
    def get_measure(num):
        measure_list = []
        for i in range(1, num):
            if num % i == 0:
                measure_list.append(i)

        return measure_list

    @staticmethod
    def get_sum_of_list(_list):
        sum_result = 0
        for i in _list:
            sum_result += i

        return sum_result


if __name__ == "__main__":
    input = 10000
    euler = Euler(input)
    euler()
