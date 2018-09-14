input_password = ['319', '680', '180', '690', '129', '620', '762', '689', '762', '318', '368', '710', '720', '710', '629', '168', '160', '689', '716', '731', '736', '729', '316', '729', '729', '710', '769', '290', '719', '680', '318', '389', '162', '289', '162', '718', '729', '319', '790', '680', '890', '362', '319', '760', '316', '729', '380', '319', '728', '716']


class Euler(object):
    def __call__(self):
        password = '12367890'
        while True:
            if '4' in password or '5' in password:
                password = str(int(password) + 1)
                continue

            is_able = True
            for each_password in input_password:
                try:
                    if password.index(each_password[0]) > password.index(each_password[1]) or password.index(each_password[1]) > password.index(each_password[2]) or password.index(each_password[0]) > password.index(each_password[2]):
                        print(f"{password} : FALSE")
                        is_able = False
                        password = str(int(password) + 1)
                        break

                    is_able = True

                except:
                    print(f"{password} : FALSE")
                    is_able = False
                    password = str(int(password) + 1)
                    break

            if is_able is True:
                print(f"{password} : TRUE")
                return True


if __name__ == "__main__":
    euler = Euler()
    euler()
