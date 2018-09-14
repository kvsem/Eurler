class Euler(object):
    def __call__(self):
        n = 2357111317
        while 1:
            count = 0
            exist_list = list()
            for x in range(1, n * (n + 1) + 1):
                if x == n:
                    continue
                y = (x * n) / (x - n)
                if y % 1 == 0 and y > 0 and (int(y), x) not in exist_list:
                    # print(f"{x}, {int(y)}")
                    exist_list.append((x, int(y)))
                    count += 1

            print(f"{n} : {count}")

            n += 1

            if count >= 1000:
                print(f'{n} 돌파')
                return True


if __name__ == "__main__":
    euler = Euler()
    euler()
