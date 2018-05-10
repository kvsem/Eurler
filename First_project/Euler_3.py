import math


class Euler(object):
    num = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):
        for i in range(int(math.sqrt(self.num)), 1, -1):
            if self.num % i == 0 and self.is_prime(i) is True:
                print(i)

    def is_prime(self, prime):
        for i in range(2, prime):
            if prime % i is 0:
                return False
        return True


if __name__ == "__main__":
    euler = Euler(600851475143)
    euler()
