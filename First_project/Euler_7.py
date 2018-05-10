class Euler(object):
    count = 0
    num = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):
        prime = True
        for i in range(1, 1000000000):
            for j in range(3, int(i/3)+1):
                if i % j == 0:
                    prime = False
                    break
            if prime is False:
                prime = True
                continue
            self.count += 1
            print(f"{self.count} {i}")
            if self.count == self.num:
                return


if __name__ == "__main__":
    euler = Euler(10001)
    euler()

# TODO 시간 단축