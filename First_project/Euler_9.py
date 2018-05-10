class Euler(object):
    max = 0
    num = ''

    def __init__(self, num):
        self.num = num

    def __call__(self):
        for a in range(1, self.num//3):
            for b in range(a, self.num//2):
                for c in range(b, self.num//2):
                    if a+b+c == 1000:
                        if pow(a,2) + pow(b,2) == pow(c,2):
                            print(f"{a}, {b}, {c}")


if __name__ == "__main__":
    input = 1000
    euler = Euler(input)
    euler()
