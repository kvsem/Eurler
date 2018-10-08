class Euler(object):
    def __call__(self):
        i = 1
        result = 0
        while True:
            str_i = str(i)
            sum_of_fact = 0
            for each in str_i:
                sum_of_fact += self.factorial(int(each))

            # print(f"{i} / {sum_of_fact}")
            if sum_of_fact == i and i != 1 and i != 2:
                result += i

            if sum_of_fact*10000 < i:
                break
            i += 1
        print(result)

    def factorial(self, num):
        result = 1
        for i in range(1, num+1):
            result = result * i
        return result


if __name__ == "__main__":
    euler = Euler()
    euler()

