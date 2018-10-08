class Euler(object):
    def __call__(self):
        result_list = []
        for below in range(10, 100):
            for upper in range(10, below):
                if str(upper)[1] != str(below)[0]:
                    continue
                if int(str(below)[1]) == 0:
                    continue

                if int(str(upper)[0]) / int(str(below)[1]) == upper / below:
                    result_list.append(f"{upper}/{below}")

        print(result_list)
        upper_mul = 1
        below_mul = 1

        for each in result_list:
            upper = each.split('/')[0]
            below = each.split('/')[1]
            upper_mul = upper_mul * int(upper)
            below_mul = below_mul * int(below)

        print(f"{upper_mul}/{below_mul}")


if __name__ == "__main__":
    euler = Euler()
    euler()

