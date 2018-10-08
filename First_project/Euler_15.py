class Euler(object):
    def __init__(self, num):
        self.num = num

    def __call__(self):
        print(self.factorial(self.num*2) / (self.factorial(self.num) * self.factorial(self.num)))

    def factorial(self, num):
        result = 1
        for i in range(1, num+1):
            result = result * i
        return result


if __name__ == "__main__":
    input = 20
    euler = Euler(input)
    euler()

