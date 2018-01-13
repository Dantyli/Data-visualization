from random import randint
class Die():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def roll(self):
        """返回一个位于1和骰(tou)子面数之间的随机数"""
        return randint(1,self.num_sides)