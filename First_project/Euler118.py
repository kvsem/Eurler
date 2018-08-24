import sys
sys.setrecursionlimit(100000)


class Euler(object):
    subset_list = []
    input_list = []

    def __init__(self, input_list):
        self.input_list = input_list

    def __call__(self):
        K = self.allsubsets(self.input_list);
        print(K)
        self.select_prime_set(self.subset_list)

    def copy(self, src_list, index_list):
        result = []
        for i in index_list:
            result.append(src_list[i])

        return result

    def forward_index(self, idx, max_length):
        changed = False
        r = list(range(0, len(idx)))
        r.reverse()
        idx_length = len(idx)
        for i in r:
            if idx[i] == max_length - idx_length + i:
                continue
            else:
                # 이 부분이 위 그림에서 (1) 이라고 표현된 부분
                idx[i] = idx[i] + 1
                for j in range(i + 1, idx_length):
                    idx[j] = idx[j - 1] + 1
                changed = True
                break

        if changed == True:
            return idx
        else:
            return []

    def ksubset(self, L, k):
        src_length = len(L)
        if src_length < k: return []
        if src_length == k: return [L]
        if src_length == 0: return []

        max_length = src_length
        ksubsets = []
        idx = list(range(0, k))
        while idx != []:
            subset = self.copy(L, idx)
            ksubsets.append(subset)
            idx = self.forward_index(idx, max_length)

        return ksubsets

    def allsubsets(self, L):
        result = [];
        for i in range(1, len(L)):
            k = self.ksubset(L, i)
            result.extend(k)

        return result

    def select_prime_set(self, set_list):
        pass


if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    euler = Euler(input_list)
    euler()
