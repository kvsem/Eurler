class Euler(object):
    def __call__(self):
        result_list = []
        for i in range(100, 2000000):
            if i < 1000:
                num = 3
            elif i < 10000:
                num = 4
            else:
                num = 5

            if i % 100000 == 0:
                print(i)

            sum_of_place = 0
            for j in range(0, num):
                str_num = str(i)
                sum_of_place += pow(int(str_num[j]), 5)

            if i == sum_of_place:
                result_list.append(i)

        print(result_list)
        result = 0
        for a in result_list:
            result += a
        print(result)


if __name__ == "__main__":
    euler = Euler()
    euler()
