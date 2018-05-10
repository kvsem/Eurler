class Euler(object):
    sum = 0

    def __init__(self, num):
        self.num = num
        self.num_list = [x for x in range(2, num+1)]

    def __call__(self):
        for i in self.num_list:
            print(f"{i} 의 배수 제거")
            for j in range(4, self.num+1):
                if i == j:
                    continue
                if j % i != 0:
                    continue
                if j not in self.num_list:
                    continue
                del self.num_list[self.num_list.index(j)]
        print(self.num_list)


if __name__ == "__main__":
    input = 200000
    euler = Euler(input)
    euler()
