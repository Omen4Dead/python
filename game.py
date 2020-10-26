import itertools
import random


class NewGame:
    def __init__(self):
        self.flag = 0
        self.player_card = self.new_card()
        self.computer_card = self.new_card()
        self.barrels = [i for i in range(1, 91)]
        self.game()

    @staticmethod
    def new_card():
        digits = []
        while len(digits) < 27:
            a = random.randint(1, 90)
            if a in digits:
                continue
            else:
                digits.append(a)
        digits.sort()
        card = [[], [], []]

        for i in itertools.cycle([0, 1, 2]):
            try:
                card[i].append(digits.pop(0))
            except IndexError:
                break

        for i in range(0, 3):
            whitespace_pos = random.sample(range(9), 4)
            for pos in whitespace_pos:
                card[i][pos] = '  '
        return card

    def replace(self, lst, number):
        for row in lst:
            for i, val in enumerate(row):
                if val == number:
                    self.flag = 1
                    row[i] = '--'
        return lst, self.flag

    def next_step(self):
        new_barrel = random.choice(self.barrels)

        for i, el in enumerate(self.barrels):
            if el == new_barrel:
                self.barrels.pop(i)
        _, flag = self.replace(self.player_card, new_barrel)
        self.replace(self.computer_card, new_barrel)
        return new_barrel, flag

    def draw(self):
        print('------ Ваша карточка -----')
        for line in self.player_card:
            for element in line:
                print('{:>2} '.format(str(element)), end='')
            print()
        print('__________________________')
        print('-- Карточка компьютера ---')
        for line in self.computer_card:
            for element in line:
                print('{:>2} '.format(str(element)), end='')
            print()
        print('__________________________\n')

    def game(self):
        print('Новая игра!')
        self.draw()

        while True:
            if len(self.barrels) == 0:
                print('Конец игры! Бочонки закончились!')
                break
            self.flag = 0
            new, flag = self.next_step()
            print(f'Новый боченок: {new}. Осталось: {len(self.barrels)}')
            step = input('Зачеркнуть цифру? (Y/N)\n')
            if step.upper() == 'N':
                if flag == 1:
                    print('Конец игры!')
                    break
                elif flag == 0:
                    self.draw()
            elif step.upper() == 'Y':
                if flag == 1:
                    self.draw()
                elif flag == 0:
                    print('Конец игры!')
                    break


n = NewGame()
