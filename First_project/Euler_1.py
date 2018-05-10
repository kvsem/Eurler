class Euler(object):
    def __init__(self, limit):
        self.limit = limit

    def __call__(self):
        result = 0
        for n in range(1, self.limit):
            if n % 3 == 0 or n % 5 == 0:
                result += n
        print(result)


if __name__ == "__main__":
    limit = 1000
    euler = Euler(limit)
    euler()
