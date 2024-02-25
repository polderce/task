from player import Player
from variants import Variants

# создаем экземпляр класса Player
bot = Player()

# При создании можем ни чего не передавать или же
# можем передать выбор (камень, ножницы или бумагу), а также имя

alex = Player(Variants.SCISSORS, 'Alex')

# далее через объект можем обратиться к функции whoWins
# и мы узнаем кто победил
print(bot.whoWins(bot, alex))
