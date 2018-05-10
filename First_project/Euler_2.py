class Euler(object):
    count = 0
    result = 0
    fibo_list = [1, 2]

    def __init__(self, count):
        self.count = count

    def __call__(self):
        self.fib(self.count)
        print(self.fibo_list)
        for fibo_num in self.fibo_list:
            if fibo_num % 2 == 0:
                self.result += fibo_num

        print(self.result)

    def fib(self, count):
        for n in range(0, count):
            last_index = len(self.fibo_list)
            next_num = self.fibo_list[last_index-1] + self.fibo_list[last_index-2]
            if next_num > 4000000:
                return True
            self.fibo_list.append(next_num)


if __name__ == "__main__":
    euler = Euler(100000)
    euler()
