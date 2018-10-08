class Euler(object):
    sum = 0

    def __init__(self, num):
        self.num = num
        self.num_list = [2, 3]

    def __call__(self):
        print(self.primes_up_to_good(self.num))
        print(sum(self.primes_up_to_good(self.num)))

    def primes_up_to_good(self, n: int) -> [int]:
        seive = [False, False, True, True] + [True] * (n - 1)
        k = 5
        while k < n + 1:
            if seive[k]:
                seive[k * 2::k] = [False] * (((n + 2) // k) - 1)
            k += 2
        return [x for x in range(n + 1) if seive[x]]


if __name__ == "__main__":
    input = 2000001
    euler = Euler(input)
    euler()

