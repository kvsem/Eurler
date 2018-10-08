message_list = list()


class User_A:
    nickname = ''
    message_index = list()
    message_count = 0

    def __init__(self, _nickname):
        self.nickname = _nickname

    def insert(self):
        text = f"{self.nickname}님이 들어왔습니다."
        message_list.append(text)
        self.message_index.append(message_list.index(text))

    def change_and_inset(self, change_nickname):
        self.change(change_nickname)
        self.insert()

    def exit(self):
        text = f"{self.nickname}님이 나갔습니다."
        message_list.append(text)
        self.message_index.append(message_list.index(text))

    def change(self, change_nickname):
        for message_index in self.message_index:
            message_list[message_index] = message_list[message_index].replace(self.nickname, change_nickname)
        self.nickname = change_nickname


class User_B:
    nickname = ''
    message_index = list()
    message_count = 0

    def __init__(self, _nickname):
        self.nickname = _nickname

    def insert(self):
        text = f"{self.nickname}님이 들어왔습니다."
        message_list.append(text)
        self.message_index.append(message_list.index(text))

    def change_and_inset(self, change_nickname):
        self.change(change_nickname)
        self.insert()

    def exit(self):
        text = f"{self.nickname}님이 나갔습니다."
        message_list.append(text)
        self.message_index.append(message_list.index(text))

    def change(self, change_nickname):
        for message_index in self.message_index:
            message_list[message_index] = message_list[message_index].replace(self.nickname, change_nickname)
        self.nickname = change_nickname


def solution(record):
    user_a = User_A('Muzi')
    user_b = User_B('Prodo')
    user_a.insert()
    print(message_list)
    user_b.insert()
    print(message_list)
    user_a.exit()
    print(message_list)
    user_a.change_and_inset('Prodo')
    print(message_list)
    user_b.change('Ryan')
    print(message_list)

    answer = [message_list]

    return answer


solution(1)