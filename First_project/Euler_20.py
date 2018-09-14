class Euler(object):
    def __call__(self):
        target_num = 1
        for i in range(1, 101):
            target_num = target_num * i

        result = 0
        for i in str(target_num):
            result += int(i)

        print(result)


if __name__ == "__main__":
    euler = Euler()
    euler()
