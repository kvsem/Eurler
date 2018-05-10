
class Euler(object):
    n = 0

    def __init__(self, num):
        self.n = num

    def __call__(self):
        for i in range(1, self.n+1):
            print(i)


if __name__ == "__main__":
    num = 1000
    euler = Euler(num)
    euler()

# TODO 로직으로 다시