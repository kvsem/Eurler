class Euler(object):
    times_list = list()

    def __call__(self):
        for n in range(1, 1000000):
            print(n)
            each_list = [n]
            while 1:
                if n % 2 == 0:
                    n = n / 2
                    each_list.append(n)
                else:
                    n = 3 * n + 1
                    each_list.append(n)

                if n == 1:
                    self.times_list.append(len(each_list))
                    break

        max_times = max(self.times_list)
        max_index = self.times_list.index(max_times)

        print(max_index+1)


if __name__ == "__main__":
    euler = Euler()
    euler()
