class MorseCode(object):
    alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
    origin_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self, input_code):
        self.code = input_code

    def __call__(self):
        words = code.split("  ")
        for word in words:
            letters = word.split(" ")
            for letter in letters:
                index = self.alphabet.index(letter)
                print(f"{self.origin_alphabet[index]}", end="")
            print(" ", end="")


if __name__ == "__main__":
    code = ".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
    morse = MorseCode(code)
    morse()
