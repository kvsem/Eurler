class Euler(object):
    num = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):
        not_increase_decrease = list()
        for each_num in range(1, self.num+1):
            num = each_num
            num_size = len(str(num))
            str_num = str(num)
            last_num = int(str_num[0])
            increase = False
            decrease = False

            for i in range(0, num_size):
                i_num = int(str_num[i])
                if i_num < last_num:
                    decrease = True
                elif i_num > last_num:
                    increase = True

                if decrease is True and i_num > last_num:
                    not_increase_decrease.append(num)
                    break
                if increase is True and i_num < last_num:
                    not_increase_decrease.append(num)
                    break

                last_num = i_num

        print(len(not_increase_decrease)/self.num)
        if len(not_increase_decrease)/self.num >= 0.99:
            print(f"{self.num}!!!!!!!!!!!!!")


if __name__ == "__main__":
    for i in range(1587000, 10000000):
        input_num = i
        euler = Euler(input_num)
        euler()
