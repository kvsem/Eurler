from random import randrange


LAST = 'LAST'
LEFT = 'LEFT'
RIGHT = 'RIGHT'


class Run(object):
    num_of_pots = 0
    pot_list = list()

    def __init__(self, _num_of_pots):
        self.num_of_pots = _num_of_pots
        # 금화 단위 높여서
        self.pot_list = [randrange(30, 100, 5) for x in range(0, num_of_pots-1)]

    def __call__(self):
        player_a = Player(_name='PLAYER A')
        player_b = Player(_name='PLAYER B')

        player_list = [player_a, player_b]

        while len(self.pot_list) > 0:
            # Turn 부여
            if player_a.is_turn is True:
                player_a.is_turn = False
                player_b.is_turn = True
            else:
                player_a.is_turn = True
                player_b.is_turn = False

            for player in player_list:
                if player.is_turn is False:
                    continue

                print(f'[ TURN {player.name} ]')
                print(f"{self.pot_list}\n")

                if len(self.pot_list) < 2:
                    side = LAST

                else:
                    my_profit = self.pot_list[0] - self.pot_list[-1]
                    your_profit = self.pot_list[1] - self.pot_list[-2]

                    if my_profit > your_profit:
                        side = LEFT
                    else:
                        side = RIGHT

                self.gold_grasb(player, side)
                print(f"{player_a.name} : {player_a.gold} / {player_b.name} : {player_b.gold}\n")

        if player_a.gold > player_b.gold:
            win_player = player_a
        elif player_a.gold == player_b.gold:
            win_player = None
        else:
            win_player = player_b

        if win_player is not None:
            print(f"------- {win_player.name} WIN! -------\n")
        else:
            print(f"------- DRAW -------\n")

        if player_a.gold > player_b.gold:
            return 1
        elif player_a.gold == player_b.gold:
            return 0
        else:
            return -1

    def gold_grasb(self, player, side):
        if side is LEFT:
            gold = self.pot_list[0]
            self.pot_list = self.pot_list[1:len(self.pot_list)]
        else:
            gold = self.pot_list[-1]
            self.pot_list = self.pot_list[0:-1]
        print(f"{player.name} GET {side} POT : {gold} GOLD")
        player.get_gold(gold)


class Player:
    is_turn = False
    gold = 0
    name = ''

    def __init__(self, _name):
        self.name = _name

    def turn(self):
        self.is_turn = True

    def get_gold(self, gold):
        self.gold += gold


if __name__ == "__main__":
    # 짝수로 난수생성
    win_count = 0
    draw_count = 0
    lose_count = 0

    for i in range(1, 10000):
        num_of_pots = randrange(5, 20, 2)
        run = Run(num_of_pots)
        result = run()
        if result == 1:
            win_count += 1
        elif result == 0:
            draw_count += 1
        elif result == -1:
            lose_count += 1

    print(f"[ 전체 결과 ]\n승 : {win_count} / 무 : {draw_count} / 패 : {lose_count} -> 승률 : {win_count/(win_count+draw_count+lose_count)}")
