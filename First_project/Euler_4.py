
class Euler(object):

    def __init__(self):
        pass

    def __call__(self):
        for i in range(999, 900, -1):
            for j in range(999, 900, -1):
                str_num = str(i * j)
                if str_num == str_num[::-1]:
                    print(str_num)
            # if str_i == str_i[::-1]:
            #     print(i)


if __name__ == "__main__":
    euler = Euler()
    euler()
