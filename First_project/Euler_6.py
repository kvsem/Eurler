
class Euler(object):
    num = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):
        pow_sum_result = 0
        sum_pow_result = 0

        for i in range(1, self.num+1):
            pow_sum_result += pow(i,2)
            sum_pow_result += i
        print(pow(sum_pow_result, 2) - pow_sum_result)


if __name__ == "__main__":
    euler = Euler(100)
    euler()
