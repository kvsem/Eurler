class Euler(object):
    num = 0

    def __init__(self, num):
        self.num = num

    def __call__(self):
        val_dict = {
            0: '',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'hundred',
            1000: 'one thousand',
        }

        sum_of_text = 0

        for i in range(1, self.num+1):
            _text = ''
            if i <= 20:
                _text = f"{_text}{val_dict[int(str(i))]}"
            elif i < 100:
                _len = len(str(i))
                _text_10 = val_dict[int(str(i)[0])*10]
                _text = f"{_text_10} {val_dict[int(str(i)[1])]}"
            elif str(i)[1:] == '00':
                _text = f"{val_dict[int(str(i)[0])]} {val_dict[100]}"
            elif i < 1000:
                _len = len(str(i))
                _text_100 = f"{val_dict[int(str(i)[0])]} {val_dict[100]}"
                _text_10 = val_dict[int(str(i)[1])*10]
                if str(i)[1] == '1':
                    _text_10 = val_dict[int(str(i)[1:3])]
                    _text = f"{_text_100} and {_text_10}"
                else:
                    _text = f"{_text_100} and {_text_10} {val_dict[int(str(i)[2])]}"
            else:
                _text = val_dict[1000]

            unblank_text = _text.replace(' ', '')
            sum_of_text += len(unblank_text)
            print(f"{i} : {_text} : {len(unblank_text)} -> {sum_of_text}")

        print(sum_of_text)


if __name__ == "__main__":
    input_num = 1000
    euler = Euler(input_num)
    euler()
