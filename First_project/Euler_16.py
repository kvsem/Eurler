class Euler(object):
    def __call__(self):
        target_num = pow(2, 1000)
        result = 0
        for i in str(target_num):
            result += int(i)

        print(result)


if __name__ == "__main__":
    euler = Euler()
    euler()
