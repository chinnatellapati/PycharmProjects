import random
class Dice:
    def roll(self):
        # num1 = (1, 2, 3, 4, 5, 6)
        # num2 = (1, 2, 3, 4, 5, 6)
        # val1 = random.choice(num1)
        # val2 = random.choice(num2)
        # return (val1, val2)
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())



