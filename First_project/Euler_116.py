class Euler(object):
    tiles = 0

    def __init__(self, _tiles):
        self.tiles = _tiles

    def __call__(self):
        tile_list = [0 for x in range(0, tiles)]

        # red
        each_red = 2
        method_red = self.get_method(each_red)
        print(f"RED : {method_red}")

        # green
        each_green = 3
        method_green = self.get_method(each_green)
        print(f"GREEN : {method_green}")

        # blue
        each_blue = 4
        method_blue = self.get_method(each_blue)
        print(f"BLUE : {method_blue}")
        print(f"TOTAL : {method_red + method_green + method_blue}")

    def get_method(self, each):
        max_tile = self.tiles // each

        method_num = 0
        total = self.tiles - (each-1)
        for i in range(1, max_tile + 1):
            pick = i
            method_num += int(fact(total) / (fact(pick) * fact(total - pick)))
            total -= (each-1)

        return method_num


def fact(num):
    result = 1
    for i in range(1, num+1):
        result = result * i

    return result


if __name__ == "__main__":
    tiles = 50
    euler = Euler(tiles)
    euler()
