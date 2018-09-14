class Euler(object):
    num = 0
    sum = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):

        for a in range(3, self.num+1):
            max_r = 0
            max_n = 0
            for n in range(1, a+1):
                r = (pow(a-1, n) + pow(a+1, n)) % pow(a, 2)
                if max_r < r:
                    max_n = n
                max_r = max(r, max_r)

            self.sum += max_r
            print(f"pow({a}, {max_n}) : {max_r} -> {self.sum}")


if __name__ == "__main__":
    input_num = 1000
    euler = Euler(input_num)
    euler()
